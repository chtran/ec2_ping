import datetime
import sys
import time
import random
import urllib

PING_URL_TMPL = 'http://ec2.%s.amazonaws.com/ping'
DATA_CENTERS_FILE = 'config/datacenters.txt'

urls = {}
files = {}
host_name = sys.argv[1]
count = 0

with open(DATA_CENTERS_FILE) as f:
    for line in f:
        name = line.strip()
        urls[name] = PING_URL_TMPL % name

while True:
    for name, url in urls.iteritems():
        try:
            start = time.time()
            nf = urllib.urlopen(url)
            end = time.time()
            nf.close()
            ping = 1000*(end-start) # in ms
            ts = str(datetime.datetime.now())
            #print ts, name, ping
            count +=1
            if count % 10 == 0:
                print ts, host_name, count
            with open("results/" + name + '.txt', 'a') as out:
                out.write(ts + '\t' + str(ping) + '\n')
        except IOError:
            pass
