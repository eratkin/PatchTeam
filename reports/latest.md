# Weekly Patch Briefing - 2026-09-29

*Data source: live CISA KEV feed (catalog version 2026.09.29)*  
*Tech stack watched: microsoft*

| Tier | Count |
|---|---|
| 🔴 PATCH NOW | 1 |
| 🟠 THIS WEEK | 10 |
| 🟡 WATCH | 33 |

## 🔴 PATCH NOW

### CVE-2026-65660 - Microsoft SharePoint (score 70)
**Microsoft SharePoint Code Injection Vulnerability**  
Microsoft SharePoint contains a code injection vulnerability which could allow an authorized attacker to execute code over a network.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-28

Why it ranked here:
- Actively exploited in the wild (+10)
- Vendor/product is in YOUR tech stack (+30)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

## 🟠 THIS WEEK

### CVE-2026-81963 - Microsoft Windows (score 55)
**Microsoft Windows Link Following Vulnerability**  
Microsoft Windows Update Stack contains a link following vulnerability that allows a local attacker to escalate privileges locally up to SYSTEM.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-22

Why it ranked here:
- Actively exploited in the wild (+10)
- Vendor/product is in YOUR tech stack (+30)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-85880 - Microsoft Windows (score 55)
**Microsoft Windows Heap-Based Buffer Overflow Vulnerability**  
Microsoft Windows Advanced Local Procedure Call contains a heap-based buffer overflow vulnerability that allows an attacker to elevate privileges locally.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-22

Why it ranked here:
- Actively exploited in the wild (+10)
- Vendor/product is in YOUR tech stack (+30)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-67279 - MikroTik RouterOS (score 40)
**Mikrotik RouterOS Improper Enforcement of Behavioral Workflow Vulnerability**  
Mikrotik RouterOS contains an improper enforcement of behavioral workflow vulnerability that could allow an unauthenticated client to open a session channel and send an exec request. This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-28

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2026-87902 - WordPress Core (score 40)
**WordPress Core Remote File Inclusion Vulnerability**  
WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-28

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2026-5430 - WSO2 Multiple Products (score 40)
**WSO2 Multiple Products Path Traversal Vulnerability **  
WSO2 API Control Plane, API Manager, Traffic Manager & Universal Gateway contain a path traversal vulnerability that could allow for unrestricted file upload and lead to remote code execution. 

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-27

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 2 days ago (+15)

### CVE-2026-71362 - Adobe Commerce and Magento  (score 40)
**Adobe Commerce and Magento Incorrect Authorization Vulnerability **  
Adobe Commerce and Magento contains an incorrect authorization vulnerability that could allow an attacker to leverage this vulnerability to gain elevated access to sensitive resources without any user interaction. 

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-27

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 2 days ago (+15)

### CVE-2026-93952 - Arista VeloCloud Orchestrator (score 40)
**Arista VeloCloud Orchestrator Improper Input Validation Vulnerability**  
Arista VeloCloud Orchestrator (VCO) on-prem contains an improper input validation vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-25

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 4 days ago (+15)

### CVE-2026-94127 - F5 BIG-IP APM (score 40)
**F5 BIG-IP APM Heap-based Buffer Overflow Vulnerability**  
F5 BIG-IP APM contains a heap-based buffer overflow vulnerability when access policy and an OAuth profile are configured on a virtual server. This vulnerability could allow an unauthenticated attacker to perform remote code execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-25

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 4 days ago (+15)

### CVE-2026-93616 - Check Point Multiple Products (score 40)
**Check Point Multiple Products Path Traversal Vulnerability**  
Check Point Security Management Server, Multi-Domain Security Management Server, Log Server, Multi-Domain Log Server, and SmartEvent contain a path traversal vulnerability that allows an unauthenticated attacker to upload and execute arbitrary scripts.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-25

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 4 days ago (+15)

### CVE-2026-85102 - Check Point Multiple Products (score 40)
**Check Point Multiple Products Improper Certificate Validation Vulnerability**  
Check Point Security Gateway and Check Point Spark Firewall using Site to Site VPN or Remote Access VPN contain an improper certificate validation vulnerability which could allow an unauthenticated remote attacker to execute arbitrary code on the Gateway.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-25

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 4 days ago (+15)

## 🟡 WATCH

### CVE-2026-86950 - Apple Multiple Products (score 35)
**Apple Multiple Products Out-of-Bounds Write Vulnerability**  
Apple iOS, macOS, and iPadOS contain an out-of-bounds write vulnerability in CoreGraphics that may lead to arbitrary code execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-02

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 3 days (+10)

### CVE-2026-88772 - Citrix NetScaler (score 35)
**Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability**  
Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-30

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 1 days (+10)

### CVE-2026-88771 - Citrix NetScaler (score 35)
**Citrix NetScaler Improper Input Validation Vulnerability**  
Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-30

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 1 days (+10)

### CVE-2026-7273 - Zyxel GS1900 Series Switches (score 25)
**Zyxel GS1900 Series Switches Stack-Based Buffer Overflow Vulnerability**  
Zyxel GS1900 series switches contain a stack-based buffer overflow vulnerability in the CGI program which could allow a LAN-based, unauthenticated attacker to exploit the flaw and potentially execute OS commands via a crafted HTTP request.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-24

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 5 days ago (+15)

### CVE-2025-39964 - Linux Kernel (score 25)
**Linux Kernel Race Condition Vulnerability**  
Linux Kernel contains a race condition vulnerability which allows concurrent writes to the same AF_ALG socket causing data to be unpredictably interleaved and creating inconsistencies in the socket's internal state.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-21

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 8 days ago (+15)

### CVE-2026-53266 - Linux Kernel (score 25)
**Linux Kernel Out-of-Bounds Write Vulnerability**  
Linux Kernel contains an out-of-bounds write vulnerability in the ebtables SNAT target which allows an ARP sender hardware address rewrite to write directly into a nonlinear socket-buffer fragment backed by a splice-imported file page. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-21

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 8 days ago (+15)

### CVE-2025-39682 - Linux Kernel (score 25)
**Linux Kernel Improper Check for Unusual or Exceptional Conditions Vulnerability**  
Linux Kernel contains an improper check for unusual or exceptional conditions vulnerability in the TLS receive path which allows a zero-length record retrieved from the rx_list to bypass the intended recvmsg() record-type handling, potentially causing subsequent TLS records to be processed using incorrect zero-copy and queuing assumptions. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-21

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 8 days ago (+15)

### CVE-2026-58704 - Google Pixel (score 25)
**Google Pixel Improper Authorization Vulnerability**  
Google Pixel devices contain an improper authorization vulnerability in the cellular modem. A logic error may allow an attacker to bypass permission checks and escalate privileges.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-19

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 10 days ago (+15)

### CVE-2026-76460 - Cisco Identity Services Engine (score 25)
**Cisco Identity Services Engine Incorrect Use of Privileged APIs Vulnerability**  
Cisco Identity Services Engine (ISE) and Cisco ISE Passive Identity Connector (ISE-PIC) contain an incorrect use of privileged APIs vulnerability that could allow an unauthenticated, remote attacker to gain unauthorized access to the affected device by bypassing the web-based management interface.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-19

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 10 days ago (+15)

### CVE-2026-87886 - Acronis Backup (score 25)
**Acronis Backup Incorrect Default Permissions Vulnerability**  
Acronis Backup plugin for cPanel & WHM and extension for Plesk contains an incorrect default permissions vulnerability that could allow for privilege escalation.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-19

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 10 days ago (+15)
