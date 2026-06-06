Table of Contents

        Introduction to Post-Exploitation
        Local Enumeration
        Privilege Escalation Concepts
        Tools Reference
        Defensive Considerations
        Further Resources


1. Introduction to Post-Exploitation

        What Happens After Gaining Access?
   
Gaining initial access to a target system is only the beginning of a penetration test. Post-exploitation is the phase that follows — it is where a tester demonstrates the real-world impact of a vulnerability. This phase typically involves:

        Situational awareness — understanding where you are and what you have access to
        Privilege escalation — moving from a limited user to an administrator or root
        Lateral movement — pivoting to other systems in the network
        Persistence — establishing mechanisms to maintain access
        Data exfiltration — identifying and accessing sensitive data to prove impact

As defined by MITRE ATT&CK, privilege escalation refers to techniques adversaries use to gain higher-level permissions on a system or network. From a broader perspective, it is the act of exploiting a bug, design flaw, or configuration oversight in an operating system or application to gain access to resources that are normally protected.

        Why Post-Exploitation Matters in Pentesting
Post-exploitation is what separates a surface-level vulnerability scan from a true security assessment. Its goals in the context of a pentest include:

        Demonstrating real impact — proving that an attacker could extract data, install malware, or take over the environment
        Identifying privilege escalation paths — uncovering weaknesses in access controls
        Supporting lateral movement — discovering credentials and trust relationships that allow deeper network access
        Establishing persistence — showing that an attacker could maintain long-term access

A successful privilege escalation allows attackers to increase control over a system, make administrative changes, exfiltrate data, modify or damage the operating system, and maintain persistence through mechanisms such as registry edits or cron jobs.

        Rules of Engagement and Scope Considerations

Before conducting any post-exploitation activity, a penetration tester must operate within a clearly defined scope of engagement. Key considerations include:

        Written authorization — always required before testing
        Defined IP ranges and systems — know what is in-scope and out-of-scope
        Data handling rules — what to do with any sensitive data encountered
        Notification procedures — who to contact if a critical system is impacted
        Time windows — specific hours during which testing is permitted

Going outside the scope — even accidentally — can have legal consequences. This is especially true in post-exploitation, where actions like credential dumping or modifying services can affect production systems.

        Risk Assessment and Impact Evaluation

Every action in post-exploitation carries risk. Testers must evaluate:

        Stability risk — could running a kernel exploit crash the machine?
        Data risk — could a test inadvertently expose or corrupt sensitive data?
        Detection risk — will this action trigger alerts that could compromise the engagement?
        Business impact — what is the real-world consequence of the vulnerability being exploited?

Risk-aware testing is the hallmark of a professional penetration tester.

        2. Local Enumeration

After gaining initial access, thorough local enumeration is the most critical step before attempting any escalation. The goal is to gather as much information as possible about the target environment to identify potential attack paths.

Core principle: Enumeration is the most important part of the process — be as thorough as possible.

Enumeration is generally conducted in two ways:

        Manual — using native OS commands; slower but more thorough and less likely to trigger alerts
        Automated — using scripts like LinPEAS or WinPEAS; faster but noisier and may be flagged by AV/EDR

In practice, a blend of both approaches is used.

        2.1 System Information

Understanding the target operating system is the foundation of all subsequent enumeration.
InformationLinux CommandWindows CommandOS versioncat /etc/os-release or lsb_release -asysteminfoKernel versionuname -averArchitectureuname -msysteminfo | findstr /B /C:"OS"Installed packagesdpkg -l / rpm -qawmic product get name,versionPatch levelapt list --installedwmic qfe list

Why this matters:

        The kernel and OS version reveal whether known public exploits exist (e.g., Dirty Cow on Linux kernels, PrintNightmare on Windows)
        Patch levels indicate if critical security updates are missing
        Installed software may include vulnerable third-party applications
        Architecture (32-bit vs 64-bit) determines which exploit payloads are compatible


        2.2 User Enumeration

Knowing the user context and what other accounts exist is essential for understanding privilege boundaries.
InformationLinux CommandWindows CommandCurrent userwhoamiwhoamiCurrent privilegesidwhoami /privAll local userscat /etc/passwdnet userAll local groupscat /etc/groupnet localgroupSudo rightssudo -lN/ALogged-in usersw / whoquery userAdmin group membersgetent group sudonet localgroup Administrators

Key checks:

        sudo -l is one of the most valuable checks on Linux — it reveals commands a user can run as root, many of which can be abused via GTFOBins
        On Windows, whoami /priv reveals special tokens like SeImpersonatePrivilege which can be leveraged with Potato attacks
        Users in groups like docker, lxd, or disk on Linux may have indirect root-level access


        2.3 Process Enumeration

