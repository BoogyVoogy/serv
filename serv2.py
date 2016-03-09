import time, _thread as thread 
from socket import * 
myHost = '0.0.0.0' 
myPort = 2222 
sockobj = socket(AF_INET, SOCK_STREAM) 
sockobj.bind((myHost, myPort)) 
sockobj.listen(1) 

 
def handleClient(connection): 
    time.sleep(5) 
    while True: 
        data = connection.recv(1024)
        if not data: break
        reply = 'Echo=>%s at %s' % (data, now())
        connection.send(reply.encode())
    connection.close()
def dispatcher(): # пока процесс работает,
    while True: 
        connection, address = sockobj.accept() 
        thread.start_new_thread(handleClient, (connection,))
dispatcher()