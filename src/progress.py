
import time
import shutil
from sys import stdout
from pytube.query import StreamQuery
from converter import data_speed, file_size
from m3u import write_m3u_file

last_time = speed = None


def on_progress(stream, chunk, bytes_remaining):

    scale = 0.30
    ch = "█"
    filesize = stream.filesize
    _time = time.time()
    bytes_received = filesize - bytes_remaining
    global last_time, speed
    speed = None
    if(last_time != None):
        try:
            speed = data_speed(bytes_received / (_time - last_time))
        except:
            pass

    else:
        last_time = _time

    columns = shutil.get_terminal_size().columns
    max_width = int(columns * scale)
    filled = int(round(max_width * bytes_received / float(filesize)))
    remaining = max_width - filled
    progress_bar = ch * filled + " " * remaining
    percent = round(100.0 * bytes_received / float(filesize), 1)
    text = "\033[A{}\033[A".format(''.join(
        [' '] * columns)) + f"\n ↳ [{percent}%] |{progress_bar}|    {file_size(bytes_received)}  | {speed if speed != None else ''}"
    stdout.write(text)
    stdout.flush()


def on_complete(stream: StreamQuery, filepath: str):
    global last_time, speed
    last_time = speed = None
    filename = filepath.split("\\")[-1]
    #title = ".".join(filename.split(".")[:-1:])
    dir = "\\".join(filepath.split("\\")[:-1:])
    write_m3u_file(dir, filename)
