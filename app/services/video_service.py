import io
import os
import subprocess
import uuid

"""
1. mp4(영상) -> m4a(음성) 파일로 변환
2. m4a(음성) -> wav(음성) 확장자 변환
    - m4a 텍스트 추출 인식 불가
    - 궁금한 점: mp4 -> wav로 왜 바로 변환하지 않았는가?
3. 소음 제거
4. 텍스트 추출
@. 요약 여부에 따라 요약 또는 텍스트 진행
"""


class video_service:
    def __init__(self, file):
        self.file = file

        self.current_dir = os.path.dirname(os.path.abspath(__file__))
        self.ffmpeg_path = os.path.join(self.current_dir, "ffmpeg", "bin", "ffmpeg.exe")
        self.video_path = os.path.join(self.current_dir, "tmpFiles", "video")
        self.voice_path = os.path.join(self.current_dir, "tmpFiles", "voice")

    def _create_filename(self, extension):
        return f"{uuid.uuid4()}.{extension}"

    def _save_temp_video(self, path, file_name):
        print(">>>>>>>>>>>>>>>>> ", self.file)
        file_path = os.path.join(path, file_name)
        self.file.save(file_path)

        return file_path

    def _remove_file(self, file_path):
        if os.path.exists(file_path):
            os.remove(file_path)

    # 영상 -> 음성 파일 변환
    def _extract_audio(self):
        # 비디오 임시파일 생성
        video_file_name = self._create_filename("mp4")
        video_file_path = self._save_temp_video(self.video_path, video_file_name)
        self.video_path = video_file_path

        # 영상 -> 음성 변환
        voice_file_name = self._create_filename("wav")
        voice_file_path = os.path.join(self.voice_path, voice_file_name)
        self.voice_path = voice_file_path

        command = [
            self.ffmpeg_path,
            "-i",
            self.video_path,
            "-vn",
            "-acodec",
            "pcm_s16le",
            "-ar",
            "16000",
            "-ac",
            "1",
            voice_file_path,
        ]

        subprocess.run(command)

    # 음성 노이즈 제거
    def _reduce_noise():
        pass

    # 음성 텍스트화
    def _extract_audio_aaaaaaaaaa():
        pass

    # 비즈니스 로직
    def perform_extract_text(self):
        self._extract_audio()
        # recognizer = sr.Recognizer()

        # with sr.AudioFile(self.audio_stream) as source:
        #     audio_data = recognizer.record(source)

        # try:
        #     text = recognizer.recognize_google(audio_data, language="ko-KR")
        #     return text[0], None, 200
        # except sr.UnknownValueError:
        #     message = "음성을 인식하지 못했습니다."
        # except sr.RequestError as e:
        #     message = f"Google Web Speech API 요청 에러: {e}"

        return None, "message", 200