Running processes can reveal active services, security software, and privileged operations.
InformationLinux CommandWindows CommandAll running processesps auxtasklistProcesses by root/SYSTEMps aux | grep roottasklist /FI "USERNAME eq SYSTEM"Servicessystemctl list-units --type=servicesc queryOpen network portsnetstat -tulpnnetstat -ano

What to look for:

        Service accounts running processes — a vulnerable service running as SYSTEM on Windows or root on Linux is a direct escalation target
        Security products — identify antivirus, EDR, and SIEM agents so their detection capabilities can be considered (e.g., Defender, CrowdStrike, Sysmon)
        Custom internal applications — these often have weaker security than vendor software and may run with elevated permissions
        Privileged processes with weak permissions — on Windows, if a SYSTEM-level service uses an executable path you can write to, it becomes an escalation vector


        2.4 Network Enumeration

Understanding the network context reveals internal services, pivot opportunities, and further attack surface.
InformationLinux CommandWindows CommandNetwork interfacesip a / ifconfigipconfig /allRouting tableroute -n / ip routeroute printActive connectionsss -tulpn / netstat -annetstat -anoARP cachearp -aarp -aDNS configcat /etc/resolv.confipconfig /displaydns

        Why this matters:

Multiple network interfaces may indicate the system is a gateway between network segments
Internal services listening on 127.0.0.1 may be accessible only locally, providing a unique attack surface not visible from outside
The ARP cache reveals other hosts on the local network — useful for identifying lateral movement targets
Internal DNS names may reveal additional hosts, services, or domain controllers


        2.5 File System Enumeration

The file system often holds the most valuable information for privilege escalation — credentials, config files, and scripts with excessive permissions.

High-value targets on Linux:

        bash# World-writable files
        find / -writable -type f 2>/dev/null

# SUID/SGID binaries

        find / -perm -4000 -type f 2>/dev/null    # SUID
        find / -perm -2000 -type f 2>/dev/null    # SGID

# Cron jobs

        cat /etc/crontab
        ls -la /etc/cron.*
        crontab -l

# Config files with credentials

        find / -name "*.conf" 2>/dev/null
        find / -name "*.config" 2>/dev/null

# Bash history

        cat ~/.bash_history
        cat /home/*/.bash_history
        High-value targets on Windows:
        powershell# Unquoted service paths
        wmic service get name,displayname,pathname,startmode | findstr /i "auto" | findstr /i /v "c:\windows\\"

# Writable service executables

        icacls "C:\path\to\service.exe"

# Scheduled tasks

        schtasks /query /fo LIST /v

# Sensitive files

        dir /s /b *pass* *cred* *secret* *config* 2>nul

        2.6 Credential Discovery
        
Credentials found on the file system, in memory, or in environment variables are often the fastest path to privilege escalation.

        Linux credential locations:
        
LocationDescription/etc/shadowHashed passwords (requires root to read, but valuable if readable)~/.ssh/id_rsaPrivate SSH keys~/.bash_historyCommand history, may contain plaintext passwords/var/www/html/Web app config files with DB credentialsEnvironment variables (env)May contain API keys, passwords, or tokens/proc/*/environProcess environment variables

        Windows credential locations:
        
LocationDescriptionSAM databaseLocal account hashes (requires SYSTEM)LSASS memoryCredential material (extracted with Mimikatz)%APPDATA%\...\credentialsStored Windows credentialsRegistry (HKLM\SOFTWARE)Application configuration with credentialsUnattended install filesunattend.xml, sysprep.xml — may contain plaintext credsPowerShell history%APPDATA%\Microsoft\Windows\PowerShell\PSReadLine\ConsoleHost_history.txt

        2.7 Security Controls Discovery

Before escalation attempts, identify what security controls are in place.

Linux:

        bash# Check for AppArmor
        aa-status 2>/dev/null

# Check for SELinux

        getenforce 2>/dev/null

# Identify AV/EDR processes

        ps aux | grep -E "clam|av|edr|siem|falcon|carbon"
        
Windows:

        powershell# Windows Defender status
        Get-MpComputerStatus

# Firewall status

        netsh advfirewall show allprofiles

# Installed security software

        wmic /namespace:\\root\securitycenter2 path antivirusproduct get displayname
        Understanding these controls informs the escalation strategy — for example, known kernel exploits may be detected by EDR, requiring a stealthier misconfiguration-based approach instead.

        2.8 Automation Tools

While manual enumeration is critical for understanding and thoroughness, automation tools dramatically speed up the process.
ToolPlatformDescriptionLinPEASLinuxBash script; hundreds of checks; color-coded output by severityWinPEASWindowsPortable executable; scans services, registry, files, tokensLinEnumLinuxLightweight bash script for common local enumeration checksPowerUpWindowsPowerShell tool targeting common Windows escalation vectorslinux-exploit-suggesterLinuxSuggests kernel exploits based on OS versionSeatbeltWindowsC# enumeration tool with extensive host checksBeRootLinux/WindowsIdentifies common misconfiguration escalation paths

        Important caveats:

