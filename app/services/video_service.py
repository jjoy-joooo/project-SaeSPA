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