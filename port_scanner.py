import socket


def port_scanner(ip, port1, port2):
	
	for port in range(port1, port2):
		#print (port)
		try:
		   s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		   s.settimeout(1)
		   result = s.connect((ip,port))
		   print (port, "PORT OPEN")
		except:
			s.close()

	
def main():
	user_input = input("Enter a desired IP to scan, followed by a port range. 127.0.0.1 1-500 \n\n")
	#print (user_input)

	ip_addr = user_input.split(" ")[0]
	#print (ip_addr)

	first_port = int(user_input.split(" ")[1].split("-")[0])
	#print (first_port)

	second_port = int(user_input.split(" ")[1].split("-")[1])
	#print (second_port)

	port_scanner(ip_addr, first_port, second_port)


main()