
def write_m3u_file(dir, filename):
    file = open(dir + "\\playlist.m3u", "a")
    file_r = open(dir + "\\playlist.m3u", "r")
    lines = file_r.readlines()
    for line in lines:
        if(filename in line):
            return file_r.close()
    file.write(f'{filename}\n')
    file_r.close()
    file.close()
