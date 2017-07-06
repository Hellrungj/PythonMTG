#
# https://pymotw.com/2/socket/tcp.html
# https://docs.python.org/3/howto/sockets.html
# Messaging Server v0.1.0
import socket
import sys

# CONTRACT
# start_server : string number -> socket
# Takes a hostname and port number, and returns a socket
# that is ready to listen for requests
def start_server (host, port):
  server_address = (host, port)
  sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  sock.bind(server_address)
  sock.listen(1)
  return sock

# CONTRACT
# get_message : socket -> string
# Takes a socket and loops until it receives a complete message
# from a client. Returns the string we were sent.
# No error handling whatsoever.
def get_message (sock):
  chars = []
  connection, client_address = sock.accept()
  print ("Connection from [{0}]".format(client_address))
  try:
    while True:
      char = connection.recv(1)
      if char == b'\0':
        break
      if char == b'':
        break
      else:
	  # print("Appending {0}".format(char))
        chars.append(char.decode("utf-8") )
  finally:
    return (''.join(chars), connection)

# CONTRACT
# socket -> boolean
# Shuts down the socket we're listening on.
def stop_server (sock):
  return sock.close()

# DATA STRUCTURES
# The structures for your server should be defined and documented here.

# SERVER IMPLEMENTATION
# The implementation of your server should go here.
UD = {} #UserData  {<STR Username>:[<STR Password>,<BOOL LoginStatus>]}
MBX = {} #Mailbox  {<STR User>:<IMQ>}
IMQ = [] #Messages [<STR Message>]

def is_login(UD, username):
  user = UD[username]
  loginstatus = user[1]
  return loginstatus
  
# CONTRACT
def handle_message (msg):
  if "LOGIN" in msg:
    # Username
    username = msg.split(" ")[1]
    # Password
    password = msg.split(" ")[2]
    # IF the user is register status equals None?
    if UD.get(username) == None:
      return("ERROR","User does not exsited")
    # ELIF the user is equal to the givin password
    elif UD[username][1] != password:
      return("ERROR","Password invald")
    # ELSE login 
    else:
      login_status = is_login(UD[username], username)
      login_status = True
      return("LOGIN", "{0} Login".format(username))
	  
  elif "DUMP" in msg:
    # Get the username
    #username = msg.split(" ")[1]
    # Checking user status
    #if is_login(UD[username]) == True:
    print(MBX)
    print(IMQ)
    return ("OK", "Dumped.")
    #else:
    #  return ("Error", "Current user is not login")
	  
  elif "REGISTER" in msg:
    # Get the username
    username = msg.split(" ")[1]
    # Get the password
    password = msg.split(" ")[2]
    # Create an empty list of messages
    UD[username] = [password,False]
    MBX[username] = []
    return ("OK", "Registered. {0}/n {1}/n {2}".format(UD,MBX,IMQ))
  
  elif "MESSAGE" in msg:
    # Get the username
    username = msg.split(" ")[1]
    print("Username: {0}".format(username))
    if is_login(UD[username], username) == True:
      # Get the content; slice everything after
      # the word MESSAGE
      content = msg.split(" ")[2:]
      # Put the content back together, and put 
      # it on the incoming message queue.
      IMQ.insert(0, " ".join(content))
      return ("OK", "Sent message.")
    else:
      return ("Error", "Current user is not login")
  
  elif "STORE" in msg:
    # Get the username
    #username = msg.split(" ")[1]
    #if is_login(UD[username]) == True:
    queued = IMQ.pop()
    print("Message in queue:\n---\n{0}\n---\n".format(queued))
    MBX[username].insert(0, queued)
    return ("OK", "Stored message.")
    #else:
    #  return ("Error", "Current user is not login")
  
  elif "COUNT" in msg:
    # Get the username
    username = msg.split(" ")[1]
    if is_login(UD[username], username) == True:
      return ("SEND", "COUNTED {0}".format(len(MBX[username])))
    else:
      return ("Error", "Current user is not login")
  elif "DELMSG" in msg:
    # Get the username
    username = msg.split(" ")[1]
    if is_login(UD[username]) == True:
      MBX[username].pop(0)
      return ("OK", "Message deleted.")
    else:
      return ("Error", "Current user is not login")
	  
  elif "GETMSG" in msg:
    # Get the username
    username = msg.split(" ")[1]
    if is_login(UD[username], username) == True:
      first = MBX[username][0]
      print ("First message:\n---\n{0}\n---\n".format(first) )
      return ("SEND", first)
    else:
      return ("Error", "Current user is not login")
  else:
    print("NO HANDLER FOR CLIENT MESSAGE: [{0}]".format(msg))
    return ("KO", "No handler found for client message.")

if __name__ == "__main__":
  # Check if the user provided all of the 
  # arguments. The script name counts
  # as one of the elements, so we need at 
  # least three, not fewer.
  """
  if len(sys.argv) < 3:
    print ("Usage: ")
    print (" python server.py <host> <port>")
    print (" e.g. python server.py localhost 8888")
    print
    sys.exit()
  """
  #host = sys.argv[1]
  host = "Localhost"
  #port = int(sys.argv[2])
  port = 8888
  sock = start_server(host, port)
  print("Running server on host [{0}] and port [{1}]".format(host, port))
  
  RUNNING = True
  while RUNNING:
    message, conn = get_message(sock)
    print("MESSAGE: [{0}]".format(message))
    result, msg = handle_message(message)
    print ("Result: {0}\nMessage: {1}\n".format(result, msg))
    if result == "ERROR":
      conn.sendall(bytes("{0}\0".format(result)))
    elif result == "LOGIN":
      conn.sendall(bytes("{0}\0".format(result)))
    elif result == "OK":
      conn.sendall(bytes("{0}\0".format(result)))
    elif result == "SEND":
      conn.sendall(bytes("{0}\0".format(msg)))
    else:
      print("'else' reached.")
      RUNNING = False
    conn.close()

stop_server(sock)
