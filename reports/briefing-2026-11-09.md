# Weekly Patch Briefing - 2026-11-09

*Data source: live CISA KEV feed (catalog version 2026.11.09)*  
*Tech stack watched: microsoft*

| Tier | Count |
|---|---|
| 🔴 PATCH NOW | 0 |
| 🟠 THIS WEEK | 2 |
| 🟡 WATCH | 32 |

## 🟠 THIS WEEK

### CVE-2026-96951 - Microsoft Windows (score 55)
**Microsoft Windows Command Injection Vulnerability**  
Microsoft Windows Shell contains a command injection vulnerability that allows an unauthorized attacker to bypass a security feature over a network.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-16

Why it ranked here:
- Actively exploited in the wild (+10)
- Vendor/product is in YOUR tech stack (+30)
- Government patch deadline passed 24 days ago (+15)

### CVE-2026-119977 - WordPress WordPress Core (score 40)
**WordPress WordPress Core Time-of-check Time-of-use (TOCTOU) Race Condition Vulnerability**  
WordPress WordPress Core contains a time-of-check time-of-use (TOCTOU) race condition vulnerability that could allow unauthenticated attackers to execute code on the server during the upgrade window. This is due to predictable, web-accessible staging paths used during full-package core upgrades.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-06

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 3 days ago (+15)

## 🟡 WATCH

### CVE-2026-102895 - GPUStack GPUStack (score 35)
**GPUStack Improper Authentication Vulnerability**  
GPUStack contains an improper authentication vulnerability which could allow unauthenticated administrative access, including user and model changes, persistent administrator API-key creation, disclosure of worker and cloud-provider secrets, and code execution through POST /v2/inference-backends/from-yaml.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-12

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 3 days (+10)

### CVE-2026-123158 - OpenBSD OpenSSH (score 35)
**OpenBSD OpenSSH Unexpected Status Code or Return Value Vulnerability**  
OpenBSD OpenSSH on Linux contains an unexpected status code or return value vulnerability that could allow for authentication bypass.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-12

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 3 days (+10)

### CVE-2026-116779 - SignalWire FreeSwitch (score 35)
**SignalWire FreeSwitch Code Injection Vulnerability**  
SignalWire FreeSwitch contains a code injection vulnerability that permits configuration and credential disclosure, arbitrary call control, and command execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-12

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 3 days (+10)

### CVE-2026-123218 - IBM Aspera Faspex (score 35)
**IBM Aspera Faspex Incorrect Authorization Vulnerability**  
IBM Aspera Faspex contains an incorrect authorization vulnerability that could allow an authenticated user to craft a specific message to bypass authorization, causing privilege escalations.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-12

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline in 3 days (+10)

### CVE-2026-19868 - SonicWall SonicOS SSLVPN (score 25)
**SonicWall SonicOS SSLVPN Use of Single-factor Authentication Vulnerability**  
SonicWall SonicOS SSLVPN contains a use of single-factor authentication vulnerability that may allow a user with valid credentials for an alternate authentication method to bypass SAML authentication controls. Successful exploitation may also bypass SAML-enforced multi-factor authentication (MFA).

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-20

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2024-27834 - Apple Multiple Products (score 25)
**Apple Multiple Products Improper Authentication Vulnerability**  
Apple iOS, iPadOS, macOS, Safari, tvOS and watchOS 10.5 contain an improper authentication vulnerability which could allow an attacker with arbitrary read and write capability to bypass pointer authentication.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-18

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)

### CVE-2026-111357 - Ivanti Connect Secure (score 25)
**Ivanti Connect Secure Missing Authentication for Critical Function Vulnerability**  
Ivanti Connect Secure contains a missing authentication for critical function vulnerability that could allow a local authenticated attacker to escalate their privileges. This vulnerability can be chained with CVE-2026-104935 and CVE-2026-118527.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-02

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-97229 - GitLab Community Edition and Enterprise Edition (score 25)
**GitLab Community Edition and Enterprise Edition Integer Overflow or Wraparound Vulnerability**  
GitLab Community Edition and Enterprise Edition contain a integer overflow or wraparound vulnerability that could allow an unauthenticated user to execute arbitrary code on the GitLab server via a specially crafted regular expression in a CI/CD configuration, due to insufficient regular expression validation.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-01

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 8 days ago (+15)

### CVE-2026-76418 - Cisco Secure Firewall ASA Software and Cisco Secure FTD Software (score 25)
**Cisco Secure Firewall ASA Software and Cisco Secure FTD Software Unchecked Return Value to NULL Pointer Dereference Vulnerability**  
Cisco Secure Firewall ASA Software and Cisco Secure FTD Software contains an unchecked return value to NULL pointer dereference vulnerability that could allow an unauthenticated, remote attacker to cause the device to reload unexpectedly, resulting in a denial of service (DoS) condition.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-11-01

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 8 days ago (+15)

### CVE-2026-46300 - Linux Kernel (score 25)
**Linux Kernel Missing Initialization of a Variable Vulnerability**  
Linux Kernel contains a missing initialization of a variable vulnerability that could allow for unintended modification of page-cache-backed data via failure to preserve the shared-fragment marker during socket buffer coalescing, causing ESP input processing to decrypt shared fragments in place. This vulnerability can be chained with CVE-2026-109618 and CVE-2026-109619 to implant PHP webshells and run commands as root.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-31

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 9 days ago (+15)
