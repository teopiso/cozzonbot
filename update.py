import instaloader
import os
import random
n=0
USER = ''
PASSWORD = ''
dir_path = os.path.dirname(os.path.realpath(__file__))
ig = instaloader.Instaloader(dirname_pattern=dir_path+'/ig/{target}', save_metadata=False, download_videos=False, download_video_thumbnails=True, download_comments=False, sleep=False)

ig.login(USER, PASSWORD)

users=[]#lista IG pupille

for user in users:
    ig.download_profile(user,fast_update=True, profile_pic=False)
    fold=dir_path+'/ig/'+user
    folder = os.listdir(fold)
    for item in folder:
        if item.endswith(".txt"):
            os.remove(os.path.join(fold, item))
