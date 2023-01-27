import threading
import time
import random

import socket

def client():
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: Client socket created")
    except socket.error as err:
        print('socket open error: {} \n'.format(err))
        exit()
        
    # Define the port on which you want to connect to the server
    port = 50007
    localhost_addr = socket.gethostbyname(socket.gethostname())

    # connect to the server on local machine
    server_binding = (localhost_addr, port)
    cs.connect(server_binding)

    # send a intro message to the server. 
    with open('in-proj.txt') as f:
        content = f.read() 
        
    # msg2 = "hello"
    print("Data sent to server: ", content)
    cs.send(content.encode('utf-8'))    

    # msg3 = "hello"
    # print("Data sent to client for uppercase: ", msg3)
    # cs.send(msg3.encode('utf-8'))
   
    # Receive data from the server
    data_from_server=cs.recv(200)
    print("[C]: Data received from server: {}".format(data_from_server.decode('utf-8')))

    # Receive data from the server
    data_from_serverrev=cs.recv(200)
    print("[C]: Uppercase data received from server: {}".format(data_from_serverrev.decode('utf-8')))

    data_from_serverup=cs.recv(200)
    print("[C]: Reversed data received from server: {}".format(data_from_serverup.decode('utf-8')))

    # close the client socket
    cs.close()
    exit()

if __name__ == "__main__":
    # t1 = threading.Thread(name='server', target=server)
    # t1.start()

    # time.sleep(random.random() * 5)
    t2 = threading.Thread(name='client', target=client)
    t2.start()

    time.sleep(5)
    print("Done.")