# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import socket   
import RPi.GPIO as gpio
import time

gpio.setmode(gpio.BOARD)
gpio.setwarnings(False)
 
pin = [29, 31, 33, 35]
for i in range(4):
    gpio.setup(pin[i], gpio.OUT)
 
forward_sq = ['0011', '1001', '1100', '0110']
reverse_sq = ['0110', '1100', '1001', '0011']
 
def forward(steps, delay):
    for i in range(steps):
        for step in forward_sq:
            set_motor(step)
            time.sleep(delay)
 
def reverse(steps, delay):
    for i in range(steps):
        for step in reverse_sq:
            set_motor(step)
            time.sleep(delay)
 
def set_motor(step):
    for i in range(4):
        gpio.output(pin[i], step[i] == '1')
        
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
        
    elif data =="feed" :
        set_motor('0000')
        forward(241, 0.005)
        
    cmd = "好開勳".encode("utf-8")
    conn.send(cmd)
    print('傳送: ' ,cmd)
conn.close() 
