import threading
import time
import random

import socket

def server():
    try:
        ss = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[S]: Server socket created")
    except socket.error as err:
        print('socket open error: {}\n'.format(err))
        exit()

    server_binding = ('', 50007)
    ss.bind(server_binding)
    ss.listen(1)
    host = socket.gethostname()
    print("[S]: Server host name is {}".format(host))
    localhost_ip = (socket.gethostbyname(host))
    print("[S]: Server IP address is {}".format(localhost_ip))
    csockid, addr = ss.accept()
    print ("[S]: Got a connection request from a client at {}".format(addr))

    # send a intro message to the client.  
    msg = "Welcome to CS 352!"
    csockid.send(msg.encode('utf-8'))

     # Receive data from the client
    data_from_client=csockid.recv(100)
    data = data_from_client.decode('utf-8')
    #print("[C]: Data received from client: {}".format(data_from_client.decode('utf-8')))
    datarev = data[::-1]
    csockid.send(datarev.encode('utf-8'))

    time.sleep(3)

    # data_from_client2=csockid.recv(100)
    data2 = data_from_client.decode('utf-8')
    dataup = data2.upper()
    csockid.send(dataup.encode('utf-8'))


    # Close the server socket
    ss.close()
    exit()

if __name__ == "__main__":
    t1 = threading.Thread(name='server', target=server)
    t1.start()

    time.sleep(random.random() * 5)
    # t2 = threading.Thread(name='client', target=client)
    # t2.start()

    # time.sleep(5)
    # print("Done.")