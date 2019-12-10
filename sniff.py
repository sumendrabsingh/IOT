#!/usr/bin/env python
from scapy.all import *
packets= sniff( iface="interfacename", count=number_of_packets_counts)
wrpcap('filename.pcap', packets)
print(len(packets))
