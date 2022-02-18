from itertools import islice
from math import ceil
import os
from instaloader import Instaloader, Profile

PROFILE = ''        # profile to download from
X_percentage = 5    # percentage of posts that should be downloaded
dir_path = os.path.dirname(os.path.realpath(__file__))

L = Instaloader(dirname_pattern=dir_path+'\\ig\\{target}', save_metadata=False, download_videos=False, download_video_thumbnails=True, download_comments=False, sleep=False)
L.interactive_login('nerina.elf') 
profile = Profile.from_username(L.context, PROFILE)
posts_sorted_by_likes = sorted(profile.get_posts(),
                               key=lambda p: p.likes + p.comments,
                               reverse=True)

for post in islice(posts_sorted_by_likes, ceil(profile.mediacount * X_percentage / 100)):
    L.download_post(post, PROFILE)