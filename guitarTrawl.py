import urllib2
from HTMLParser import HTMLParser

songLinks = []
getData = 0
chords = []

# create a subclass and override the handler methods
class HTMLParserForLinks(HTMLParser):
    def handle_starttag(self, tag, attrs):
	attrsArray = []
	if tag == 'a':	
        	for attr in attrs:
			attrsArray.append(attr[1])
            		#print "     attr:", attr
			if 'song result-link' in attrsArray:
				songLinks.append(attrsArray[0])			
				attrsArray = []

# create a subclass and override the handler methods
class HTMLParserForSongs(HTMLParser):
    def handle_starttag(self, tag, attrs):
	global getData
	if tag == 'pre':
		for attr in attrs:
			if attr[1] == 'js-tab-content':
				getData = 1
    def handle_data(self, data):
	global getData
	if getData:
		chords.append(data)                        
    def handle_endtag(self, tag):
	global getData
        if tag == 'pre':
		getData = 0
		

def getPageContent(site):
	header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}

	req = urllib2.Request(site, headers=header)
	
	try:
	        page = urllib2.urlopen(req)
	except urllib2.HTTPError, e:
        	print e.fp.read()

	content = page.read()
	
	return content



def getChords(song):
	global songLinks
	global chords
	print song
	linkGetter = HTMLParserForLinks()
	songSelector = HTMLParserForSongs()


	site = 'https://www.ultimate-guitar.com/search.php?search_type=title&order=&value='+song
	content = getPageContent(site)

	linkGetter.feed(content)
	

	for songLink in songLinks:
		content = getPageContent(songLink)
		songSelector.feed(content)
		print songLink
		break
	songLinks = []

	tempChords = chords
	chords = []
	return tempChords



