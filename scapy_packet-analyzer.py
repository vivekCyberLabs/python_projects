# # from scapy.all import *

# # packet = IP(dst='8.8.8.8')/TCP(dport=80)/"HELLo"
# # packet.show()

# # send(packet)

# # # rply = sr1(IP(dst='8.8.8.8')/ICMP())

# # # if rply:
# # #     rply.show()

# # # ans,unans  = sr(IP(dst='8.8.8.8')/TCP(dport=[80,443]),timeout =2)
# # # ans.summary()



# # def pkt_check(packet):
# #     print(packet.summary())


# # sniff(count=5, prn=pkt_check)


# # class Parent:
# #     def __init__(self,name,age,edu):
# #         self.Peru = name
# #         self.vayas = age
# #         self.edu = edu
# #         print()
    
# #     def peridal(self):
# #         print(self.Peru)
# #         print(self.edu)        


# # class Child(Parent):
# #     def __init__(self, name, age, edu):
# #         self.puthiyaPeru = name
# #         self.PuthiyaVayas = age
# #         self.PuthiyaEdu = edu
# #         super().__init__(self.puthiyaPeru,self.PuthiyaVayas,self.PuthiyaEdu)


# # koch  = Child("vivek",23,"bsc")
# # koch.peridal()



# from scapy.all import *

# packet = rdpcap("traffic.pcap")

# for pkt in packet:
#     if pkt.haslayer(TCP) and pkt.haslayer(Raw):
#        payload =  pkt[Raw].load.decode(errors='ignore')
#        if payload.startswith("GET"):
#            print(payload.split("/r/n/")[0])