from PyPDF2 import PdfReader
from .summary_service import summary_service

from app.utilities.common_parameters import (
    get_boolean_summary_param,
)


"""
1. 텍스트 추출
@. 요약 여부에 따라 요약 또는 텍스트 진행
"""
class pdf_service:
    def __init__(self, file):
        self.file = file
        
    # 텍스트 추출
    def _extract_text(self, page):
        page_text = page.extract_text()
        return page_text
    
    # 비즈니스 로직
    def perform_extract_text_from_pdf(self):
        reader = PdfReader(self.file)
        length_page = len(reader.pages)
        is_summary = get_boolean_summary_param()
        
        if (length_page == 1):
            page = reader.pages[0]
            text_summary = self._extract_text(page)

            if(is_summary == True):
                text_summary = summary_service(text_summary)

            return text_summary
        
        text_summaries = []
        for page in reader.pages:
            page_text = self._extract_text(page)

            if(is_summary == True):
                page_text = summary_service(page_text)

            text_summaries.append(page_text)

        all_pdf_text = " ".join(text_summaries)

        if(is_summary == True):
            all_pdf_text = summary_service(all_pdf_text)

        return all_pdf_text
        # for page in reader.pages:
        # 1. PDF 장수 확인(1장인가?)
        # 2. Yes
            # 1. 텍스트 추출
            # 2. 요약 기능 사용 여부 확인
                # 1. Yes
                    # 요약
                # 2. No
                    # 요약 X
        # 3. No(for 이용)
            # 1. 텍스트 추출
            # 2. 요약 기능 사용 여부 확인
                # 1. Yes
                    # 요약
                # 2. No
                    # 요약 X
            # 3. 배열에 추출된거 또는 요약된거 담기.
            # 4. 요약 기능 사용 여부 확인
                # 1. Yes
                    # 전체 배열 추출된거 한번 더 요약
                # 2. No
                    # 요약 X
# class TextProcessor:
#     def __init__(self, file_path):
#         self.file_path = file_path
#         self.text = None
#     def extract_text(self):
#         # 파일로부터 텍스트를 추출하는 로직 구현
#         # 예시로는, 파일을 열고 내용을 읽는 기본적인 처리를 포함할 수 있습니다.
#         # 실제 텍스트 추출 방법은 파일 유형(PDF, 이미지 등)에 따라 달라질 수 있습니다.
#         with open(self.file_path, 'r') as file:
#             self.text = file.read()
#         return self.text
#     def summarize_text(self):
#         # 텍스트를 요약하는 로직 구현
#         # 이 부분에서는 단순화를 위해 텍스트의 일부를 반환하는 예시로 구현합니다.
#         # 실제로는 자연어 처리 라이브러리를 사용하여 요약을 구현할 수 있습니다.
#         if self.text is None:
#             self.extract_text()
#         summary = self.text[:100]  # 예시로 첫 100자만을 요약으로 사용
#         return summary