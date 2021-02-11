
from pytube.contrib.playlist import Playlist, YouTube
from os import mkdir, path, startfile
import time
from console import color
from progress import on_complete, on_progress
from converter import file_size, seconds
from settings import Settings, settingsID


def openFile(file):
    startfile(file)


def download_settings():
    settings = Settings()

    class DownloadSettings:
        _Settings = settings
        audioOnly = settings.get_settings(settingsID.audio_only)
        download_dir = settings.get_settings(settingsID.download_directory)
        res = settings.get_settings(settingsID.video_quality)
        res = res if res != 'auto' else None
        new_folder_playlist = settings.get_settings(
            settingsID.new_folder_playlist)
        open_file = settings.get_settings(settingsID.open_file)

    return DownloadSettings()


def YTPlaylist(pl: Playlist):
    color.green('\n' + pl.title)
    color.green(f'{len(pl.video_urls)} videos found.\n')

    # get settings from settings.json
    settings = download_settings()
    settings.download_dir = path.join(settings.download_dir, pl.title)

    try:
        mkdir(settings.download_dir)
    except:
        pass
    video_count = 1
    for video in pl.videos:
        video.video_id
        video_start_time = time.time()
        stream = video.streams.filter(
            progressive=True, only_audio=settings.audioOnly).get_by_resolution(settings.res)
        color.yellow(f"\n\n[{video_count} of {len(pl.video_urls)}]")
        video.register_on_progress_callback(on_progress)
        video.register_on_complete_callback(on_complete)
        print("Title 🔥 : " + video.title)
        print("Size  📂 :  " + file_size(stream.filesize) + "\n")

        stream.download(
            output_path=settings.download_dir)

        print(
            f"\n Got  🕓 {seconds(time.time()-video_start_time)} to download.")
        video_count += 1
    if(settings.open_file):
        openFile(settings.download_dir)


def YTVideo(video: YouTube):
    settings = download_settings()
    stream = video.streams.filter(
        progressive=True, only_audio=settings.audioOnly).get_by_resolution(settings.res)
    print("Title 🔥 : " + video.title)
    print("Size  📂 :  " + file_size(stream.filesize) + "\n")
    video_start_time = time.time()
    video.register_on_progress_callback(on_progress)
    stream.download(
        output_path=settings.download_dir)

    print(
        f"\n Got  🕓 {seconds(time.time()-video_start_time)} to download.")
    if(settings.open_file):
        openFile(path.normpath(
            path.join(settings.download_dir, stream.default_filename)))
