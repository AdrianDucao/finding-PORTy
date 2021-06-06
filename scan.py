#!/usr/bin/env python3

#import curses #for console interface...soon
from socket import *
import time
import os
import multiprocessing
import subprocess

from datetime import datetime


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

def ping_Sweep(job_q, results_q):
    DEVNULL = open(os.devnull, 'w')    
    
    while True:
        ip = job_q.get()
        if ip is None:
            break
        try:
            subprocess.check_call(['ping','-c1',ip], 
                                stdout = DEVNULL)
            results_q.put(ip)
        except:
            pass


if __name__ == '__main__':    
    print('======[finding-PORTy v1.]====== \n')
    print('===[OPTIONS]=== \n [1] Scan Open Ports \n [2] Ping Sweep Live Host (Loud) \n [3] TCP Scan (Stealth) \n')
    
    action = input('Action: ')    

    if(action == '1'):
        targetIP = input('===[Scan Open Ports]=== \n Enter IP: ')
        timer = time.time()
        socket_Scan(targetIP)
    
    elif(action == '2'):
        size = int(input('===[Ping Sweep Live Host]=== \n Enter Range(1 to ?): '))
        targetNetwork = input('\n Enter Network IP: ')
        splitIP = targetNetwork.split('.')
        x = '.'

        reconIP = size + 1

        jobs = multiprocessing.Queue()
        results = multiprocessing.Queue()
        pool = [multiprocessing.Process(target=ping_Sweep, args=(jobs, results))
                for i in range(size) ]

        for p in pool:
            p.start()
        for i in range(1,size):
            fnetwork = splitIP[0] + x + splitIP[1] + x + splitIP[2] + x + str(i) #tricky hack on splitting ip
            jobs.put(fnetwork)
        for p in pool:
            jobs.put(None)
        for p in pool:
            p.join()

        while not results.empty():
            liveIP = results.get()
            print(liveIP, '---> we got a live one!')
            

    elif(action == '3'):
        print('will add soon...')
    
    elif(action == '4'):
        print('will add soon...')
    
    else:
        print('incorrect option...')
