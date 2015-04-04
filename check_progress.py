import sys
import os

CONFIG_FILE = "config/ec2_hosts.txt"

if len(sys.argv) > 1:
    for line in open(CONFIG_FILE):
        (ip, region) = line.split()
        if region.strip() == sys.argv[1]:
            print region
            os.system("ssh ec2-user@%s -i keys/%s.pem 'wc -l ec2_ping-master/results/*.txt'" % (ip, region))
            print "--------------------"
            sys.exit(1)
else:
    for line in open(CONFIG_FILE):
        (ip, region) = line.split()
        print region
        os.system("ssh ec2-user@%s -i keys/%s.pem 'wc -l ec2_ping-master/results/*.txt'" % (ip, region))
        print "--------------------"
