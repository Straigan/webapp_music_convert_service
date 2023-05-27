from flask import Blueprint, jsonify, request
import os
from werkzeug.utils import secure_filename

from webapp.config import ALLOWED_EXTENSIONS
from webapp.config import UPLOAD_FOLDER


blueprint = Blueprint('kanal_service', __name__)

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@blueprint.route('/api/v1.0/upload_wav', methods=['POST'])
def upload_wav():
    file_wav = request.files['file_wav']
    if file_wav and allowed_file(file_wav.filename):
        filename = secure_filename(file_wav.filename)
        file_wav.save(os.path.join(UPLOAD_FOLDER, filename))
        resp = jsonify({'message' : 'File successfully uploaded'})
        resp.status_code = 201
        return resp
