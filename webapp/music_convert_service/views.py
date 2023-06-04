from flask import Blueprint, jsonify, request, send_file
import os
from werkzeug.utils import secure_filename
from uuid import uuid4

from webapp.config import DOWNLOAD_FOLDER, PORT, UPLOAD_FOLDER
from webapp.db import db
from webapp.services.service_convert_wav_to_mp3 import allowed_file, process_convert_wav_to_mp3
from webapp.music_convert_service.models import Record
from webapp.users.models import User


blueprint = Blueprint('kanal_service', __name__)

@blueprint.route('/upload_record', methods=['POST'])
def upload_record():
    """загрузка записи с расширением wav на сервер, с дальнешим ей конвертирование в mp3"""
    upload_record_id_user = request.form['id_user']
    upload_record_access_token_user = request.form['access_token_user']
    upload_record_file_record = request.files['file_wav']
    print(upload_record_file_record)
    upload_record_user_upload_record = User.query.filter_by(id=int(upload_record_id_user)).first()
    
    if upload_record_file_record.filename == '':
        resp = jsonify({'message' : 'No file selected for uploading'})
        resp.status_code = 400
        return resp
    
    if upload_record_file_record and allowed_file(upload_record_file_record.filename) and upload_record_access_token_user == upload_record_user_upload_record.access_token:
        filename_extension_wav = secure_filename(upload_record_file_record.filename)
        upload_record_file_record.save(os.path.join(UPLOAD_FOLDER, filename_extension_wav)) 

        filename_extension_mp3 = str(uuid4()) + '.mp3'
        print(filename_extension_mp3)

        process_convert_wav_to_mp3(filename_extension_wav, filename_extension_mp3)
        
        add_record = Record(
            name=filename_extension_mp3,
            user_id=upload_record_id_user
        )
        db.session.add(add_record)
        db.session.commit()
        
        record = Record.query.filter_by(name=filename_extension_mp3).first()
        resp = f'http://localhost:{PORT}/record?id={record.id}&user={upload_record_id_user}', 201

        return resp
    else:
        resp = jsonify({'message' : 'error post data'})
        resp.status_code = 400
        return resp
    


@blueprint.route('/record', methods=['GET'])
def download_record():
    """Предоставление доступа на скачивание конвертированного файла из wav в mp3"""
    download_record_id_record = request.json['id']
    download_record_id_user = request.json['user']
    record = Record.query.filter_by(id=int(download_record_id_record)).first()
    if record != None and record.user_id == int(download_record_id_user):
        return send_file(os.path.join(DOWNLOAD_FOLDER, record.name))
    else:
        return {'error': 'error data'}
