from flask import Blueprint, jsonify, request
import os
from werkzeug.utils import secure_filename

from webapp.config import UPLOAD_FOLDER
from webapp.services.service_convert_wav_to_mp3 import allowed_file, process_convert_wav_to_mp3
from webapp.users.models import User


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/api/v1.0/upload_record', methods=['POST'])
def upload_record():
    upload_record_id_user = request.form['id_user']
    upload_record_access_token_user = request.form['access_token_user']
    upload_record_file_record = request.files['file_wav']
    upload_record_user_upload_record = User.query.filter_by(id=int(upload_record_id_user)).first()
    if upload_record_file_record and allowed_file(upload_record_file_record.filename) and upload_record_user_upload_record != None and upload_record_access_token_user == upload_record_user_upload_record.access_token:
        filename = secure_filename(upload_record_file_record.filename)
        upload_record_file_record.save(os.path.join(UPLOAD_FOLDER, filename))
        process_convert_wav_to_mp3(filename)
        resp = jsonify({'message' : 'File successfully uploaded'})
        resp.status_code = 201
        return resp
    else:
        return {'error': 'error data'}
