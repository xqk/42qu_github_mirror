PREFIX=$(cd "$(dirname "$0")"; pwd)
crontab -l > $PREFIX/crontab
hg commit -m"auto crontab -l backup"
