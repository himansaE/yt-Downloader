
def write_m3u_file(dir, filename):
    file = open(dir + "\\playlist.m3u", "a",encoding="utf-8")
    file_r = open(dir + "\\playlist.m3u", "r",encoding="utf-8")
    lines = file_r.readlines()
    for line in lines:
        if(filename in line):
            return file_r.close()
    file.write(f'{filename}\n')
    file_r.close()
    file.close()
