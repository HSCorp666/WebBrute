import socket

def port_scan(ip, port):
    try:
        sock = socket.socket()
        sock.settimeout(.4)
        sock.connect((ip, port))
        print('Port', port, 'is open')
        exit()
    except:
        print('Port', port, 'is closed')
        exit()


def inputs():
    ip = str(input("Enter IP address:-> "))
    port = input("Enter port:-> ")

    port_scan(ip, port)