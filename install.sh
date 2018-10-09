#!/bin/bash
sudo apt install python3-pip
python3 pip install numpy
wget https://github.com/sharkdp/hyperfine/releases/download/v1.3.0/hyperfine_1.3.0_amd64.deb
sudo dpkg -i hyperfine_1.3.0_amd64.deb
