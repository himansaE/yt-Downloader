$scriptpath = $MyInvocation.MyCommand.Path
$dir = Split-Path $scriptpath
python $dir/src/yt.py