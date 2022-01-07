import socket
import sys
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("This script was make by Phuc")
print("Credit all author is Phuc, Sans")
def connection():
	RHOSTS = str(input("[+] Please input your target: "))
	RPORT = int(input("[+] Please input your target port: "))
	print("[#] Warning! If you are using this for hacking you need to ask administrator or root or this might illegal because you are hacking without permonsions")
	print("[+] Exploiting...")
	try:
		s.connect((RHOSTS, RPORT))
		s.send(b'GET /HTTP/1.1\n\nHost: '+ RHOSTS.encode()+ b'\r\n\r\n')
		respone = s.recv(4096)
		print(respone)
		bytes_to_send = str(input("[+] Please send a bytes: "))
		s.send(b''+ bytes_to_send.encode())
		print(respone)
		s.close()
	except socket.error as msg:
		print("[-] Socket is error "+ msg)
		sys.exit(0)
	except socket.gaierror:
		print("[-] Unresolve host!!!")
		sys.exit(0)
	except KeyboardInterrupt:
		print("\n")
		print("[#] Interrupted exitting...")
		sys.exit(0)
def banner_grabber():
	s.settimeout(20)
	ip = str(input("[+] Please input your ip: "))
	port = int(input("[+] Please input your port: "))
	try:
		s.connect((ip, port))
		s.send(b'Whoareyou\r\n')
		banner = s.recv(100)
		s.close()
		print(banner)
		print("[+] My job is done!")
	except:
		print("[-] Can't connect")
		sys.exit(0)
try:
	print("Option 1: Send a simple http/1.1 post")
	print("Option 2:  Make a simple banner grabber")
	options = int(input("Please input your option: "))
	if options == 1:
		connection()
	elif options == 2:
		banner_grabber()
	else:
		print("Unknow option!!!")
		sys.exit(0)
except KeyboardInterrupt:
		print("\n")
		print("[#] Interrupted exitting...")
		sys.exit(0)
