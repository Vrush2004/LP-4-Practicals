# A person on a nearby road is trying to enter into a WiFi network by trying to crack the Password to use the IP Printer resource; 
# write a program detect such attempt and prohibit the access. Develop the necessary scenario by Using an IEEE 802.11, configure a 
# Wi-Fi adapter and Access Point

from scapy.all import *
import time

# Set your Wi-Fi credentials
AUTHORIZED_MACS = ["5C-BA-EF-5F-B4-93"] 
SUSPICIOUS_MACS = []  

def packet_handler(packet):
    """Handles the packets captured on the network."""
    if packet.haslayer(Dot11):
        mac = packet.addr2 
        if mac not in AUTHORIZED_MACS and mac not in SUSPICIOUS_MACS:
            print(f"Unauthorized access attempt detected from MAC: {mac}")
            SUSPICIOUS_MACS.append(mac)
            log_access_attempt(mac)

def log_access_attempt(mac):
    """Log unauthorized access attempts."""
    with open("access_log.txt", "a") as log_file:
        log_file.write(f"Unauthorized access attempt from MAC: {mac} at {time.ctime()}\n")
    print(f"Logged unauthorized access attempt from MAC: {mac}")

def main():
    """Main function to run the packet sniffer."""
    print("Starting Wi-Fi monitoring...")
    sniff(iface="Wi-Fi", prn=packet_handler) 

if __name__ == "__main__":
    main()