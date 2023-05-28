from pydub import AudioSegment
import os

from webapp.config import UPLOAD_FOLDER, DOWNLOAD_FOLDER, UPLOAD_ALLOWED_EXTENSIONS


def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in UPLOAD_ALLOWED_EXTENSIONS

def process_convert_wav_to_mp3(filename):
    filename_no_extension = '.' in filename and filename.rsplit('.', 1)[0].lower()
    AudioSegment.from_wav(os.path.join(UPLOAD_FOLDER, filename)).export(os.path.join(DOWNLOAD_FOLDER, filename_no_extension + '.mp3'), format="mp3", codec="libmp3lame")