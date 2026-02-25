from scapy.all import *

packet = IP(dst='8.8.8.8')/TCP(dport=80)/"HELLo"
packet.show()

send(packet)

rply = sr1(IP(dst='8.8.8.8')/ICMP())

if rply:
    rply.show()

ans,unans  = sr(IP(dst='8.8.8.8')/TCP(dport=[80,443]),timeout =2)
ans.summary()



def pkt_check(packet):
    print(packet.summary())


sniff(count=5, prn=pkt_check)


########### checking the traffic in a pcap file    
from scapy.all import *

packet = rdpcap("traffic.pcap")

for pkt in packet:
    if pkt.haslayer(TCP) and pkt.haslayer(Raw):
       payload =  pkt[Raw].load.decode(errors='ignore')
       if payload.startswith("GET"):
           print(payload.split("/r/n/")[0])