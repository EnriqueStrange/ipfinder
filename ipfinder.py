import socket

hostname = socket.gethostname()
myip = socket.gethostbyname(hostname)

print("YOU ARE WORKING ON " + hostname)
print("YOUR IP IS " + myip)

url = input("ENTER THE URL TO SCAN >> ")
print("THE IP FOR " + url + " IS ",socket.gethostbyname(url))