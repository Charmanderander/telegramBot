import sys
import time
import pprint
import telepot
import subprocess

def handle(msg):
    pprint.pprint(msg)
    # Do your stuff here ...
    if msg == 'screenshot':
	print "taking ss"
	subprocess.call(["scrot"," ss.png"])
	f = open('ss.png',rb)
	print "sending photo"
	response = bot.sendPhoto(158951306,f)
	f.close()

# Getting the token from command-line is better than embedding it in code,
# because tokens are supposed to be kept secret.
TOKEN = sys.argv[1]

bot = telepot.Bot(TOKEN)
bot.message_loop(handle)
print ('Listening ...')

# Keep the program running.
while 1:
    time.sleep(10)
