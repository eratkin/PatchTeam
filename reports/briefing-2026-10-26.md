# Weekly Patch Briefing - 2026-10-26

*Data source: live CISA KEV feed (catalog version 2026.10.23)*  
*Tech stack watched: microsoft*

| Tier | Count |
|---|---|
| 🔴 PATCH NOW | 0 |
| 🟠 THIS WEEK | 4 |
| 🟡 WATCH | 26 |

## 🟠 THIS WEEK

### CVE-2026-96951 - Microsoft Windows (score 55)
**Microsoft Windows Command Injection Vulnerability**  
Microsoft Windows Shell contains a command injection vulnerability that allows an unauthorized attacker to bypass a security feature over a network.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-16

Why it ranked here:
- Actively exploited in the wild (+10)
- Vendor/product is in YOUR tech stack (+30)
- Government patch deadline passed 10 days ago (+15)

### CVE-2026-106931 - EG Secure Solutions SiteGuard Server Edition (score 40)
**EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability**  
EG Secure Solutions SiteGuard Server Edition contains an OS command injection vulnerability which may allow an attacker to execute arbitrary OS commands with root or SYSTEM privileges on the system running the affected product.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-23

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 3 days ago (+15)

### CVE-2026-96656 - Plex Media Server (score 40)
**Plex Media Server External Control of File Name or Path Vulnerability**  
Plex Media Server contains an external control of file name or path vulnerability which can allow an admin user to write arbitrary files that may be executed on load. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96654, and CVE-2026-96655.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-23

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 3 days ago (+15)

### CVE-2026-96654 - Plex Media Server (score 40)
**Plex Media Server Improper Neutralization of Encoded URI Schemes in a Web Page Vulnerability**  
Plex Media Server contains an improper neutralization of encoded URI schemes in a web page vulnerability that could allow an attacker to call other plugins' functions and supply their own parameters. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96655, and CVE-2026-96656.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-23

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 3 days ago (+15)

## 🟡 WATCH

### CVE-2026-114625 - Arista VeloCloud Orchestrator (score 35)
**Arista VeloCloud Orchestrator SQL Injection Vulnerability**  
Arista VeloCloud Orchestrator on-prem contains a SQL injection vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-26

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 0 days (+10)

### CVE-2026-110447 - Collabora Collabora Online – Built-in CODE Server (score 35)
**Collabora Online – Built-in CODE Server OS Command Injection Vulnerability**  
Collabora Collabora Online – Built-in CODE Server when used within the NextCloud platform contains an OS command injection vulnerability that allows for remote code execution when the CODE server isn't running.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-26

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 0 days (+10)

### CVE-2026-96655 - Plex Media Server (score 25)
**Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability**  
Plex Media Server contains a server-side request forgery (SSRF) vulnerability that could allow an authenticated user to request arbitrary internal or external addresses via the '/video/:/transcode/universal' path parameter. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96654, and CVE-2026-96656.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-03

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-96652 - Plex Media Server (score 25)
**Plex Media Server Server-Side Request Forgery (SSRF) Vulnerability**  
Plex Media Server contains a server-side request forgery (SSRF) vulnerability which could allow an attacker using any X-Plex-Token value to include a full URL in the 'protocol' parameter and force the Plex server to POST to the attacker's chosen destination. This vulnerability can be chained with CVE-2026-96654, CVE-2026-96655, and CVE-2026-96656. 

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-03

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-110936 - Siemens Software Center (score 25)
**Siemens Software Center Uncontrolled Search Path Element Vulnerability**  
Siemens Software Center contains an uncontrolled search path element vulnerability that could allow an authenticated local attacker to place a specially crafted DLL in a directory that the application searches, leading to arbitrary code execution with the privileges of the affected application.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-03

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-102764 - BeyondTrust Remote Support (score 25)
**BeyondTrust Remote Support Authentication Bypass by Spoofing Vulnerability**  
BeyondTrust Remote Support contains an authentication bypass by spoofing vulnerability that could allow a remote attacker to perform file operations on the appliance.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-19

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 7 days ago (+15)

### CVE-2025-61624 - Fortinet Multiple Products (score 25)
**Fortinet Multiple Products Path Traversal Vulnerability**  
FortiOS, FortiPAM, FortiProxy, and FortiSwitchManager contain a path traversal vulnerability that may allow an authenticated attacker with admin profile and at least read-write permissions to write or delete arbitrary files via specific CLI commands.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-19

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-21589 - Atlassian Multiple Products (score 25)
**Atlassian Multiple Products Files or Directories Accessible to External Parties Vulnerability**  
Multiple Atlassian products (Bitbucket Data Center ,Confluence Data Center, Jira Service Management Data Center, Jira Software Data Center, Bamboo Data Center, Crowd Data Center, Crucible and Fisheye) contain a files or directories accessible to external parties vulnerability which could allow an unauthenticated attacker to access specific files within the web application root directory in affected versions.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-18

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 8 days ago (+15)

### CVE-2026-105134 - Ahsay AhsayCBS (score 25)
**Ahsay AhsayCBS Command Injection Vulnerability**  
Ahsay AhsayCBS contains a command injection vulnerability that could allow a remote attacker to execute operating system commands via manipulation of the random parameter in the Replication Receiver component’s /rps/api/json/UpdateReceivers.do endpoint. This vulnerability can be chained with CVE-2026-105133.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-17

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 9 days ago (+15)

### CVE-2026-76519 - Cisco Secure Email Gateway (score 25)
**Cisco Secure Email Gateway Relative Path Traversal Vulnerability**  
Cisco Secure Email Gateway contains a relative path traversal vulnerability that could allow an unauthenticated, remote attacker to write arbitrary files on the underlying operating system.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-17

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 9 days ago (+15)
