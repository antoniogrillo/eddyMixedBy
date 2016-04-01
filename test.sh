#!/bin/sh

python -m SimpleHTTPServer 8000 &
chromium-browser http://localhost:8000/face6.html &
python3 /home/pi/Desktop/ominogiallo/bindm.py &
