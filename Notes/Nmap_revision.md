# Network Port Scanning Methods Reference

This document provides a technical overview of common TCP port scanning techniques, their underlying mechanisms, packet behaviors, and native Nmap implementation commands.

---

## 📊 Quick Summary Table

| Scan Type | Nmap Command | Target Open Port Behavior | Stealth Level | Requirements |
| :--- | :--- | :--- | :--- | :--- |
| **TCP Connect** | `nmap -sT <target>` | SYN-ACK $\rightarrow$ Completes handshake with ACK $\rightarrow$ RST | Low (Fully logged) | No root privileges required |
| **Stealth SYN** | `nmap -sS <target>` | SYN-ACK $\rightarrow$ Instantly sends RST to abort | Medium | Root/Administrator privileges |
| **Null Scan** | `nmap -sN <target>` | No response (Relies on RFC 793 behavior) | High | Root/Administrator privileges |
| **FIN Scan** | `nmap -sF <target>` | No response (Relies on RFC 793 behavior) | High | Root/Administrator privileges |
| **Xmas Scan** | `nmap -sX <target>` | No response (Relies on RFC 793 behavior) | High | Root/Administrator privileges |
| **Idle (Zombie)** | `nmap -sI <zombie> <target>` | Zombie IP ID increments by 2 | Maximum (Blind scan) | Root + Predictable Zombie IP ID |

---

## 🔍 Detailed Behavior Breakdown

### 1. TCP Connect Scan (`-sT`)
* **Mechanism:** The attacker performs a standard full TCP three-way handshake (`SYN` $\rightarrow$ `SYN-ACK` $\rightarrow$ `ACK`).
* **Open Port Response:** Target returns `SYN-ACK`. The attacker replies with an `ACK` to complete the connection, then immediately sends an `RST` to tear it down.
* **Closed Port Response:** Target returns an `RST`.
* **Note:** This is the most reliable scan method but is easily logged by application servers because a full connection is established.

### 2. Stealth (SYN) Scan (`-sS`)
* **Mechanism:** Also known as a "half-open" scan. The attacker stops short of establishing a full session.
* **Open Port Response:** Target returns a `SYN-ACK`. Instead of replying with an `ACK`, the attacker instantly sends an `RST` to abort the connection attempt.
* **Closed Port Response:** Target returns an `RST`.
* **Note:** This is the default Nmap scan type when run as root. It is faster and harder to log than a full connect scan.

### 3. Null, FIN, and Xmas Scans
These are "malformed" packet scans that rely on how specific Unix-like operating systems (such as Linux or BSD) handle TCP packets outside of active connections. They generally **do not work** reliably against Windows systems due to differences in TCP/IP stack implementations.

* **Null Scan (`-sN`):** Sends a packet with zero flags set (all bits 0).
* **FIN Scan (`-sF`):** Sends a packet with only the `FIN` flag set.
* **Xmas Scan (`-sX`):** Sends a packet with the `FIN`, `PSH`, and `URG` flags set simultaneously (lighting up the packet like a Christmas tree).
* **Packet Behavior:** 
  * According to RFC 793, if a port is **closed**, the target must respond with an `RST`. 
  * If the port is **open**, the target discards the malformed packet and returns **no response**.

### 4. Idle / Zombie Scan (`-sI`)
* **Mechanism:** A highly sophisticated, completely blind scanning technique that utilizes a third-party host (the zombie) to obscure the attacker's true IP address. It relies on monitoring the Zombie’s IP ID sequence changes.
* **How it works:**
  1. The attacker probes the Zombie machine's current IP ID number.
  2. The attacker sends a spoofed packet to the intended Target port, altering the packet header to look like it originated from the Zombie IP.
  3. **If the target port is open:** The Target sends a `SYN-ACK` to the Zombie. The Zombie, confused by the unsolicited packet, replies with an `RST`, which increments its IP ID by 1.
  4. **If the target port is closed:** The Target sends an `RST` to the Zombie. The Zombie discards this and does not increment its IP ID.
  5. The attacker probes the Zombie's IP ID again. If the ID increased by 2 (accounting for the step 1 probe and step 3 response), the target port is open. If it only increased by 1, the port is closed.

---

## 🛠️ Command Cheat Sheet

```bash
# Basic TCP Connect Scan
sudo nmap -sT 192.168.1.50

# Default Stealth SYN Scan
sudo nmap -sS 192.168.1.50

# Inverse / Malformed Flag Scans
sudo nmap -sN 192.168.1.50
sudo nmap -sF 192.168.1.50
sudo nmap -sX 192.168.1.50

# Blind Idle Scan (Requires Zombie IP and Target IP)
sudo nmap -sI 192.168.1.20 192.168.1.50
```
