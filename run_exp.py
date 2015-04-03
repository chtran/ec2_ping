import sys
import os
import multiprocessing

CONFIG_FILE = "config/ec2_hosts.txt"

def get_cmd(mode, ip, region):
    if mode == "restart":
        return "ssh ec2-user@%s -i keys/%s.pem 'rm -rf *; wget https://github.com/chtran/ec2_ping/archive/master.zip; unzip master.zip; cd ec2_ping-master/; python latency.py'" % (ip, region)
    elif mode is "continue":
        return "ssh ec2-user@%s -i keys/%s.pem 'cd ec2_ping-master/; python latency.py'" % (ip, region)

def worker(ip, region):
    if len(sys.argv) > 1:
        os.system(get_cmd(sys.argv[1], ip, region))
    else:
        os.system(get_cmd("continue", ip, region))

for line in open(CONFIG_FILE):
    (ip, region) = line.split()
    p = multiprocessing.Process(target=worker, args=(ip, region))
    p.start()
