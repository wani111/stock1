sudo /etc/init.d/tor restart
sudo netstat -ntlp
. ./venv/bin/activate
python get_kospistock.py
python get_kosdaqstock.py
