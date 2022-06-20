#/bin/sh

# Prerequisites
apt install firefox
wget https://github.com/mozilla/geckodriver/releases/download/v0.31.0/geckodriver-v0.31.0-linux64.tar.gz
tar -xvzf geckodriver*
chmod +x geckodriver
mv geckodriver /usr/local/bin/
export PATH=$PATH:/usr/local/bin/geckodriver

# Python packages
pip install selenium
pip install tkinter
pip install selenium-requests