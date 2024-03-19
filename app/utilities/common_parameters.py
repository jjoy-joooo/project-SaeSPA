from flask import request, jsonify


def get_boolean_summary_param():
    return request.args.get("summary", default="false").lower() == "true"


def validate_file_upload():
    if "file" not in request.files:
        return None, "No file part", 400

    file = request.files["file"]
    if file.filename == "":
        return None, "No selected file", 400

    return file, "File uploaded successfully", 200
