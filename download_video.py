import yt_dlp
import os

def download_video(url,saveas,name):
    # Assurez-vous que le dossier de sauvegarde existe
    os.makedirs(os.path.dirname(saveas), exist_ok=True)

    ydl_opts = {
        'format': 'bestvideo[height<=1080][ext=mp4]+bestaudio/best[height<=1080]',  # Télécharge les vidéos avec une résolution maximale de 1080p
        'outtmpl': os.path.join(saveas, 'vo'),  # Enregistrer dans le chemin spécifié
        'ffmpeg_location': 'C:/ffmpeg.exe',  # Spécifiez le chemin complet vers ffmpeg
    }
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])