Automated tools generate noisy output — always verify findings manually before exploiting
Some AV/EDR solutions will flag and quarantine tools like WinPEAS on contact
Tools may produce false positives or miss context-specific vulnerabilities
Manual verification is always required; tools are a starting point, not a conclusion


        3. Privilege Escalation Concepts

Privilege escalation is the act of exploiting bugs, design flaws, or configuration oversights to gain elevated access to resources normally protected from a user. The goal is to move from a lower-privilege context (e.g., standard user or www-data) to a higher-privilege context (e.g., root or SYSTEM/Administrator).

        3.1 Types of Privilege Escalation

Vertical Privilege Escalation

        Moving up the privilege hierarchy — gaining a higher level of access than currently held.

Standard user → Administrator/root — the most common goal
Service account → Administrator — service accounts running applications may have configuration weaknesses that allow escaping to a higher privilege context
Low-privileged shell → SYSTEM (Windows) — many Windows escalation techniques target the SYSTEM account, which is more powerful than even a local Administrator

Horizontal Privilege Escalation

        Moving laterally across accounts at the same privilege level.

Accessing another user's resources — reading files in /home/otheruser/, accessing another user's email or browser data
Moving between accounts with similar privilege levels — using one compromised account to gain access to another account's data or sessions

Horizontal escalation is particularly relevant in multi-user environments and often precedes vertical escalation (e.g., compromising a higher-value user account that has administrative access).

3.2 Common Escalation Categories

        A. Misconfiguration-Based Escalation

Misconfigurations are among the most prevalent and exploitable privilege escalation vectors. They require no vulnerability in code — only an incorrect setting.

        Linux:
MisconfigurationDescriptionExampleSUID binariesPrograms that execute with the file owner's permissionsfind / -perm -4000; exploit via GTFOBinsSudo misconfigurationsUser allowed to run specific commands as rootsudo vim → :!/bin/bashWritable cron scriptsCron job runs a script the attacker can modifyReplace script content with reverse shellWorld-writable /etc/passwdRare but critical — allows adding a root userAdd hacker:x:0:0::/root:/bin/bashDocker group membershipCan mount the host filesystem inside a containerdocker run -v /:/mnt alpine chroot /mnt sh

        Windows:

MisconfigurationDescriptionUnquoted service pathsWindows searches for executables in parent paths if the service path has spaces and no quotesWeak service permissionsUser can modify service binary or its configurationAlwaysInstallElevatedMSI packages install with SYSTEM privilegesWritable PATH directoriesPlace a malicious binary earlier in the PATH than a legitimate oneMisconfigured ACLsIncorrect NTFS permissions on sensitive files or registry keys

        B. Credential-Based Escalation
        
Credentials discovered during enumeration can directly provide higher-privileged access.

Password reuse — credentials found in a config file may work on other accounts or systems
Exposed credentials — plaintext passwords in environment variables, bash history, or unattended install files
Service account weaknesses — service accounts may have domain-level privileges or weak/default passwords
Pass-the-Hash (PtH) — on Windows, NTLM password hashes can sometimes be used directly without cracking
Kerberoasting — requesting service tickets for domain accounts and cracking their hashes offline (Active Directory environments)

        C. Software Weaknesses

Vulnerable installed software provides code-execution opportunities that can lead to privilege escalation.

Vulnerable applications — third-party software running as root or SYSTEM with known CVEs
Outdated software — software that has not been patched against known vulnerabilities
Third-party component weaknesses — libraries and dependencies with security flaws

Example: A web server running as root with a Remote Code Execution (RCE) vulnerability directly yields a root shell.
D. Operating System Weaknesses
Kernel-level vulnerabilities allow an unprivileged user to execute code in the kernel context, granting complete control over the system.
Notable Linux Kernel Exploits:
CVENameAffected VersionsDescriptionCVE-2016-5195Dirty CowLinux ≤ 4.8.3Race condition in memory-management subsystem allowing privilege escalationCVE-2022-0847Dirty PipeLinux 5.8 – 5.16.11Overwrite read-only files via pipe, including /etc/passwdCVE-2021-4034PwnKitAll Linux distros (polkit)Heap memory corruption in pkexecCVE-2019-14287Sudo bypasssudo < 1.8.28Run commands as root by specifying UID -1
Notable Windows Escalation CVEs:
CVENameDescriptionCVE-2021-34527PrintNightmareRemote/local code execution via Windows Print SpoolerCVE-2020-1472ZeroLogonDomain controller compromise via Netlogon protocolCVE-2019-0708BlueKeepRemote Desktop Protocol vulnerability allowing RCECVE-2021-1675PrintNightmare (variant)Print Spooler privilege escalation
E. Application-Level Escalation
Applications themselves can be escalation vectors, independent of the operating system.

