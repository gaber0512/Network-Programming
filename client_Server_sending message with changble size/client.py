import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("client socket created")

# hostName=socket.gethostname()  
hostName="127.0.0.1"
port=7000

s.connect((hostName,port))

recieved=s.recv(1024).decode('utf-8')
print(f"server send [ {recieved} ] to you")

client_message = input("as client :) Enter your message: ")
s.send(client_message.encode('utf-8'))

# If the message length is greater than 1024 bytes, send it in chunks
if len(client_message) > 1024:
    message_size = 1024
    for i in range(0, len(client_message), message_size):
        s.send(client_message[i:i+message_size])#.encode('utf-8'))
else:
    s.send(client_message.encode('utf-8'))

s.close()