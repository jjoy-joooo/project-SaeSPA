from flask import Blueprint, request, jsonify

from app.utilities.common_parameters import (
    get_boolean_summary_param,
    validate_file_upload,
)

from app.services import (
    pdf_service
    # perform_extract_text_from_pdf
)

text_extraction_blueprint = Blueprint("text_extraction", __name__)


@text_extraction_blueprint.route("/image", methods=["GET"])
def process_image_get():
    summary_param = get_boolean_summary_param()

    return jsonify(
        {
            "message": "Image processed successfully: ",
            "summary": summary_param,
        }
    )



@text_extraction_blueprint.route("/image", methods=["POST"])
def process_image():
    summary_param = get_boolean_summary_param()
    file, message, statusCode = validate_file_upload()
    text = pdf_service(file).perform_extract_text_from_pdf()

    print('------------------------------------ ')
    print('Test >>> ', text)

    return jsonify(
        {
            "summary": summary_param,
            "file": file.filename,
            "message": message,
            "statusCode": statusCode,
            "text": text
        }
    )


@text_extraction_blueprint.route("/pdf", methods=["POST"])
def process_pdf():
    summary_param = get_boolean_summary_param()

    return jsonify({"message": "Pdf processed successfully"})


@text_extraction_blueprint.route("/auio", methods=["POST"])
def process_audio():
    summary_param = get_boolean_summary_param()

    return jsonify({"message": "Auio processed successfully"})


@text_extraction_blueprint.route("/video", methods=["POST"])
def process_video():
    summary_param = get_boolean_summary_param()

    return jsonify({"message": "Video processed successfully"})
