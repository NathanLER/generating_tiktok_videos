from moviepy.editor import *
from random import randint
import os




def crete_vid(video,jeux,nom_vid,timecode,part,name):
    rand=randint(0,720)
    video1 = VideoFileClip(video).subclip(timecode, timecode+61)
    video2 = VideoFileClip(jeux).subclip(rand,rand+61)
    audio1 = video1.audio

    # Redimensionner les vidéos en conservant le ratio d'aspect
    video1_resized = video1.resize(height=900)
    video2_resized = video2.resize(height=900)

    # Extraire la partie centrale des vidéos
    video1_center = video1_resized.crop(x_center=video1_resized.w / 2, y_center=video1_resized.h / 2, width=video1_resized.w / 2, height=video1_resized.h)
    video2_center = video2_resized.crop(x_center=video2_resized.w / 2, y_center=video2_resized.h / 2, width=video2_resized.w / 2, height=video2_resized.h/1.2)

    # Choisir quelle vidéo sera en haut
    video_up, video_down = video1_center, video2_center

    # Combinaison des vidéos
    final_video = clips_array([[video_up], [video_down]])

    # Ajouter le son de la première vidéo à la vidéo finale
    final_video = final_video.set_audio(audio1)

    # Ajouter du texte blanc au centre de la vidéo
    txt = TextClip(name, fontsize=100, color='white', method='caption',bg_color="red", stroke_color="black",stroke_width=3)
    txt = txt.set_position(('center', final_video.h * 0.55)).set_duration(final_video.duration/10)

    # Créer un contour noir autour du texte
    contour = txt.on_color(size=(txt.w + 10, txt.h + 10), color=(0, 0, 0), pos=('center', 'center'), col_opacity=0)
    contour = contour.set_position(('center', final_video.h * 0.55)).set_duration(final_video.duration/10)

    # Superposer le texte blanc sur la vidéo
    final_video_with_text = CompositeVideoClip([final_video, txt])

    # Superposer le contour noir autour du texte blanc
    final_video_with_text_with_contour = CompositeVideoClip([final_video_with_text, contour])

    final_video_with_text_with_contour.write_videofile(nom_vid + '/' + nom_vid +' - ' +part + ".mp4", codec="libx264", bitrate="3000k", fps=30)



'''
    # Enregistrer la vidéo finale avec le codec H.264 et un débit binaire de 8000 kbit/s
    final_video_with_text_with_contour.write_videofile(nom_vid + '/' + nom_vid +' - ' +part + ".mp4", codec="libx264", bitrate="3000k", fps=30)

 libx264
 '''