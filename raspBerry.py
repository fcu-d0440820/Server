# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket   

HOST='localhost'  
PORT=6666
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)  
s.bind((HOST,PORT))   
s.listen(3)
print('等待客戶端連結...') 
while True:  
    conn,addr=s.accept()  
    print('Connected by',addr)
    length_of_message = int.from_bytes(conn.recv(2), byteorder='big')
    data=conn.recv(length_of_message).decode('utf-8')
    print(data)

    if data =="exit" :
        break
        
    cmd = "好開勳".encode("utf-8")
    conn.send(cmd)
    print('傳送: ' ,cmd)
conn.close() 