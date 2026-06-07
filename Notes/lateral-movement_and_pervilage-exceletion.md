# ⬡ VulnCorp Portal — Penetration Testing Report

## Executive Summary
A comprehensive security assessment was conducted against the VulnCorp internal portal infrastructure (`100.31.117.193`), leading to a full infrastructure compromise. By chaining multiple high-severity vulnerabilities, initial access was escalated from an unauthenticated observer to local network administrative access via a pivoted remote machine.

---

## Detailed Flag & Vulnerability Breakdown

### 🛠 Phase 1: Passive & Active Reconnaissance
*   **Vulnerability Type:** Information Disclosure via Metadata & Obscure Routing
*   **Vulnerability Description:** The application leaked administrative paths and debug parameters directly inside public-facing files and HTTP headers.
*   **Exploitation Summary:** Inspecting the public `/robots.txt` directory exposed deprecated administrative naming conventions. Forcing a `404 Not Found` error revealed a custom server debugging token inside the HTTP response headers.
*   **Captured Flags:**
    1.  `FLAG{r3c0n_m4st3r_r0b0ts_txt}` (Discovered inside the `robots.txt` comments)
       
       <img width="718" height="234" alt="pri-exc1" src="https://github.com/user-attachments/assets/b2cff0dc-0b78-47ec-9f9e-9e597a977622" />

    2.  `FLAG{p4ss1v3_r3c0n_m3t4d4t4_l34k}` (Discovered inside the `X-Debug-Token` header)
       
       <img width="1040" height="271" alt="pri-exc2" src="https://github.com/user-attachments/assets/fdd6e6dc-a95e-4136-99a0-e295a240001d" />


### 👤 Phase 2: Authentication Bypass & Horizontal Privilege Escalation
*   **Vulnerability Type:** Insecure Direct Object Reference (IDOR) & SQL Injection (SQLi)
*   **Vulnerability Description:** The `/api/user/<id>` endpoint failed to validate request authorization, leaking profile paths. Concurrently, the login parameter failed to sanitize input characters, allowing database logic manipulation.
*   **Exploitation Summary:** Shifting user IDs exposed user profiles. Utilizing a classic boolean SQL statement (bob'--) bypassed database verification controls, logging into an active employee account.
*   **Captured Flag:**
    3.  `FLAG{sql1_4uth_byp4ss_pwn3d}` (Recovered upon bypassing database auth via Bob's account)
    <img width="902" height="269" alt="pri-exc3(sql)" src="https://github.com/user-attachments/assets/d93e1d36-633d-400d-bbd8-a3e108725998" />


### 🛑 Phase 3: Vertical Privilege Escalation
*   **Vulnerability Type:** Broken Access Control
*   **Vulnerability Description:** The application left unremoved administrative configuration credentials inside user-accessible internal files.
*   **Exploitation Summary:** Inspecting administrative database entries directly exposed restricted network records detailing operational credentials.
*   **Captured Flag:**
    4.  `FLAG{brok3n_4cc3ss_c0ntr0l_0wn3d}` (Found inside the administrative database document keys)
    <img width="872" height="247" alt="pri-exc5(broken-access-control)" src="https://github.com/user-attachments/assets/d96a6eb6-a678-4bfa-8812-76bec17bbbcf" />





### 💉 Phase 4: Server-Side Injection 
*   **Vulnerability Type:** Server-Side Template Injection (SSTI)
*   **Vulnerability Description:** The portal's greeting template engine directly processed raw user data inputs within Jinja2 delimiters without enforcing syntax sandboxing.
*   **Exploitation Summary:** Injecting an `{% include ... %}` directive forced the local template renderer to fetch and output local files directly into the web application UI view.
*   **Captured Flag:**
    5.  `FLAG{5st1_t3mpl4t3_1nj3ct10n_rce}` (Exfiltrated by forcing template rendering of local text records)
    <img width="609" height="445" alt="pri-exc7(ssti)" src="https://github.com/user-attachments/assets/d28f3bef-0502-4ba6-894e-a8705a81c861" />



### 🕵️‍♂️ Phase 5: Client-Side Session Hijacking
*   **Vulnerability Type:** Stored Cross-Site Scripting (XSS)
*   **Vulnerability Description:** The Feedback portal accepted raw HTML/JavaScript inputs and saved them to an administrative overview table without conducting character sanitization.
*   **Exploitation Summary:** A malicious JavaScript snippet was submitted via the feedback forum. When an automated administrator review script loaded the review interface, the script executed, sending the session cookie out-of-band to an external Webhook handler.
*   **Captured Flag:**
    6.  `FLAG{x55_st0r3d_c00k13_st0l3n}` (Hijacked directly from the incoming admin request parameter stream)
    <img width="726" height="224" alt="pri-exc4(admin-cookie)" src="https://github.com/user-attachments/assets/5026bdf5-7c95-48b4-9fea-2c01e8891b17" />



### 📤 Phase 6: Unrestricted File Upload & Remote Code Execution (RCE)
*   **Vulnerability Type:** Arbitrary File Upload via Client-Side Validation Bypass
*   **Vulnerability Description:** The web shell upload module restricted file extensions solely on the client-side browser layer, trusting incoming HTTP POST configurations implicitly on the backend server.
*   **Exploitation Summary:** The upload request was intercepted via a local proxy, swapping out allowed text extensions with a functional arbitrary script handler (`burk.php`). Accessing the file directly provided programmatic control over the operating system layer.
*   **Captured Flags:**
    7.  **Web Shell Upload Access Flag** (Awarded upon bypassing backend upload blocks)
    <img width="891" height="379" alt="pri-exc8(file_upload)" src="https://github.com/user-attachments/assets/a7a9d828-225b-4603-a7b0-e99a675b2357" />


---

## 🔒 Recommended Remediation Steps
1.  **Sanitize Inputs:** Enforce absolute parameter binding across all database queries to mitigate SQL injection vectors.
2.  **Server-Side Verification:** Move all file extension verification from the browser to the backend using MIME-type validation.
3.  **Strict Context Filtering:** Implement strict HTML entity encoding across user comments to render JavaScript dead on the page.
