#!/usr/bin/env python3

#import curses #for console interface...soon
from socket import *
import time

def socket_Scan(targetIP):
    host = gethostbyname(targetIP)
    print('Scanning...',host)
    
    for i in range(0, 65535):
        soc = socket(AF_INET, SOCK_STREAM)
    
        connect = soc.connect_ex((host, i))
        if(connect == 0):
            print('Port %d: [OPEN]'%(i,))
        soc.close()
    
    print('time taken = ', time.time() - timer)


if __name__ == '__main__':    
    print('>==>= >finding-PORTy v1.0 \n')
    print('[OPTIONS] \n [1] Scan all Open Ports \n [2] Scan for Live Host \n [3] TCP Scan \n [4] UDP Scan \n')
    
    action = input('Action: ')    

    if(action == '1'):
        targetIP = input('Enter IP: ')
        timer = time.time()
        socket_Scan(targetIP)
    elif(action == '2'):
        print('will add soon...')
    elif(action == '3'):
        print('will add soon...')
    elif(action == '4'):
        print('will add soon...')
    else:
        print('incorrect option...')
