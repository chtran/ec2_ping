import sys

CONFIG_FILE = "config/ec2_hosts.txt"
hosts = {}

for line in open(CONFIG_FILE):
    (ip, region) = line.split()
    hosts[region] = ip

to_login = sys.argv[1]
print "ssh ec2-user@%s -i keys/%s.pem" % (hosts[to_login], to_login)

