#!/usr/bin/python
#The Script is inside Kali Linux Network Scanning Cookbok
import logging
logging.getLogger("scapy.runtime" ).setLevel(logging.ERROR)
from scapy.all import *

if len(sys.argv) != 2:
 print "Usage - ./arp_discovery.py [filename]"
 print "Example - ./arp_discovery.py iplist.txt"
 print "Example will perform an ARP scan of the IP addresses listed in iplist.txt"
 sys.exit()

filename = str(sys.argv[1])
file = open(filename, 'r' )

for addr in file:
 answer = sr1(ARP(pdst=addr.strip()),timeout=1,verbose=0)
 if answer == None:
  pass
 else:
  print addr.strip()
