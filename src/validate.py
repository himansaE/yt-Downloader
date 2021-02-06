
from typing import Dict
from pytube import YouTube, Playlist
from urllib import error as url_err


def get_data(url):

    _info = {
        'data': None,
        'type': Url.Error,
        'error': True
    }

    try:
        yt = YouTube(url)
        _info = {
            'data': yt,
            'type': Url.Video,
            'error': False
        }
    except url_err.URLError:
        _info = {
            'data': None,
            'type': Url.Offline,
            'error': True
        }
    except:
        try:
            yt = Playlist(url)
            _info = {
                'data': yt,
                'type': Url.Playlist,
                'error': False
            }
        except:
            pass

    return _info


class Url:
    Playlist = "yt-playlist"
    Video = 'yt-video'
    Error = 'Url-error'
    Offline = 'Connect-problem'
