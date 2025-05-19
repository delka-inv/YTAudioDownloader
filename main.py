import yt_dlp
import os
import shutil
import time

PATH_OUTPUT = os.path.abspath('./!OUTPUT/')
PATH_FFMPEG = os.path.abspath('./bin/')

def download_audio_from_youtube(url):
    temp_dir = 'temp_audio'
    os.makedirs(temp_dir, exist_ok=True)

    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(temp_dir, '%(title)s.%(id)s.%(ext)s'),
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
        'quiet': False,
        'no_warnings': True,
        'ffmpeg_location': PATH_FFMPEG,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

    for file in os.listdir(temp_dir):
        if file.endswith('.mp3'):
            src = os.path.join(temp_dir, file)
            dst = os.path.join(PATH_OUTPUT, file)
            if os.path.exists(dst):
                os.remove(dst)
            shutil.move(src, dst)
            print(f'Файл сохранён как: {dst}')

    # Очистка временной папки
    os.rmdir(temp_dir)

def create_directory():
    os.makedirs(PATH_OUTPUT, exist_ok=True)

if __name__ == "__main__":
    create_directory()
    url = input("Введите URL видео с YouTube: ").strip()
    download_audio_from_youtube(url)
