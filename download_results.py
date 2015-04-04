import sys
import os
import multiprocessing

CONFIG_FILE = "config/ec2_hosts.txt"

for line in open(CONFIG_FILE):
    (ip, region) = line.split()
    os.system("mkdir results/%s" % region)
    os.system("scp -i keys/%s.pem  ec2-user@%s:~/ec2_ping-master/results/*.txt results/%s " % (region, ip, region))
    print "Downloaded",region
