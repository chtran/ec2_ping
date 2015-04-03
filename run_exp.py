CONFIG_FILE = "ec2_hosts.txt"

for line in open(CONFIG_FILE):
    (ip, region) = line.split()
    print "ssh ec2-user@%s -i keys/%s.pem 'wget https://github.com/chtran/ec2_ping/archive/master.zip; unzip master.zip; cd ec2_ping-master/; python latency.py'" % (ip, region)
