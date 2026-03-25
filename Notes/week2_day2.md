  Week1_Day-2

1. What is Networking?

Networking is the connection of multiple devices to communicate and share data.

Examples:
* Internet
* Local Area Network (LAN)
* WiFi networks

---

2. IP Address (Internet Protocol)
An IP address is a unique identifier assigned to each device on a network.

Example:
        10.201.206.203
        192.168.1.1

        Commands to Check IP
ip a        # show your IP address
ip route    # show gateway (router)


        3. IP Classes (A, B, C)
IP addresses are divided into classes based on network size.

 Class A
* Range: `1.0.0.0 – 126.255.255.255`
* Default subnet: `/8`
* Large networks (big organizations)

 Class B

* Range: `128.0.0.0 – 191.255.255.255`
* Default subnet: `/16`
* Medium networks

 Class C
* Range: `192.0.0.0 – 223.255.255.255`
* Default subnet: `/24`
* Small networks (most common)

Example:
10.201.206.203 → Class A
192.168.1.1   → Class C


        5. OSI Model (7 Layers)
A theoretical model used to understand how networks work.

         Layers
7. Application
6. Presentation
5. Session
4. Transport
3. Network
2. Data Link
1. Physical

        Summary
| Layer        | Function                     |
| ------------ | ---------------------------- |
| Application  | user interaction (HTTP, DNS) |
| Presentation | encryption, formatting       |
| Session      | manages sessions             |
| Transport    | TCP/UDP, ports               |
| Network      | IP addressing                |
| Data Link    | MAC address                  |
| Physical     | cables, signals              |


6. TCP/IP Model (Real World Model)

Used in real networking (internet).

        Layers
Application

Transport

Internet

Network Access


7. TCP (Transmission Control Protocol)
Reliable communication protocol.
* Connection-based
* Ensures data delivery
* Uses ports

3-Way Handshake
        SYN → SYN-ACK → ACK


                        8. UDP (User Datagram Protocol)
Fast but unreliable protocol.
* No connection
* No delivery guarantee
* Faster than TCP

Used In
* Streaming
* Gaming
* Voice calls

TCP vs UDP
| Feature    | TCP    | UDP    |
| ---------- | ------ | ------ |
| Reliable   | Yes    | No     |
| Speed      | Slower | Faster |
| Connection | Yes    | No     |


                SUMMARY
* IP identifies devices on a network
* Class A, B, C define network sizes
* OSI = theoretical (7 layers)
* TCP/IP = real-world model (4 layers)
* TCP = reliable, UDP = fast
