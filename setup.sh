#!/bin/bash
wget https://bootstrap.pypa.io/get-pip.py
python3 get-pip.py
rm get-pip.py
pip3 install -r requirement.txt