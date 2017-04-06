import socket

# create a socket object
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 

# get local machine name
host = socket.gethostname()

port = 6666

# connection to hostname on the port.
s.connect((host, port))

# Receive no more than 1024 bytes
tm = s.recv(1024)

s.close()

print("The time got from the server is %s" % tm.decode('ascii'))
s.bind((host,port))
while True:

      data = raw_input("Enter..... ")
      s.sendto(data,(host,port))

      print "Server says: " + s.recv(1024)

      if data=="bye" or s.recv(1024)=="bye":
           print "Exiting..........."
           time.sleep(1)
           break
