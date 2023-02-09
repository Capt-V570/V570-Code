import socket

# Create the socket (make a phone!)
mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# Dial the phone -> (to a domain name and a port to that domain name)
mysock.connect(("data.pr4e.org", 80))
# If you get this far, we need to send a command, encoded in the UTF-8 string:
try:
    cmd = "GET http://data.pr4e.org/page1.htm HTTP/1.0\r\n\r\n".encode()
    mysock.send(cmd)
except socket.error:
    mysock.close()

# Loop to receive data until the socket is closed (up until 512 characters):
while True:
    data = mysock.recv(512)
    # if we don't get any data whatsoever (e.g. <1 character), we gonna break the connection:
    if len(data) < 1:
        break
    # if something come up, we gonna print it on screen, by deconding it (as it is in UTF-8) to Unicode (UTF-16 for Python):
    print(data.decode(), end="")

    mysock.close()
