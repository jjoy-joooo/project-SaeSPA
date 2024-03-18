from flask import Blueprint, jsonify

from app.services import image_service, pdf_service, video_service, voice_service
from app.utilities.common_parameters import (
    get_boolean_summary_param,
    validate_file_upload,
)

text_extraction_blueprint = Blueprint("text_extraction", __name__)


@text_extraction_blueprint.route("/image", methods=["GET"])
def process_api_test():
    summary_param = get_boolean_summary_param()

    return jsonify(
        {
            "message": "Image processed successfully: ",
            "summary": summary_param,
        }
    )


@text_extraction_blueprint.route("/image", methods=["POST"])
def process_image():
    file, message, statusCode = validate_file_upload()
    text = image_service(file).perform_extract_text()

    # 제거 예정
    summary_param = get_boolean_summary_param()

    return jsonify(
        {
            "summary": summary_param,
            "file": file.filename,
            "message": message,
            "statusCode": statusCode,
            "text": text,
        }
    )


@text_extraction_blueprint.route("/pdf", methods=["POST"])
def process_pdf():
    file, message, statusCode = validate_file_upload()
    text = pdf_service(file).perform_extract_text()

    return jsonify(
        {
            "file": file.filename,
            "message": message,
            "statusCode": statusCode,
            "text": text,
        }
    )


@text_extraction_blueprint.route("/voice", methods=["POST"])
def process_audio():
    file, message, statusCode = validate_file_upload()
    text = voice_service(file).perform_extract_text()

    return jsonify(
        {
            "file": file.filename,
            "message": message,
            "statusCode": statusCode,
            "text": text,
        }
    )


@text_extraction_blueprint.route("/video", methods=["POST"])
def process_video():
    file, message, statusCode = validate_file_upload()
    text = video_service(file).perform_extract_text()

    return jsonify(
        {
            "file": file.filename,
            "message": message,
            "statusCode": statusCode,
            "text": text,
        }
    )
