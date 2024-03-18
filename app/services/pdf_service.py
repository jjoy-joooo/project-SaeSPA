from PyPDF2 import PdfReader

from app.utilities.common_parameters import get_boolean_summary_param

from .summary_service import summary_service


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

        if length_page == 1:
            page = reader.pages[0]
            text_summary = self._extract_text(page)

            if is_summary == True:
                text_summary = summary_service(text_summary)

            return text_summary

        text_summaries = []
        for page in reader.pages:
            page_text = self._extract_text(page)

            if is_summary == True:
                page_text = summary_service(page_text)

            text_summaries.append(page_text)

        all_pdf_text = " ".join(text_summaries)

        if is_summary == True:
            all_pdf_text = summary_service(all_pdf_text)

        return all_pdf_text
