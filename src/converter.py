
time_units = [{"u": 'sec', "v": 60},
              {"u": 'min', "v": 60},
              {"u": "hr", "v": 24}]
file_units = ['B', 'KiB', 'MiB', 'GiB']
data_speed_units = ['Byte/s', 'KB/s', 'MB/s']


def file_size(num):
    for unit in file_units:
        if abs(num) < 1024.0:
            return "%.1f%s" % (num, unit)
        num /= 1024.0

    return "%.1f%s" % (num, 'TiB')


def seconds(s):

    for unit in time_units:
        if s < unit["v"]:
            return "%.0f%s" % ((s), unit["u"])
        s /= unit["v"]
    return "%.0f%s" % (s, "day")


def data_speed(num):
    for unit in data_speed_units:
        if abs(num) < 1024.0:
            return "%.1f%s" % (num, unit)
        num /= 1024.0

    return "%.1f%s" % (num, 'GB/s')
