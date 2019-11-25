#!/bin/bash
sudo apt-get update
sudo apt install python3-pip -y
pip3 install flask flask_restful requests pymongo
python3 /home/ubuntu/WebserverRedirect/redireciona.py
