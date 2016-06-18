import sys
import time
import pprint
import telepot
import subprocess
import os
from guitarTrawl import *

curDir = os.path.dirname(os.path.realpath(__file__)) + '/'

def screenShot(uid):
	subprocess.call(["scrot", "ss.png"])
        with open(curDir + 'ss.png','r') as f:
                print "sending photo"
                response = bot.sendPhoto(uid,f)

def guitarTab(song,uid):
	print 'passing in ' + song
	chords = getChords(song)

	with open ('chords.txt','w') as f:
		for item in chords:
			f.write(item+"\n")
	with open ('chords.txt','r') as f:
		response = bot.sendDocument(uid,f)

	os.remove("chords.txt")

	
	

def handle(msg):
    pprint.pprint(msg)
    uid = msg['from']['id']
    text = msg['text'].lower().split()
    
    # Do your stuff here ...
    if text[0] == 'screenshot':
	print "taking ss"
	screenShot(uid)
    if text[0] == 'tab':
	if len(msg) > 1:
		song = ''
		for item in text[1:]:
			song = song + ' ' + item
		guitarTab(song,uid)
	else:
		print "please provide song"
# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
