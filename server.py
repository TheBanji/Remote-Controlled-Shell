import socket

class Server():
	def __init__(self):
		self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		self.socket.bind(("0.0.0.0", 1234))	# IP of your machine
		self.socket.listen(5)
		self.client = 0
		self.address = 0

	def run(self):
		self.client, self.address = self.socket.accept()
		print("[+] New connection from {}".format(self.address))
		while(1):
			command = input(">>> ")
			if(command in ["stop", "close"]):
				self.client.close()
				self.socket.close()
				break
			self.client.send(command.encode())
			print(self.client.recv(20480).decode())
server = Server()
server.run()
print("[-] Connection closed with {}".format(server.address))