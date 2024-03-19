import io

import speech_recognition as sr


class voice_service:
    def __init__(self, file):
        self.audio_stream = io.BytesIO(file.read())

    # 비즈니스 로직
    def perform_extract_text(self):
        recognizer = sr.Recognizer()

        with sr.AudioFile(self.audio_stream) as source:
            audio_data = recognizer.record(source)

        try:
            text = recognizer.recognize_google(audio_data, language="ko-KR")
            return text, None, 200
        except sr.UnknownValueError:
            message = "음성을 인식하지 못했습니다."
        except sr.RequestError as e:
            message = f"Google Web Speech API 요청 에러: {e}"

        return None, message, 500
