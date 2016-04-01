#from __future__ import unicode_literals
from twython import TwythonStreamer
import time
import pygame
import os
from Adafruit_Thermal import *

os.environ['IT'] = 'EST'
dataform = time.strftime('Hai avuto questa idea alle %H:%M del %d/%m/%Y')

printer = Adafruit_Thermal("/dev/ttyAMA0", 19200, timeout=5)
pygame.mixer.init()
s = pygame.mixer.Sound("sirena.wav")
# Twitter application authentication
APP_KEY = 'eg71IuNpmhXPbhRfO2SAEEyXM'
APP_SECRET = 't3zgunquqb5A6LeixJ91CrYCm2NyulnP5zDr0USifAuuaqPQta'
OAUTH_TOKEN = '711665111136649216-lRp7SRCukD8kukXkDPxrx4KWZ2Dw7w3'
OAUTH_TOKEN_SECRET = 'kpBug0BoSoZt6B0w0VUXBCvwL94HbVf21yqYKO6Bsx0Rh'


class MyStreamer(TwythonStreamer):
    def on_success(self, data):
        if 'text' in data:
            print data['text'].encode('utf-8')
	    #datanf = data['created_at'].encode('utf-8')
	    #print data['created_at'].encode('utf-8')
	    #dataf = datanf.strftime('%d, %b %Y')
	    #print datanf
            os.system ('aplay /home/pi/Desktop/ominogiallo/sirena.wav')
	    printer.inverseOn()
	    printer.setSize('s')
	    printer.println(' ')
	    printer.println(' ')
	    printer.println(data['text'].encode('utf-8'))
	    #printer.println(data['created_at'])
	    printer.println(dataform)
#	    printer.println(' ')
#	    printer.println(' ')	
	    printer.feed(3)
	    printer.inverseOff()
	    printer.sleep()      # Tell printer to sleep
	    printer.wake()       # Call wake() before printing again, even if reset
	    printer.setDefault()
        # Want to disconnect after the first result?
        # self.disconnect()

    def on_error(self, status_code, data):
        print status_code, data

# Requires Authentication as of Twitter API v1.1
stream = MyStreamer(APP_KEY, APP_SECRET,
                    OAUTH_TOKEN, OAUTH_TOKEN_SECRET)

stream.statuses.filter(follow='711665111136649216')
#stream.statuses.filter(track='#mixxxxxy')
# stream.user()
# Read the authenticated users home timeline
# (what they see on Twitter) in real-time
# stream.site(follow='twitter')
