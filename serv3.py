import os, time, sys
from socket import * 
myHost = '0.0.0.0' 
myPort = 2222 
sockobj = socket(AF_INET, SOCK_STREAM) 
sockobj.bind((myHost, myPort)) 
sockobj.listen(1)

activeChildren = []
def reapChildren(): 
    while activeChildren: 
    pid, stat = os.waitpid(0, os.WNOHANG) 
    if not pid: break 
    activeChildren.remove(pid)
def handleClient(connection): 

    while True: 
        data = connection.recv(1024) 
        if data=='close': break 
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
 connection.close()
 os._exit(0)
def dispatcher(): 
    while True: 
        connection, address = sockobj.accept() 
        print('Server connected by', address, end=' ') 
        print('at', now())
        reapChildren()
        childPid = os.fork() 
        if childPid == 0:
            handleClient(connection)
        else: 
            activeChildren.append(childPid)
dispatcher()
