import socket

s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
print("server socket created")
hostName="127.0.0.1" 
# hostName=socket.gethostname() 
port=7000

s.bind((hostName,port))

s.listen(5)
print("server waiting for incomming requests ....")
while True:
    session,address=s.accept()
    print(f"Get connection from {address} and his session with server is {session}")
    session.send("welcome from server".encode('utf-8'))
    all_message = ""  # Initialize an empty byte string to store the all message
    while True:
        chunk = session.recv(1024).decode('utf-8')  # Receive data in chunks of 1024 bytes
        if not chunk:
            break  # No more data to receive, break out of the loop
        all_message += chunk
    message = all_message #.decode('utf-8')
    print(f"i recieve [{message}] from connected client")   
    session.close() # session  closed