import openai
import speech_recognition as sr

class AudioTextConverter:
    def recognize_audio(self, audio_file_path):
        recognizer = sr.Recognizer()

        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="ko-KR")
            return text
        except sr.UnknownValueError:
            print("음성을 인식하지 못했습니다.")
        except sr.RequestError as e:
            print(f"Google Web Speech API 요청 에러: {e}")
            return None

class TextSummarizer:
    def __init__(self, api_key):
        self.api_key = api_key
        self.openai = openai
        self.openai.api_key = api_key

    def summarize_text(self, user_text, lang="en"):
        if lang == "en":
            messages = [
                {"role":"system", "content":"You are a helpful assistant in summary."},
                {"role":"user", "content":f"Summarize the following. \n {user_text}"}
            ]
        elif lang == "ko":
            messages = [
                {"role":"system", "content":"You are a helpful assistant in summary."},
                {"role":"user", "content":f"다음의 내용을 한국어로 요약해 주세요. \n {user_text}"}
            ]

        response = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000,
            temperature=0.3,
            n=1
        )

        summary = response["choices"][0]["message"]["content"]
        return summary

# 음성 파일 경로
audio_file_path = "./baseball_lecture_1min.wav"

# API 키 설정
api_key = "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"

# 클래스 인스턴스 생성
summarizer = TextSummarizer(api_key)
audio_converter = AudioTextConverter()

# 음성 파일을 텍스트로 변환
audio_text = audio_converter.recognize_audio(audio_file_path)

if audio_text:
    # 음성으로부터 추출된 텍스트를 요약
    summarized_text = summarizer.summarize_text(audio_text, lang="ko")
    print("음성 파일에서 추출된 텍스트를 요약한 결과:")
    print(summarized_text)
