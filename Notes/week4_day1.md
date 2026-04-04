1. What is Nmap?

Nmap (Network Mapper) is an open-source tool used for:
      
      * Network discovery
      * Port scanning
      * Security auditing

It tells us:

      * Which devices are online
      * What services they are running
      * Possible vulnerabilities

2. What is Nmap used for?

      * Discover hosts on a network
      * Identify open ports
      * Detect running services (HTTP, FTP, SSH, etc.)
      * OS fingerprinting
      * Vulnerability scanning (via NSE scripts)

3. OSI Layers Nmap interacts with

Nmap mainly works on:

| Layer   | Name        | Role                  |
| ------- | ----------- | --------------------- |
| Layer 3 | Network     | IP (host discovery)   |
| Layer 4 | Transport   | TCP/UDP port scanning |
| Layer 7 | Application | Service detection     |

4. How TCP Scan Works (-sS)

SYN Scan (Stealth Scan)

Steps:

      1. Nmap sends SYN
      2. If target responds:
            * SYN-ACK → port is **open**
            * RST → port is **closed**
      3. Nmap sends RST (doesn't complete handshake) - Called “half-open scan”

Command:

      nmap -sS <target>

5. How UDP Scan Works (-sU)

Steps:

      1. Nmap sends UDP packet
      2. If:
      
         * ICMP unreachable → port **closed**
         * No response → open|filtered

Command:

      nmap -sU <target>

6. Why UDP scans are slower

      * No handshake
      * No response = unclear result
      * Relies on ICMP (often blocked)
      * Requires retries

7. OS Detection (-O)

Nmap tries to identify:

      * Operating system (Windows, Linux, etc.)
      * Kernel version
      * Device type

It Uses:

      * TCP/IP fingerprinting
      * Packet behavior differences

Command:

      nmap -O <target>

8. NSE (Nmap Scripting Engine)

NSE allows automation using scripts.

Used for:

      * Vulnerability detection
      * Brute force attacks
      * Service enumeration

Example:

      nmap --script=vuln <target>

9. Common Nmap Flags

      | Flag | Meaning             |
      | ---- | ------------------- |
      | -sS  | SYN scan            |
      | -sT  | TCP connect scan    |
      | -sU  | UDP scan            |
      | -O   | OS detection        |
      | -A   | Aggressive scan     |
      | -p   | Specify ports       |
      | -Pn  | Skip host discovery |
      | -T4  | Faster scan         |
      | -v   | Verbose             |

10. -sS vs -sT

      | Feature   | -sS           | -sT             |
      | --------- | ------------- | --------------- |
      | Type      | Half-open     | Full connection |
      | Speed     | Faster        | Slower          |
      | Stealth   | More stealthy | Easily detected |
      | Privilege | Requires root | No root needed  |

11. What does "filtered" mean?

A port is 'filtered' when:

      Nmap cannot determine its state

Usually due to:

      Firewall
      Packet filtering

12. Firewall Evasion Techniques

Techniques:
      
      * Fragment packets:

            nmap -f <target>

      * Use decoys:

            nmap -D RND:10 <target>

      * Change source port:
      
            nmap --source-port 53 <target>
      
      * Slow scan:
      
            nmap -T1 <target>

Goal: avoid detection

13. Nmap Xmas Scan (-sX)

Sends packets with:

      * FIN
      * PSH
      * URG flags

Behavior:

      * No response → **open|filtered**
      * RST → **closed**

Command:

      nmap -sX <target>

14. Beyond Class (Important Concepts)

Scan Types You Should Know

      * FIN Scan (`-sF`)
      * NULL Scan (`-sN`)
      * ACK Scan (`-sA`) → firewall detection
