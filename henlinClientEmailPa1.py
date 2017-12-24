from socket import *
from time import *
from encodings.base64_codec import base64_decode, base64_encode

msg = "\r\n I love computer networks!"
endmsg = "\r\n.\r\n"

userName = "whenlin45@gmail.com"
password = ""   #DELETE THIS WHEN SUBMITTING!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
base64_str = ("\x00"+userName+"\x00"+password).encode()
#base64_str = base64_encode(base64_str)
authMsg = "AUTH PLAIN ".encode()+base64_str+"\r\n".encode()

# Choose a mail server (e.g. Google mail server) and call it mailserver
#Fill in start 
mailserver = ("smtp.gmail.com", 587)
#Fill in end
# Create socket called clientSocket and establish a TCP connection with mailserver
#Fill in start
clientSocket =  socket(AF_INET, SOCK_STREAM)
clientSocket.connect(mailserver)

#Fill in end

recv = clientSocket.recv(1024).decode()
print(recv)

if recv[:3] != '220':
    print('220 reply not received from server.')
        
# Send HELO command and print server response.
heloCommand = 'HELO Alice\r\n'
clientSocket.send(heloCommand.encode())
recv1 = clientSocket.recv(1024).decode()
print(recv1)

#tls = 'STARTTLS'
#tls = tls.encode()
#clientSocket.send(tls)
#recvTLS = clientSocket.recv(1024)

clientSocket.send(authMsg)
recvAuthentication = clientSocket.recv(1024)   #authenticating user credentials
print(recvAuthentication.decode())

if recv1[:3] != '250':
    print('250 reply not received from server.')
# Send MAIL FROM command and print server response. 
# Fill in start

mailFrom = "MAIL FROM:<" + fromaddr + ">\r\n"
clientSocket.send(mailFrom.encode())
recv2 = clientSocket.recv(1024)
recv2 = recv2.decode()
print("After MAIL FROM command: "+recv2)

# Fill in end
# Send RCPT TO command and print server response.
# Fill in start

rcptTo = "RCPT TO:<whenlin@uwo.ca>\r\n"
clientSocket.send(rcptTo.encode())
recv3 = clientSocket.recv(1024)
recv3 = recv3.decode()
print("After RCPT TO command: "+recv3)

# Fill in end
# Send DATA command and print server response.
# Fill in start

data = "DATA\r\n"
clientSocket.send(data.encode())
recv4 = clientSocket.recv(1024)
recv4 = recv4.decode()
print("After DATA command: "+recv4)
# Fill in end

# Send message data.
# Fill in start

subject = "Subject: testing my client\r\n\r\n" 
clientSocket.send(subject.encode())
date = time.strftime("%a, %d %b %Y %H:%M:%S +0000", time.gmtime())
date = date + "\r\n\r\n"
clientSocket.send(date.encode())
clientSocket.send(msg.encode())
clientSocket.send(endmsg.encode())
recv_msg = clientSocket.recv(1024)
print("Response after sending message body:"+recv_msg.decode())

                                # Message ends with a single period.

# Fill in end
# Send QUIT command and get server response.
# Fill in start
quitMsg = "QUIT\r\n"
clientSocket.send(quitMsg.encode())
recv5 = clientSocket.recv(1024)
print("Final Server Response:" + recv5.decode())
# Fill in end