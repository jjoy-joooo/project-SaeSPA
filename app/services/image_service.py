from google.cloud import vision


class image_service:
    def __init__(self, file):
        self.file = file

    # 비즈니스 로직
    def perform_extract_text(self):
        content = self.file.read()

        client = vision.ImageAnnotatorClient()
        image = vision.Image(content=content)

        response = client.text_detection(image=image)
        texts = response.text_annotations
        detected_texts = " ".join([text.description for text in texts])

        if detected_texts:
            return detected_texts, None, 200
        else:
            return None, "텍스트를 감지하지 못했습니다.", 400
