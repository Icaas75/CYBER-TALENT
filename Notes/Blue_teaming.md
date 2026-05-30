BLUE TEAMING

Research

    1)log types
    2)what, when, how,where, who, why
    3)SOC, IR, CTI
    4)Log analysis

Answer

1) Core Log Types

       Authentication Logs: Track login success, failures, and privilege changes.
       Application Logs: Record software-specific events, errors, and user activities.
       Operating System Logs: Capture system events, service starts, and crashes.
       Network Logs: Detail traffic flows, bandwidth usage, and connections.
       Firewall Logs: Document blocked and allowed traffic at perimeters.
       IDS/IPS Logs: Alert on malicious traffic patterns and signatures.
       Proxy/Web Logs: Track URLs visited and web request methods.
       EDR Logs: Monitor endpoint process execution and file modifications.
       Cloud Logs: Audit API calls and cloud resource changes.

2) The 6 Framework Questions

       What: The specific action or event that occurred.
       When: The exact timestamp of the recorded activity.
       How: The mechanism, tool, or protocol used.
       Where: The source, destination, or affected system.
       Who: The user account, IP address, or process identity.
       Why: The attacker's objective, such as exfiltration.

3) Defensive Pillars: SOC, IR, & CTI

Cyber Threat Intelligence (CTI)

        Researches adversary tactics and tools.
        Collects indicators of compromise (IoCs).
        Feeds data into SOC monitoring systems.

Security Operations Center (SOC)

        Monitors security alerts around the clock.
        Triage alerts to filter false positives.
        Escalates confirmed threats to responders.

Incident Response (IR)

        Contains active threats to limit damage.
        Eradicates malicious presence from systems.
        Recovers operations back to normal states.

Log Analysis Process

1. Format and Parse

       Convert text: Import raw log data into a readable layout.
       Identify fields: Map out timestamps, IP addresses, usernames, and action codes.
       Apply JSON/CSV tooling: Use tools like CyberChef, Excel, or SIEM parsers to organize columns.

2. Establish Time Context

       Check time zones: Verify if logs use UTC, local time, or epoch format.
       Synchronize clocks: Align timestamps from different servers to prevent chronological errors.
       Sort chronologically: Order events from oldest to newest to read the story sequentially.

3. Filter and Reduce Noise

       Remove known good: Filter out routine automated tasks like daily backups or health checks.
       Deduplicate: Group identical, repetitive entries (e.g., 500 failed logins in one minute).
       Isolate anomalies: Focus on rare processes, unusual hours, or spikes in traffic volume.

4. Ask the 6 Framework Questions

5. Correlate Across Sources

       Pivot on identifiers: Take a suspicious IP from firewall logs and search for it in web proxy logs.
       Link identities: Match a temporary DHCP IP address to a physical host MAC address and a user account.
       Verify effects: Check if a network alert resulted in a file creation log on the target endpoint.

4) Log Analysis Methodology

        Collection: Gathering logs centrally via tools like SIEM.
        Normalization: Parsing different formats into standard fields.
        Correlation: Linking related events across distinct log sources.
        Baselining: Learning normal behavior to spot anomalies.
        Searching: Querying data using logic and regex patterns.
        Visualization: Mapping data into dashboards to spot trends.
