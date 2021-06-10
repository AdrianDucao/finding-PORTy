#!/usr/bin/env python3

#import curses #for console interface...soon
from socket import *
import time
import os
import multiprocessing
import subprocess
import csv

from datetime import datetime

def check_history():
    try:
        with open('history.csv','rb') as f:
            reader=csv.reader(f)
    except:
         with open('history.csv','a', newline='') as csvfile:
             filewriter = csv.writer(csvfile, delimiter=',', 
                                     quotechar='|', quoting=csv.QUOTE_MINIMAL)
             currentDate = datetime.now()
             filewriter.writerow([currentDate])

def show_history():
    try:
        with open('history.csv') as f:
            reader = csv.reader(f)

            for row in reader:
                print(row)
    except:
        pass

def write_history(action, data):
    with open('history.csv','a', newline='') as csvfile: 
        filewriter = csv.writer(csvfile, delimiter=',', 
                                quotechar='|', quoting=csv.QUOTE_MINIMAL)
        currentDate = datetime.now()
        data1 = action
        data2 = data
        filewriter.writerow([data1, data2])

def socket_Scan(targetIP, write_history):
    dt = datetime.now()
    timer = time.time()
    host = gethostbyname(targetIP)
    action = '-------------------Port Scan--------------------- \n'
    write_history(action,dt)

    print('Scanning...')

    for i in range(0, 65535):
        soc = socket(AF_INET, SOCK_STREAM)
        connect = soc.connect_ex((host, i))
        
        if(connect == 0):
            print('Port %d: ->[OPEN]'%(i,))
            data = 'Port %d: ->[OPEN]}'%(i,)
            soc.close()
            write_history('', data)
    time_taken = time.time() - timer
    write_history('time taken =',time_taken)
    print('time taken = ', time_taken)

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

def menu():
    
    print(""" 
    |\    o
    |  \    o
|\ /    .\ o
| |       ( ======[finding-PORTy v1.]======
|/ \     /
    |  /
     |/
                    """)
    print('\n')
    print('===[OPTIONS]=== \n [1] Scan Open Ports \n [2] Ping Sweep Live Host (Loud) \n [3] TCP Scan (Stealth) \n [4] Show Activities \n [5] Remove History \n [0] Exit')
    while(True):
        action = input('Action: ')    

        if(action == '1'):
            targetIP = input('===[Scan Open Ports]=== \n Enter IP: ')
            check_history()
            socket_Scan(targetIP, write_history)
    
        elif(action == '2'):
            check_history()
            action = '-------------------Ping Sweep Live Host--------------------- \n'
            data = 'Scanning'
            write_history(action, data)

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
                data = liveIP,'---> we got a live one!'
                dateTime = datetime.now()
                write_history(dateTime, data)
                print(liveIP, '---> we got a live one!')
            
        elif(action == '3'):
            print('will add soon...')
    
        elif(action == '4'):
            show_history()

        elif(action == '5'):
            print('will add soon...')
        elif(action == '0'):
            exit(0)
        else:
            print('incorrect option...')

if __name__ == '__main__':   
    menu() 
