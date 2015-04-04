import sys
import os
import multiprocessing

CONFIG_FILE = "config/ec2_hosts.txt"

for line in open(CONFIG_FILE):
    (ip, region) = line.split()
    os.system("ssh ec2-user@%s -i keys/%s.pem 'killall python'" % (ip, region))

