import scapy.all as scapy
import optparse as opt

def scan_network(ip_address):
    arp_request_packet = scapy.ARP(pdst=ip_address)
    broadcast_packet = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined_packet = broadcast_packet/arp_request_packet
    (answered_list,unanswered_list) = scapy.srp(combined_packet,timeout=1)
    return answered_list

def get_ip_address():
    parse_object = opt.OptionParser()
    parse_object.add_option("-r","--range",dest="ip_address",help="scan a given range. 192.168.6.0/24,/16,/8")
    (user_input,arguments) = parse_object.parse_args()
    if not user_input.ip_address:
        print("Enter ip address")
    return user_input.ip_address

scan_network(get_ip_address()).summary()