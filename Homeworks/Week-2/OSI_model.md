1. What is OSI Model?

   The OSI (Open Systems Interconnection) model is a 7-layer framework used to understand how data moves from one device to another over a network.

OSI Model (7 Layers)

📚 Layers Overview

    7. Application
    6. Presentation
    5. Session
    4. Transport
    3. Network
    2. Data Link
    1. Physical
    
🔍 Layer-by-Layer Explanation

    Layer	                  Function	                   Examples
    7. Application	    User interaction	            HTTP, FTP, DNS
    6. Presentation	    Encryption, formatting	      SSL/TLS
    5. Session	        Manages sessions             	Login sessions
    4. Transport	      Data delivery	                TCP, UDP
    3. Network	        Routing  IP	                  IP, ICMP
    2. Data Link	      MAC addressing	              Ethernet
    1. Physical	        Hardware transmission	        Cables

OSI Layers in context of Telegram
   
Layer 7 – Application

This is where the user interacts with the interface

        user open the app
        user type and send a message

Protocols:

    HTTP / HTTPS
Layer 6 – Presentation

Handles encryption and formatting

          user message is encrypted
          Data is formatted into readable structure

Layer 5 – Session

Manages connection between users

        Maintains user login session
        Keeps chat connection active
        
Layer 4 – Transport

Responsible for delivery (TCP/UDP)

        user messages is broken into segments
        message is sent reliably using TCP (or fast using UDP)
        
Layer 3 – Network

Handles IP addressing and routing
    
        user message is sent from user IP
          to Telegram server IP
            then to the perosn whom we are sending to
        
Layer 2 – Data Link

Uses MAC addresses for local delivery

        our device communicates with router (WiFi)
        
Layer 1 – Physical

Actual transmission of data

    Data travels as electrical signals or radio waves (WiFi/mobile data)

3. Vulnerabilities in Each Layer

Layer 7 – Application

    Phishing links sent via chat
    Malicious files
    
Layer 6 – Presentation

    Weak encryption
    Data leakage if encryption fails
    
Layer 5 – Session

    Session hijacking
    Unauthorized account access
    
Layer 4 – Transport

    SYN flood attacks
    Port scanning
    
Layer 3 – Network

    IP spoofing
    Man-in-the-middle attacks
    
Layer 2 – Data Link

    ARP spoofing
    MAC spoofing
    
Layer 1 – Physical

    Device theft
    Network cable tapping
    
4. Ports Related to Telegram Communication

Telegram mainly uses:

    Port	Protocol	Purpose
    
    80	TCP	HTTP
    
    443	TCP	HTTPS (secure communication)

Top 30 Common Ports

Important Ports List

    Port	Protocol	Service
    20	TCP	FTP (data)
    21	TCP	FTP
    22	TCP	SSH
    23	TCP	Telnet
    25	TCP	SMTP
    53	TCP/UDP	DNS
    67	UDP	DHCP
    68	UDP	DHCP
    69	UDP	TFTP
    80	TCP	HTTP
    110	TCP	POP3
    119	TCP	NNTP
    123	UDP	NTP
    137	UDP	NetBIOS
    138	UDP	NetBIOS
    139	TCP	NetBIOS
    143	TCP	IMAP
    161	UDP	SNMP
    179	TCP	BGP
    389	TCP/UDP	LDAP
    443	TCP	HTTPS
    445	TCP	SMB
    465	TCP	SMTPS
    500	UDP	ISAKMP
    514	UDP	Syslog
    515	TCP	Printer
    520	UDP	RIP
    587	TCP	SMTP (secure)
    993	TCP	IMAPS
    995	TCP	POP3S
