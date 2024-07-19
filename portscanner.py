from IPy import IP
import socket

def check_ip(ip):
    try:
        IP(ip) #checks whether ip is given ... if yes it retuens True ..
        return(ip) # otherwise it returns value error
    except ValueError:
        return socket.gethostbyname(ip) #resolve hostname to ip address

def get_banner(s):   #banner grabbing ie, gethering info abt service running on that port
    return s.recv(1024)


def scan_port(ipaddr,port):
    try:
        sock=socket.socket()
        sock.settimeout(0.5) #accuracy will depend upon this line ,,, remove it to attain higher accuracy
        sock.connect((ipaddr,port))
        try:
            banner=get_banner(sock)
            print("[+] Open Port "+ str(port) +" : ",+str(banner.decode()))
        except:
            print("[+] Open Port "+str(port))
    except:
        pass

def scan(target): # this is to be called when portscanner is used as an external module
    converted_ip=check_ip(target)
    for port in range(1,1000):
        scan_port(converted_ip,port)


if __name__=="__main__":
    targets=input("[+] Enter target/s to scan (seperate targets with space) ")
    for ipaddr in targets.split(" "):
        converted_ip=check_ip(ipaddr) #resolve domain names to ip addresses
        print("[ 0 - Scanning ] "+str(ipaddr))
        for port in range(1,85):
            scan_port(converted_ip,port)
    