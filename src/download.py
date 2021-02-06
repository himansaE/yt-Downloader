from pytube.contrib.playlist import Playlist, YouTube
from os import mkdir
import time
from console import color
from progress import on_complete, on_progress
from converter import file_size, seconds


def YTPlaylist(pl: Playlist):
    color.green('\n' + pl.title)
    color.green(f'{len(pl.video_urls)} videos found.\n')
    output_path = "./" + pl.title
    try:
        mkdir(pl.title)
    except:
        pass
    video_count = 0
    for video in pl.videos:
        video.video_id
        video_start_time = time.time()
        color.yellow(f"\n\n[{video_count} of {len(pl.video_urls)}]")
        video.register_on_progress_callback(on_progress)
        video.register_on_complete_callback(on_complete)
        print("Title 🔥 : " + video.title)
        print("Size  📂 :  " + file_size(video.streams.first().filesize) + "\n")

        video.streams.filter(progressive=True).first().download(
            output_path=output_path)

        print(
            f"\n Got  🕓 {seconds(time.time()-video_start_time)} to download.")
        video_count += 1


def YTVideo(video: YouTube):
    print("Title 🔥 : " + video.title)
    print("Size  📂 :  " + file_size(video.streams.first().filesize) + "\n")
    video_start_time = time.time()
    video.register_on_progress_callback(on_progress)
    video.streams.filter(progressive=True).first().download()

    print(
        f"\n Got  🕓 {seconds(time.time()-video_start_time)} to download.")
