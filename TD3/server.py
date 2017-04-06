import socket
import time

# create a socket object
serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# get local machine name
host = socket.gethostname()

port = 6666

# bind to the port
serversocket.bind((host, port))

# queue up to 5 requests
serversocket.listen(5)

while True:
    # establish a connection
    clientsocket,addr = serversocket.accept()
    print "Client says: " + s.recv(1024)

    data = raw_input("Enter..... ")  
    s.sendto(data,(HOST, PORT))

    if data=="bye" or s.recv(1024)=="bye":
           print "Exiting.................."
           time.sleep(1)
           break

    print("Connection de client avec IP %s" % str(addr))
    currentTime = time.ctime(time.time()) + "\r\n"
    clientsocket.send(currentTime.encode('ascii'))
    clientsocket.close()
