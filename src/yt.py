from sys import argv

from pytube.__main__ import YouTube
from console import close, color, clear
from cursor import hide as cursor_hide
from download import YTPlaylist, YTVideo
from validate import Url, get_data


clear()

color.red("Youtube Video Downloader.")


if(len(argv) >= 2):
    url = argv[1]
else:

    url = input("\nYoutube url :\t")

YTData: YouTube = get_data(url)


if(YTData['type'] == Url.Offline):
    color.red("\n❗ Seems connection Error\n")
    close()
if(YTData['error'] == True):
    color.red("\n⨯ Somthing went wrong\n")
    close()

cursor_hide()

if(YTData['type'] == Url.Playlist):
    YTPlaylist(YTData['data'])
if(YTData['type'] == Url.Video):
    YTVideo(YTData['data'])

close()
