cd ~/project/stock1
sudo /etc/init.d/tor restart
sudo netstat -ntlp
. ./venv/bin/activate
if [ "$1" == "" ]; then
    echo "Default Process is 8"
    python get_kospistock.py  8
    python get_kosdaqstock.py 8
    python get_mystock.py     8
    python get_todaysstock.py 8
else
    echo "Working Process is $1"
    python get_kospistock.py  $1
    python get_kosdaqstock.py $1
    python get_mystock.py     $1
    python get_todaysstock.py $1
fi
