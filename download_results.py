import sys
import os
import multiprocessing

CONFIG_FILE = "config/ec2_hosts.txt"

directory = sys.argv[1]

for line in open(CONFIG_FILE):
    (ip, region) = line.split()
    os.system("mkdir %s/%s" % (directory, region))
    os.system("scp -i keys/%s.pem  ec2-user@%s:~/ec2_ping-master/results/*.txt %s/%s " % (region, ip, directory, region))
    print "Downloaded",region
