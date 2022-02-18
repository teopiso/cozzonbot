import instaloader
import os
import random

dir_path = os.path.dirname(os.path.realpath(__file__))
ig = instaloader.Instaloader(dirname_pattern=dir_path+'/ig/{target}', save_metadata=False, download_videos=False, download_video_thumbnails=True, download_comments=False, sleep=False)

users=[] #nomi IG delle pupille

def download_post():
    username=random.choice(users)
    posts = instaloader.Profile.from_username(ig.context, username).get_posts()
    #salva i primi x post dell'utente
    ig.posts_download_loop(posts, username, fast_update=True, max_count=1)
    cleartxt(username)
    return username

def cleartxt(user):
    fold=dir_path+'/ig/'+user
    folder = os.listdir(fold)
    for item in folder:
        if item.endswith(".txt"):
            os.remove(os.path.join(fold, item))
