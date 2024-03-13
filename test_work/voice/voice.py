import openai
import speech_recognition as sr
import os
from dotenv import load_dotenv

load_dotenv()

class AudioTextConverter:
    def recognize_audio(self, audio_file_path):
        # 음성을 텍스트로 변환하는 메소드입니다.

        # 음성 인식기 인스턴스 생성
        recognizer = sr.Recognizer()

        # 오디오 파일 열기
        with sr.AudioFile(audio_file_path) as source:
            # 오디오 데이터 읽기
            audio_data = recognizer.record(source)

        try:
            # Google 웹 음성 API를 사용하여 오디오 데이터를 텍스트로 변환합니다.
            text = recognizer.recognize_google(audio_data, language="ko-KR")
            return text
        except sr.UnknownValueError:
            # 인식할 수 없는 오디오 데이터일 경우 에러 메시지 출력
            print("음성을 인식하지 못했습니다.")
        except sr.RequestError as e:
            # Google 웹 음성 API 요청 중 에러가 발생한 경우 에러 메시지 출력
            print(f"Google Web Speech API 요청 에러: {e}")
            return None

class TextSummarizer:
    def __init__(self, api_key):
        # 텍스트 요약기 클래스의 생성자입니다.

        # API 키를 저장하는 변수입니다.
        self.api_key = api_key
        # OpenAI API에 접근하기 위한 openai 모듈을 가져옵니다.
        self.openai = openai
        # OpenAI API에 접근하기 위한 API 키 설정
        self.openai.api_key = api_key

    def summarize_text(self, user_text, lang="en"):
        # 텍스트를 요약하는 메소드입니다.

        # 사용자가 입력한 텍스트를 요약 요청 메시지 형식으로 변환합니다.
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

        # OpenAI의 ChatCompletion API를 사용하여 텍스트 요약을 수행합니다.
        response = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000,
            temperature=0.3,
            n=1
        )

        # 요약된 텍스트를 반환합니다.
        summary = response["choices"][0]["message"]["content"]
        return summary


        response = self.openai.ChatCompletion.create(
            model="gpt-3.5-turbo", # 사용할 모델 선택
            messages=messages, # 전달할 메시지 지정
            max_tokens=2000, # 응답 최대 토큰 수 지정
            temperature=0.3, # 완성의 다양성을 조절하는 온도 설정
            n=1 # 생성할 완성 개수 지정
        )

        summary = response["choices"][0]["message"]["content"]
        return summary

# 현재 작업 디렉토리를 얻어옴
current_directory = os.getcwd()

# 음성 파일 이름
audio_filename = "baseball_lecture_1min.wav"

# 음성 파일 경로 (상대경로)
audio_file_path = os.path.join(current_directory, audio_filename)

# API 키 설정
api_key = os.environ.get('api_key')

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
