import paramiko 

class Client: 

	def __init__(self, ip, username, password):
		self.ip = ip
		self.username = username
		self.password = password 
		self.connection = self.connect()


	def send_command(self, command):
		ssh  = self.connection
		stdin,stdout,stderr=ssh.exec_command(command)
		outlines=stdout.readlines()
		resp=''.join(outlines)
		print(resp)

	def connect(self): 
		ssh=paramiko.SSHClient()
		ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
		ssh.connect(self.ip,"22",self.username,self.password)
		return ssh


client_A = Client("127.0.0.1", "parallels", "kali123")
client_A.send_command("whoami")
client_B = Client("127.0.0.1", "parallels", "kali123")
client_B.send_command("ls -la")