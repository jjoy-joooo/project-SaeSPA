import os
import subprocess
import speech_recognition as sr
import noisereduce as nr
import librosa
import soundfile as sf
import openai
from dotenv import load_dotenv


##영상->음성 파일 변환

class AudioProcessor:
    def __init__(self):
        self.openai_api_key = os.getenv("OPENAI_API_KEY")
        # 현재 파일의 디렉토리 경로를 구합니다.
        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.ffmpeg_path = os.path.join(self.current_dir, "ffmpeg", "bin", "ffmpeg.exe")
    def extract_audio(self, input_video_path, output_audio_path):
        # 상대 경로를 절대 경로로 변환합니다.
        input_video_path = os.path.join(self.current_dir, input_video_path)
        output_audio_path = os.path.join(self.current_dir, output_audio_path)
        
        command = [
            self.ffmpeg_path,
            "-i", input_video_path,
            "-vn",
            "-acodec", "pcm_s16le",
            "-ar", "16000",
            "-ac", "1",
            output_audio_path
        ]
        subprocess.run(command)


### 노이즈 제거
    def reduce_noise(self, input_file_path, output_file_path):
        input_file_path = os.path.join(self.current_dir, input_file_path)
        output_file_path = os.path.join(self.current_dir, output_file_path)
        
        audio, rate = librosa.load(input_file_path, sr=None)
        reduced_noise_audio = nr.reduce_noise(y=audio, sr=rate)
        sf.write(output_file_path, reduced_noise_audio, rate)

##음성 텍스트화

    def recognize_audio(self, audio_file_path, language="ko-KR"):
        audio_file_path = os.path.join(self.current_dir, audio_file_path)
        
        recognizer = sr.Recognizer()
        with sr.AudioFile(audio_file_path) as source:
            audio_data = recognizer.record(source)
        try:
            text = recognizer.recognize_google(audio_data, language=language)
            return text
        except sr.UnknownValueError:
            print("음성을 인식하지 못했습니다.")
        except sr.RequestError as e:
            print(f"Google Web Speech API 요청 에러: {e}")
            return None
        
##요약

    def summarize_text(self, user_text, lang="en"):
        openai.api_key = self.openai_api_key
        messages = [
            {"role": "system", "content": "You are a helpful assistant in summary."},
            {"role": "user", "content": f"Summarize the following. \n {user_text}"}
        ]
        if lang == "ko":
            messages[1]["content"] = f"다음의 내용을 한국어로 요약해 주세요. \n {user_text}"

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000,
            temperature=0.3,
            n=1
        )
        summary = response["choices"][0]["message"]["content"]
        return summary
    
##테스트코드
    

# 인스턴스 생성
processor = AudioProcessor()

# 비디오에서 오디오 추출
processor.extract_audio("C:\\Users\\user\\Desktop\\Module\\project-SaeSPA\\test_work\\video\\PRODUCE 101.mp4", "output_audio.wav")


# 오디오에서 소음 감소
processor.reduce_noise("output_audio.wav", "reduced_noise_audio.wav")

# 오디오 파일을 텍스트로 변환
recognized_text = processor.recognize_audio("reduced_noise_audio.wav")
print("인식된 텍스트:", recognized_text)

# 텍스트 요약
if recognized_text is not None:
    summary = processor.summarize_text(recognized_text, lang="ko")
    print("요약된 텍스트:", summary)


