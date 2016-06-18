import sys
import time
import pprint
import telepot
import subprocess
import os
from guitarTrawl import *
from allowedUsers import *

curDir = os.path.dirname(os.path.realpath(__file__)) + '/'



def screenShot(uid):
	if isSuperUser(uid):
		print "is super user!"
		bot.sendMessage(uid,"Taking a screenshot, hold on...")
		subprocess.call(["scrot", "ss.png"])
        	with open(curDir + 'ss.png','r') as f:
                	print "sending photo"
                	bot.sendPhoto(uid,f)
	else:
		print "not super user"
		bot.sendMessage(uid,"You are not a superuser!")

def guitarTab(song,uid):
	bot.sendMessage(uid,"Finding guitar chords. Hold on...")
	chords, link = getChords(song)

	with open ('chords.txt','w') as f:
		for item in chords:
			f.write(item+"\n")
	with open ('chords.txt','r') as f:
		bot.sendMessage(uid,"We found a link: "+ link + ".\nHere are the chords: ")
		bot.sendDocument(uid,f)

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
