from formatage_video import crete_vid
from download_video import *
import os
from  durre_video import get_video_duration

def creation_de_partie(link,name_dos,name,partie):
    if not os.path.exists(name_dos):
        # Créez le dossier s'il n'existe pas déjà
        os.makedirs(name_dos)

    download_video(link,name_dos+'/',name)


    durre=int(get_video_duration(name_dos+'/vo.mp4'))
    nb_part= int((durre-61)/61)

    for i in range(int(partie)-1,nb_part):
        crete_vid((name_dos+'/vo.mp4'),'vog/jeux/1.webm',name_dos,i*61,'part'+str(i+1),name)



lien = input('lien : ')
nom_dossier = input('nom dossier: ')
titre = input('Titre : ' )
partie = input('partie : ')

creation_de_partie(lien,nom_dossier,titre,partie)