Insecure application permissions — applications running with excessive privileges relative to their function
Trust relationships — applications that implicitly trust input from certain paths, users, or systems
Misconfigured administrative interfaces — database admin panels, web management interfaces, or APIs running as privileged users without proper authentication


        3.3 Platform-Specific Escalation Paths

Linux Escalation Summary

Initial Access (low-privilege shell)
        │
        ├── Check sudo -l → GTFOBins abuse
        ├── Find SUID binaries → GTFOBins / custom exploit
        ├── Check cron jobs → writable script replacement
        ├── Check kernel version → public exploit (DirtyCow, DirtyPipe)
        ├── Find credentials → SSH keys, config files, bash history
        ├── Check special group membership → docker, lxd, disk
        └── Check capabilities → cap_setuid, cap_net_raw abuse
                │
                └── root
Windows Escalation Summary
Initial Access (low-privilege shell)
        │
        ├── whoami /priv → SeImpersonatePrivilege → Potato Attacks
        ├── Unquoted service paths → malicious binary in path
        ├── Weak service permissions → replace/modify service binary
        ├── AlwaysInstallElevated → malicious .msi package
        ├── SAM/LSASS → credential dumping with Mimikatz
        ├── Scheduled tasks → writable task scripts
        ├── DLL hijacking → replace missing DLL loaded by privileged app
        └── Token impersonation → impersonate higher-privilege token
                │
                └── SYSTEM / Administrator

        4. Tools Reference

Enumeration Tools

ToolPlatformUse CaseLinkLinPEASLinuxFull automated local enumerationPEASS-ngWinPEASWindowsFull automated local enumerationPEASS-ngLinEnumLinuxLightweight enumeration scriptrebootuser/LinEnumPowerUpWindowsPowerShell-based misconfiguration checksPowerSploitSeatbeltWindowsC# host enumerationGhostPack/Seatbeltlinux-exploit-suggesterLinuxSuggests kernel exploits based on versionmzet-/linux-exploit-suggesterGTFOBinsLinuxUnix binary abuse for escalationgtfobins.github.ioLOLBASWindowsLiving off the land binary abuselolbas-project.github.io
Exploitation & Credential Tools
ToolPlatformUse CaseMimikatzWindowsCredential dumping from LSASS, pass-the-hashMetasploitMultiExploit framework with post-exploitation modulesBloodHoundADActive Directory attack path visualizationCrackMapExecWindows/ADNetwork authentication and lateral movementImpacketMultiPython suite for network protocol attacks

6. Defensive Considerations

Understanding privilege escalation from an offensive perspective directly informs defensive strategy. Key hardening measures include:
Principle of Least Privilege

Every user account and service account should have only the minimum permissions necessary
Regularly audit sudoers files and Windows ACLs
Remove users from privileged groups (docker, lxd, sudo) unless required

Patch Management

Apply kernel and OS patches promptly — many public exploits target known, patched vulnerabilities
Monitor CVEs relevant to your software stack
Use automated patch management systems for consistency

Service Hardening

Run services as dedicated low-privilege service accounts
Quote all service paths on Windows
Set NoNewPrivileges=yes in Linux systemd unit files where applicable
Restrict file permissions on service executables and configuration files

Credential Hygiene

Never store plaintext credentials in configuration files, environment variables, or scripts
Rotate service account passwords regularly
Use secret management solutions (HashiCorp Vault, AWS Secrets Manager)
Disable NTLM where possible; enforce Kerberos

Monitoring and Detection

Log privilege use events (sudo usage, token creation, UAC bypass attempts)
Deploy EDR solutions capable of detecting common escalation tools (WinPEAS, Mimikatz)
Alert on SUID binary execution and unexpected process privilege changes
Monitor for creation of new admin accounts or group membership changes


6. Further Resources
Learning Platforms

TryHackMe — tryhackme.com — guided labs on privilege escalation
HackTheBox — hackthebox.com — CTF-style machines with real escalation paths
VulnHub — vulnhub.com — downloadable vulnerable VMs

References

MITRE ATT&CK — Privilege Escalation (TA0004) — attack.mitre.org
GTFOBins — gtfobins.github.io
HackTricks — book.hacktricks.xyz — comprehensive pentesting wiki
PayloadsAllTheThings — github.com/swisskyrepo/PayloadsAllTheThings

Books

Privilege Escalation Techniques — Alexis Ahmed (Packt Publishing)
The Hacker Playbook 3 — Peter Kim
Penetration Testing — Georgia Weidman
