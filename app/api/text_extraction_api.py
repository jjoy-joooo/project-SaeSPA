from flask import Blueprint, request, jsonify

from utilities import convert_not_true_to_false

text_extraction = Blueprint('text_extraction', __name__)

REQUEST_PARAMETER_NAME = 'summary'

@text_extraction.route('/image', methods=['POST'])
def process_image():
    result = convert_not_true_to_false(request.args.get(REQUEST_PARAMETER_NAME, default=False))
    
    return jsonify({"message": "Image processed successfully"})

@text_extraction.route('/pdf', methods=['POST'])
def process_pdf():
    result = convert_not_true_to_false(request.args.get(REQUEST_PARAMETER_NAME, default=False))
        
    return jsonify({"message": "Pdf processed successfully"})

@text_extraction.route('/auio', methods=['POST'])
def process_audio():
    result = convert_not_true_to_false(request.args.get(REQUEST_PARAMETER_NAME, default=False))
        
    return jsonify({"message": "Auio processed successfully"})

@text_extraction.route('/video', methods=['POST'])
def process_video():
    result = convert_not_true_to_false(request.args.get(REQUEST_PARAMETER_NAME, default=False))
        
    return jsonify({"message": "Video processed successfully"})
