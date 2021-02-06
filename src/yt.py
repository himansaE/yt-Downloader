from sys import argv, exit
from console import color, clear
from cursor import hide as cursor_hide
from download import YTPlaylist, YTVideo
from validate import Url, get_data


clear()

color.red("Youtube Video Downloader.")


if(len(argv) >= 2):
    url = argv[1]
else:
    url = input("\nYoutube url :\t")

YTData = get_data(url)

if(YTData['type'] == Url.Offline):
    color.red("\n❗ seems connection Error\n")
    exit()
if(YTData['error'] == True):
    color.red("\n⨯ somthing went wrong\n")
    exit()

cursor_hide()

if(YTData['type'] == Url.Playlist):
    YTPlaylist(YTData['data'])
if(YTData['type'] == Url.Video):
    YTVideo(YTData['data'])
