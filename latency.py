import time
import random
import urllib

PING_URL_TMPL = 'http://ec2.%s.amazonaws.com/ping'
DATA_CENTERS_FILE = 'datacenters.txt'

urls = {}
files = {}

with open(DATA_CENTERS_FILE) as f:
    for line in f:
        name = line.strip()
        urls[name] = PING_URL_TMPL % name

while True:
    for name, url in urls.iteritems():
        start = time.time()
        nf = urllib.urlopen(url)
        end = time.time()
        nf.close()
        ping = 1000*(end-start) # in ms
        print name, ping
        with open("results/" + name + '.txt', 'a') as out:
            out.write(str(ping) + '\n')
