import os
import sys
import time
import socket

from socket import *
from _datetime import time
from header import head
from optparse import OptionParser

Parser = OptionParser()
Parser.add_option("-i", "--ip_adres", dest="ip", help="\tip adresi degeri")
(user_input, arguments) = Parser.parse_args()

ip_addr = user_input.ip

try:
    IP_Scanner = gethostbyname(ip_addr)
except KeyboardInterrupt:
    print("\npressed 'CTRL + C'")
    sys.exit()

except Exception as E:
    print(E + " error")
    sys.exit()

for ip in range(1, 65535):
    try:
        connections = socket(AF_INET, SOCK_STREAM)
        control = connections.connect_ex((IP_Scanner, ip))
        if control == 0:
            if ip == 7:
                print(f"PORT OPEN | {ip} | Echo")
            elif ip == 19:
                print(f"PORT OPEN | {ip} | Chargen")
            elif ip == 20 or ip == 21:
                print(f"PORT OPEN | {ip} | FTP")
            elif ip == 22:
                print(f"PORT OPEN | {ip} | SSH")
            elif ip == 23:
                print(f"PORT OPEN | {ip} | telnet")
            elif ip == 25:
                print(f"PORT OPEN | {ip} | SMTP")
            elif ip == 42:
                print(f"PORT OPEN | {ip} | WINS replication")
            elif ip == 43:
                print(f"PORT OPEN | {ip} | WHOIS")
            elif ip == 49:
                print(f"PORT OPEN | {ip} | TACACS")
            elif ip == 53:
                print(f"PORT OPEN | {ip} | DNS")
            elif ip == 67 or ip == 68:
                print(f"PORT OPEN | {ip} | DHCP")
            elif ip == 69:
                print(f"PORT OPEN | {ip} | TFTP")
            elif ip == 70:
                print(f"PORT OPEN | {ip} | Gopher")
            elif ip == 79:
                print(f"PORT OPEN | {ip} | Finger")
            elif ip == 80:
                print(f"PORT OPEN | {ip} | HTTP")
            elif ip == 88:
                print(f"PORT OPEN | {ip} | Kerberos")
            elif ip == 102:
                print(f"PORT OPEN | {ip} | MS Exchange")
            elif ip == 110:
                print(f"PORT OPEN | {ip} | POP3")
            elif ip == 113:
                print(f"PORT OPEN | {ip} | Ident")
            elif ip == 119:
                print(f"PORT OPEN | {ip} | NNTP (Usenet)")
            elif ip == 123:
                print(f"PORT OPEN | {ip} | NTP")
            elif ip == 135:
                print(f"PORT OPEN | {ip} | Microsoft RPC")
            elif ip == 137 or ip == 138 or ip == 139:
                print(f"PORT OPEN | {ip} | NetBIOS")
            elif ip == 143:
                print(f"PORT OPEN | {ip} | IMAP")
            elif ip == 161 or ip == 162:
                print(f"PORT OPEN | {ip} | SNMP")
            elif ip == 177:
                print(f"PORT OPEN | {ip} | XDMCP")
            elif ip == 179:
                print(f"PORT OPEN | {ip} | BGP")
            elif ip == 194:
                print(f"PORT OPEN | {ip} | IRP")
            elif ip == 201:
                print(f"PORT OPEN | {ip} | Apple Talk")
            elif ip == 264:
                print(f"PORT OPEN | {ip} | BGMP")
            elif ip == 318:
                print(f"PORT OPEN | {ip} | TSP")
            elif ip == 381 or ip == 382 or ip == 383:
                print(f"PORT OPEN | {ip} | HP openview")
            elif ip == 389:
                print(f"PORT OPEN | {ip} | LDAP")
            elif ip == 411 or ip == 412:
                print(f"PORT OPEN | {ip} | Direct Connect")
            elif ip == 443:
                print(f"PORT OPEN | {ip} | HTTPS")
            elif ip == 445:
                print(f"PORT OPEN | {ip} | Microsoft DS")
            elif ip == 464:
                print(f"PORT OPEN | {ip} | Kerberos")
            elif ip == 465:
                print(f"PORT OPEN | {ip} | SMTP over SSL")
            elif ip == 497:
                print(f"PORT OPEN | {ip} | Retrospect")
            elif ip == 500:
                print(f"PORT OPEN | {ip} | ISAKMP")
            elif ip == 512:
                print(f"PORT OPEN | {ip} | rexec")
            elif ip == 513:
                print(f"PORT OPEN | {ip} | rlogin")
            elif ip == 514:
                print(f"PORT OPEN | {ip} | syslog")
            elif ip == 515:
                print(f"PORT OPEN | {ip} | LPD/LPR")
            elif ip == 520:
                print(f"PORT OPEN | {ip} | RIP")
            elif ip == 521:
                print(f"PORT OPEN | {ip} | RIPng (IPv6)")
            elif ip == 540:
                print(f"PORT OPEN | {ip} | UUCP")
            elif ip == 546 or ip == 547:
                print(f"PORT OPEN | {ip} | DHCPv6")
            elif ip == 554:
                print(f"PORT OPEN | {ip} | RTSP")
            elif ip == 560:
                print(f"PORT OPEN | {ip} | rmonitor")
            elif ip == 563:
                print(f"PORT OPEN | {ip} | NNTP over SSL")
            elif ip == 587:
                print(f"PORT OPEN | {ip} | SMTP")
            elif ip == 591:
                print(f"PORT OPEN | {ip} | FileMaker")
            elif ip == 593:
                print(f"PORT OPEN | {ip} | Microsoft DCOM")
            elif ip == 631:
                print(f"PORT OPEN | {ip} | Internet Printing")
            elif ip == 636:
                print(f"PORT OPEN | {ip} | LDAP over SSL")
            elif ip == 639:
                print(f"PORT OPEN | {ip} | MSDP (FIM)")
            elif ip == 646:
                print(f"PORT OPEN | {ip} | LDP (MPLS)")
            elif ip == 691:
                print(f"PORT OPEN | {ip} | MS Exchange")
            elif ip == 860:
                print(f"PORT OPEN | {ip} | ISCSI")
            elif ip == 873:
                print(f"PORT OPEN | {ip} | rsync")
            elif ip == 902:
                print(f"PORT OPEN | {ip} | VMware Server")
            elif ip == 989 or ip == 990:
                print(f"PORT OPEN | {ip} | FTP over SSL")
            elif ip == 1025:
                print(f"PORT OPEN | {ip} | Microsoft RPC")
            elif ip == 1026 or ip == 1027 or ip == 1028 or ip == 1029:
                print(f"PORT OPEN | {ip} | Windows Messenger")
            elif ip == 1080:
                print(f"PORT OPEN | {ip} | SOCKS Proxy // My Doom")
            elif ip == 1194:
                print(f"PORT OPEN | {ip} | Openvpn")
            elif ip == 1214:
                print(f"PORT OPEN | {ip} | Kazaa")
            elif ip == 1241:
                print(f"PORT OPEN | {ip} | Nessus")
            elif ip == 1337:
                print(f"PORT OPEN | {ip} | WASTE")
            elif ip == 1433 or ip == 1434:
                print(f"PORT OPEN | {ip} | Microsoft SQL")
            elif ip == 1512:
                print(f"PORT OPEN | {ip} | WINS")
            elif ip == 1589:
                print(f"PORT OPEN | {ip} | Cisco VQP")
            elif ip == 1701:
                print(f"PORT OPEN | {ip} | L2TP")
            elif ip == 1723:
                print(f"PORT OPEN | {ip} | MS PPTP")
            elif ip == 1725:
                print(f"PORT OPEN | {ip} | Steam")
            elif ip == 1741:
                print(f"PORT OPEN | {ip} | Cisco Works 2000")
            elif ip == 1755:
                print(f"PORT OPEN | {ip} | MS Media Server")
            elif ip == 1812 or ip == 1813:
                print(f"PORT OPEN | {ip} | RADIUS")
            elif ip == 1985:
                print(f"PORT OPEN | {ip} | Cisco HSRP")
            elif ip == 2000:
                print(f"PORT OPEN | {ip} | Cisco SCCP")
            elif ip == 2002:
                print(f"PORT OPEN | {ip} | Cisco ACS")
            elif ip == 2049:
                print(f"PORT OPEN | {ip} | NFS")
            elif ip == 2082 or ip == 2083:
                print(f"PORT OPEN | {ip} | c panel")
            elif ip == 2100:
                print(f"PORT OPEN | {ip} | Oracle XDB")
            elif ip == 2222:
                print(f"PORT OPEN | {ip} | Direct Admin")
            elif ip == 2302:
                print(f"PORT OPEN | {ip} | Halo")
            elif ip == 2483 or ip == 2484:
                print(f"PORT OPEN | {ip} | Oracle DB")
            elif ip == 2745:
                print(f"PORT OPEN | {ip} | Bagle H")
            elif ip == 2967:
                print(f"PORT OPEN | {ip} | Symantec AV")
            elif ip == 3050:
                print(f"PORT OPEN | {ip} | Interbase DB")
            elif ip == 3074:
                print(f"PORT OPEN | {ip} | XBOX live")
            elif ip == 3124:
                print(f"PORT OPEN | {ip} | HTTP proxy")
            elif ip == 3222:
                print(f"PORT OPEN | {ip} | GLBP")
            elif ip == 3260:
                print(f"PORT OPEN | {ip} | iSCSI Target")
            elif ip == 3306:
                print(f"PORT OPEN | {ip} | MySQL")
            elif ip == 3389:
                print(f"PORT OPEN | {ip} | Terminal Server // RDP")
            elif ip == 3689:
                print(f"PORT OPEN | {ip} | İTunes")
            elif ip == 3690:
                print(f"PORT OPEN | {ip} | Subversion")
            elif ip == 3784 or ip == 3785:
                print(f"PORT OPEN | {ip} | Ventrillo")
            elif ip == 4444:
                print(f"PORT OPEN | {ip} | Blaster")
            elif ip == 4664:
                print(f"PORT OPEN | {ip} | Google Desktop")
            elif ip == 4672:
                print(f"PORT OPEN | {ip} | e Mule")
            elif ip == 4899:
                print(f"PORT OPEN | {ip} | Radmin")
            elif ip == 5000:
                print(f"PORT OPEN | {ip} | UPnP")
            elif ip == 5001:
                print(f"PORT OPEN | {ip} | Slingbox")
            elif ip == 5004 or ip == 5005:
                print(f"PORT OPEN | {ip} | RTP")
            elif ip == 5060 or ip == 5061:
                print(f"PORT OPEN | {ip} | SIP")
            elif ip == 5432:
                print(f"PORT OPEN | {ip} | Postgre SQL")
            elif ip == 5500:
                print(f"PORT OPEN | {ip} | VNC server")
            elif ip == 5554:
                print(f"PORT OPEN | {ip} | sasser")
            elif ip == 5631 or ip == 5632:
                print(f"PORT OPEN | {ip} | PC Any Where")
            elif ip == 5800:
                print(f"PORT OPEN | {ip} | VNC over HTTP")
            elif ip == 6000 or ip == 6001:
                print(f"PORT OPEN | {ip} | X11")
            elif ip == 8000:
                print(f"PORT OPEN | {ip} | Internet Radio")
            elif ip == 8080:
                print(f"PORT OPEN | {ip} | HTTP Proxy")
            else:
                print(f"PORT OPEN | {ip} | Unknown")

    except KeyboardInterrupt:
        print("\npressed 'CTRL + C'")
        sys.exit()

    except Exception as E:
        print(E + " error")
        sys.exit()

print("\ntime : ", time.time())
sys.exit()
