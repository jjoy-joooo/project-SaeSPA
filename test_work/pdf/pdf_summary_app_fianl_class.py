import streamlit as st
from PyPDF2 import PdfReader
import textwrap
import os
import openai
import tiktoken
from dotenv import load_dotenv

class PDFSummarizer:
    load_dotenv()
    api_key_path=os.environ.get('api_key_path')

    def __init__(self, api_key_path):
        self.api_key_path = api_key_path
        self.openai=openai
        self.openai.api_key_path = api_key_path
        # self.load_api_key()

    # def load_api_key(self):
    #     with open(self.api_key_path, 'r') as file:
    #         api_key = file.read().strip()
    #     openai.api_key = api_key

    def summarize_text(self, user_text, lang="en"): 
        if lang == "en":
            messages = [{"role": "system", "content": "You are a helpful assistant in the summary."},
                        {"role": "user", "content": f"Summarize the following. \n {user_text}"}]
        elif lang == "ko":
            messages = [{"role": "system", "content": "You are a helpful assistant in the summary."},
                        {"role": "user", "content": f"다음의 내용을 한국어로 요약해 주세요 \n {user_text}"}]

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=messages,
            max_tokens=2000,
            temperature=0.3,
            n=1
        )
        summary = response["choices"][0]["message"]["content"]
        return summary

    def summarize_text_final(self, text_list, lang='en'):
        joined_summary = " ".join(text_list)
        enc = tiktoken.encoding_for_model("gpt-3.5-turbo")
        token_num = len(enc.encode(joined_summary)) 
        req_max_token = 2000 
        final_summary = ""

        if token_num < req_max_token: 
            final_summary = self.summarize_text(joined_summary, lang)
        
        return token_num, final_summary


    def summarize_PDF_file(self, pdf_file, lang):
        if pdf_file is not None:
            st.write("PDF 문서를 요약 중입니다. 잠시만 기다려 주세요.")
            reader = PdfReader(pdf_file) 

            text_summaries = []
            
            for page in reader.pages:
                page_text = page.extract_text() 
                text_summary = self.summarize_text(page_text, lang)
                text_summaries.append(text_summary)
                
            token_num, final_summary = self.summarize_text_final(text_summaries, lang)
            
            if final_summary != "":
                shorten_final_summary = textwrap.shorten(final_summary, 250, placeholder=' [..이하 생략..]')
                st.write("- 최종 요약(축약):", shorten_final_summary) 
            else:
                pass
                st.write("- 통합한 요약문의 토큰 수가 커서 요약할 수 없습니다.")

# path1 = "C:\\Users\\bluecom010\\Desktop\\지의\\24_03_06_프로젝트"
# path2 = "OpenAI_API.txt"
# # os.path.join()을 사용하여 경로 결합
# api_key_path = os.path.join(path1, path2)
# # print(api_key_path)

# # 현재 작업 디렉토리를 가져옴
# current_dir = os.getcwd()
# # 상대 경로 설정
# relative_path1 = "OpenAI_API.txt"
# # os.path.join()을 사용하여 경로 결합
# api_key_path = os.path.join(current_dir, relative_path1)
# # print("출력", api_key_path)

# api_key_path = 'C:\\Users\\bluecom010\\Desktop\\지의\\24_03_06_프로젝트\\OpenAI_API.txt'
# pdf_summarizer = PDFSummarizer(self, api_key_path)

# uploaded_file = st.file_uploader("PDF 파일을 업로드하세요.", type='pdf')
# print("going well")
# if uploaded_file:
#     lang_code = 'en' 
#     pdf_summarizer.summarize_PDF_file(uploaded_file, lang_code)
#     print("Done")
