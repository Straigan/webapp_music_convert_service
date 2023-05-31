from pydub import AudioSegment
import os

from webapp.config import UPLOAD_FOLDER, DOWNLOAD_FOLDER, UPLOAD_ALLOWED_EXTENSIONS


def allowed_file(filename: str) -> bool:
    """Проверка файла на разрешенное расширение"""
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in UPLOAD_ALLOWED_EXTENSIONS


def process_convert_wav_to_mp3(filename_extension_wav: str, filename_extension_mp3: str) -> None:
    """Процесс конвертирование записи из wav в mp3"""
    AudioSegment.from_wav(os.path.join(UPLOAD_FOLDER, filename_extension_wav)).export(os.path.join(DOWNLOAD_FOLDER, filename_extension_mp3), format="mp3", codec="libmp3lame")
