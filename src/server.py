import socket
import sys
import flask

def parse_unit(unit):
    keys = ["time", "index", "name", "lat", "lon", "alt", "heading", "coalition", "unitname", "groupname"]
    unitMap={}
    if len(unit) == len(keys):
        for i,k in enumerate(keys):
            unitMap[k]=unit[i]
        return unitMap
    else:
        return None

sock = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server_address = ('localhost', 9595)
sock.bind(server_address)

RECV_SIZE = 16
sock.listen(1)
connection, client_address = sock.accept()
print("Connected")
while True:
    data = connection.recv(RECV_SIZE)
    buffer = data
    while len(data) == RECV_SIZE:
        data = connection.recv(RECV_SIZE)
        buffer += data
    if len(buffer) > 0:
        text = buffer.decode("utf-8").split("\n")
        units = []
        for line in text:
            if line:
                unit = line.split("\t")
                if (unit[0]=="UNIT"):
                    units.append(parse_unit(unit[1:]))
        print(units)