import sys
CONFIG_FILE = "config/ec2_hosts.txt"

def get_cmd(mode, ip, region):
    if mode == "restart":
        return "ssh ec2-user@%s -i keys/%s.pem 'rm -rf *; wget https://github.com/chtran/ec2_ping/archive/master.zip; unzip master.zip; cd ec2_ping-master/; python latency.py'" % (ip, region)
    elif mode is "continue":
        return "ssh ec2-user@%s -i keys/%s.pem 'cd ec2_ping-master/; python latency.py'" % (ip, region)

for line in open(CONFIG_FILE):
    (ip, region) = line.split()
    if len(sys.argv) > 1:
        print get_cmd(sys.argv[1], ip, region)
    else:
        print get_cmd("continue", ip, region)
