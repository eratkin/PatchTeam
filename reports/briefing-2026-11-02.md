# Weekly Patch Briefing - 2026-11-02

*Data source: live CISA KEV feed (catalog version 2026.10.30)*  
*Tech stack watched: microsoft*

| Tier | Count |
|---|---|
| 🔴 PATCH NOW | 0 |
| 🟠 THIS WEEK | 6 |
| 🟡 WATCH | 27 |

## 🟠 THIS WEEK

### CVE-2026-96951 - Microsoft Windows (score 55)
**Microsoft Windows Command Injection Vulnerability**  
Microsoft Windows Shell contains a command injection vulnerability that allows an unauthorized attacker to bypass a security feature over a network.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-16

Why it ranked here:
- Actively exploited in the wild (+10)
- Vendor/product is in YOUR tech stack (+30)
- Government patch deadline passed 17 days ago (+15)

### CVE-2026-97229 - GitLab Community Edition and Enterprise Edition (score 40)
**GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability**  
GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-01

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2026-76418 - Cisco Secure Firewall ASA Software and Cisco Secure FTD Software (score 40)
**Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability**  
Cisco Secure Firewall ASA Software and Cisco Secure FTD Software contains an unchecked return value to NULL pointer dereference vulnerability that could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-01

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2026-46300 - Linux Kernel (score 40)
**Linux Kernel Missing Initialization of a Variable Vulnerability**  
Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. This vulnerability can be chained with CVE-2026-109618 and CVE-2026-109619 to implant PHP webshells and run commands as root.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-31

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 2 days ago (+15)

### CVE-2026-109618 - PHP Group PHP (score 40)
**PHP Memory Corruption Vulnerability**  
PHP contains an out-of-memory corruption vulnerability that allows for unauthenticated remote code execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-29

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 4 days ago (+15)

### CVE-2026-109619 - PHP Group PHP (score 40)
**PHP Stale Internal Request-State Vulnerability**  
PHP contains a stale internal request-state vulnerability that allows for unauthenticated remote code execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-29

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 4 days ago (+15)

## 🟡 WATCH

### CVE-2026-111357 - Ivanti Connect Secure (score 35)
**Ivanti Connect Secure Missing Authentication for Critical Function Vulnerability**  
Ivanti Connect Secure contains a missing authentication for critical function vulnerability that could allow a local authenticated attacker to escalate their privileges. This vulnerability can be chained with CVE-2026-104935 and CVE-2026-118527.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-02

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 0 days (+10)

### CVE-2026-118527 - Ivanti Connect Secure (score 25)
**Ivanti Connect Secure Generation of Predictable Numbers or Identifiers Vulnerability**  
Ivanti Connect Secure contains a generation of predictable numbers or identifiers vulnerability that allows a remote authenticated attacker to upload files with attacker-controlled content to a known location on disk. This vulnerability can be chained with CVE-2026-104935 and CVE-2026-111357.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-13

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-41709 - Broadcom VMware ESX (score 25)
**Broadcom VMWare ESX Insufficient Logging Vulnerability**  
Broadcom VMWare ESX contains an insufficient logging vulnerability that could allow a malicious actor with admin access to perform certain operations without being logged.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-11

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-48356 - Adobe Commerce and Magento (score 25)
**Adobe Commerce and Magento Unrestricted Upload of File with Dangerous Type Vulnerability**  
Adobe Commerce and Magento contain an unrestricted upload of file with dangerous type vulnerability that could result in arbitrary code execution in the context of the current user, potentially gaining elevated access or control over the victim's account or session.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-10

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-111497 - Google Brotli (score 25)
**Google Brotli Unchecked Return Value Vulnerability**  
Google Brotli contains an unchecked return value vulnerability that allows a remote unauthenticated attacker to corrupt adjacent decoder state memory, disclose sensitive memory contents, cause a denial of service, or potentially execute arbitrary code using a crafted Brotli-compressed stream.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-10

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-114625 - Arista VeloCloud Orchestrator (score 25)
**Arista VeloCloud Orchestrator SQL Injection Vulnerability**  
Arista VeloCloud Orchestrator on-prem contains a SQL injection vulnerability that may allow a remote attacker to access privileged internal functionality and impact the VCO host. Successful exploitation may compromise the confidentiality, integrity, and availability of the orchestrator and data managed by the orchestrator.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-26

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-110447 - Collabora Collabora Online – Built-in CODE Server (score 25)
**Collabora Online – Built-in CODE Server OS Command Injection Vulnerability**  
Collabora Collabora Online – Built-in CODE Server when used within the NextCloud platform contains an OS command injection vulnerability that allows for remote code execution when the CODE server isn't running.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-26

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-106931 - EG Secure Solutions SiteGuard Server Edition (score 25)
**EG Secure Solutions SiteGuard Server Edition OS Command Injection Vulnerability**  
EG Secure Solutions SiteGuard Server Edition contains an OS command injection vulnerability which may allow an attacker to execute arbitrary OS commands with root or SYSTEM privileges on the system running the affected product.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-23

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 10 days ago (+15)

### CVE-2026-96656 - Plex Media Server (score 25)
**Plex Media Server External Control of File Name or Path Vulnerability**  
Plex Media Server contains an external control of file name or path vulnerability which can allow an admin user to write arbitrary files that may be executed on load. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96654, and CVE-2026-96655.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-23

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 10 days ago (+15)

### CVE-2026-96654 - Plex Media Server (score 25)
**Plex Media Server Improper Neutralization of Encoded URI Schemes in a Web Page Vulnerability**  
Plex Media Server contains an improper neutralization of encoded URI schemes in a web page vulnerability that could allow an attacker to call other plugins' functions and supply their own parameters. This vulnerability can be chained with CVE-2026-96652, CVE-2026-96655, and CVE-2026-96656.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-23

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 10 days ago (+15)
