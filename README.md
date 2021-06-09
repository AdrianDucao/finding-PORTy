# finding-PORTy
This is tool will allow you to do basic port scanning and do basic reconnaissance on a network, for educational purposes only
 
```bash
 
    |\    o
    |  \    o
|\ /    .\ o
| |       ( ======[finding-PORTy v1.]======
|/ \     /
    |  /
     |/
                    


===[OPTIONS]=== 
 [1] Scan Open Ports 
 [2] Ping Sweep Live Host (Loud) 
 [3] TCP Scan (Stealth) 
 [4] Show Activities 
 [5] Remove History
Action: 

```

### Features:
1. Scan Open Ports - Allows you to check for open ports on specific host in a network
2. Ping Sweep Live Host (Loud) - Allows you to check for connected Live Host on a network, note that this is too obvious and loud to use can be tracked by honeypots or wireshark
3. TCP Scan (Stealth) - coming soon, will use SYN flag, SYN-ACK and ACK on packets
4. View Activities - shows the past activities or history where you can review previous data
5. Clear Activities - removal of history.csv file

### Installation and Usage:
```bash
$ git clone https://github.com/AdrianDucao/finding-PORTy.git

$ cd finding-PORTy

$ ./scan.py

```
and your off to the races

#### Scan Open Ports
here's an example on how port scanning is used
```bash
$ ./scan.py
 
    |\    o
    |  \    o
|\ /    .\ o
| |       ( ======[finding-PORTy v1.]======
|/ \     /
    |  /
     |/
                    


===[OPTIONS]=== 
 [1] Scan Open Ports 
 [2] Ping Sweep Live Host (Loud) 
 [3] TCP Scan (Stealth) 
 [4] Show Activities 
 [5] Remove History
Action: 1 
===[Scan Open Ports]=== 
 Enter IP: 192.168.254.135
Scanning...
Port 80: ->[OPEN]
Port 1624: ->[OPEN]
Port 5355: ->[OPEN]
Port 32400: ->[OPEN]
Port 32469: ->[OPEN]
Port 51204: ->[OPEN]
Port 60278: ->[OPEN]
time taken =  3.6720473766326904

```

#### Ping Sweep Live Host
here's the example and how it would looked like, remember to use the gateway or router's IP and not the targets IP
```bash
$ ./scan.py
 
    |\    o
    |  \    o
|\ /    .\ o
| |       ( ======[finding-PORTy v1.]======
|/ \     /
    |  /
     |/
                    


===[OPTIONS]=== 
 [1] Scan Open Ports 
 [2] Ping Sweep Live Host (Loud) 
 [3] TCP Scan (Stealth) 
 [4] Show Activities 
 [5] Remove History
Action: 2
===[Ping Sweep Live Host]=== 
 Enter Range(1 to ?): 255

 Enter Network IP: 192.168.254.254
192.168.254.105 ---> we got a live one!
192.168.254.135 ---> we got a live one!
192.168.254.103 ---> we got a live one!

```

#### Show Activities
this will show the history of your activities for later usage, note you can remove this data whenever you don't need it.
```bash
$ ./scan.py
 
    |\    o
    |  \    o
|\ /    .\ o
| |       ( ======[finding-PORTy v1.]======
|/ \     /
    |  /
     |/
                    


===[OPTIONS]=== 
 [1] Scan Open Ports 
 [2] Ping Sweep Live Host (Loud) 
 [3] TCP Scan (Stealth) 
 [4] Show Activities 
 [5] Remove History
Action: 4
['2021-06-09 11:20:04.686995']
['|-------------------Ping Sweep Live Host--------------------- ']
['|', 'Scanning']
['2021-06-09 11:20:22.333781', "|('192.168.254.105'", " '---> we got a live one!')|"]
['2021-06-09 11:20:22.334037', "|('192.168.254.135'", " '---> we got a live one!')|"]
['|-------------------Port Scan--------------------- ']
['|', 'Scanning...']
['', 'Port 80: ->[OPEN]}']
['', 'Port 1624: ->[OPEN]}']
['', 'Port 5355: ->[OPEN]}']
['', 'Port 32400: ->[OPEN]}']
['', 'Port 32469: ->[OPEN]}']
['', 'Port 42848: ->[OPEN]}']
['', 'Port 51618: ->[OPEN]}']
['time taken =', '3.6771161556243896']
['|-------------------Port Scan--------------------- ']
['|', 'Scanning...']
['', 'Port 80: ->[OPEN]}']
['', 'Port 1624: ->[OPEN]}']
['', 'Port 5355: ->[OPEN]}']
['', 'Port 32400: ->[OPEN]}']
['', 'Port 32469: ->[OPEN]}']
['', 'Port 51204: ->[OPEN]}']
['', 'Port 60278: ->[OPEN]}']
['time taken =', '3.6720473766326904']
['|-------------------Ping Sweep Live Host--------------------- ']
['|', 'Scanning']
['2021-06-09 11:26:04.192099', "|('192.168.254.105'", " '---> we got a live one!')|"]
['2021-06-09 11:26:04.192555', "|('192.168.254.135'", " '---> we got a live one!')|"]
['2021-06-09 11:26:04.192754', "|('192.168.254.103'", " '---> we got a live one!')|"]

```
