from sys import argv, exit


from os import error, mkdir
import time
from colors import color
from progress import on_complete, on_progress, clear
from converter import file_size, seconds
from pytube import Playlist
from urllib import error as url_err
from cursor import hide as cursor_hide

clear()
color.red("Youtube Playlist Downloader.")


if(len(argv) >= 2):
    url = argv[1]
else:
    url = input("\nplaylist url :\t")
pl = None
try:
    pl = Playlist(url)
except url_err.URLError:
    color.red("\n❗ seems connection Error\n")
    exit()
except:
    color.red("\n⨯ somthing went wrong\n")
    exit()

color.green('\n' + pl.title)
color.green(f'{len(pl.video_urls)} videos found.\n')

output_path = "./" + pl.title
pl_start_time = time.time()

try:
    mkdir(pl.title)
except:
    pass
cursor_hide()
vid_num = 0
for video in pl.videos:
    video.video_id
    video_start_time = time.time()
    color.yellow(f"\n\n[{vid_num} of {len(pl.video_urls)}]")
    video.register_on_progress_callback(on_progress)
    video.register_on_complete_callback(on_complete)
    print("Title 🔥 : " + video.title)
    print("Size  📂 :  " + file_size(video.streams.first().filesize) + "\n")

    video.streams.filter(progressive=True).first().download(
        output_path=output_path)

    print(f"\n Got  🕓 {seconds(time.time()-video_start_time)} to download.")
    vid_num += 1
