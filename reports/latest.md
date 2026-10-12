# Weekly Patch Briefing - 2026-10-12

*Data source: live CISA KEV feed (catalog version 2026.10.08)*  
*Tech stack watched: microsoft*

| Tier | Count |
|---|---|
| 🔴 PATCH NOW | 0 |
| 🟠 THIS WEEK | 6 |
| 🟡 WATCH | 24 |

## 🟠 THIS WEEK

### CVE-2026-65660 - Microsoft SharePoint (score 55)
**Microsoft SharePoint Code Injection Vulnerability**  
Microsoft SharePoint contains a code injection vulnerability which could allow an authorized attacker to execute code over a network.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-28

Why it ranked here:
- Actively exploited in the wild (+10)
- Vendor/product is in YOUR tech stack (+30)
- Government patch deadline passed 14 days ago (+15)

### CVE-2015-5477 - ISC BIND (score 40)
** ISC BIND Data Processing Errors Vulnerability**  
ISC BIND contains a data processing errors vulnerability that could allow remote attackers to cause a denial of service via TKEY queries.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-11

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2016-3081 - Apache Struts (score 40)
**Apache Struts Command Injection Vulnerability**  
Apache Struts contains a command injection vulnerability that could allow remote attackers to execute arbitrary code via method:prefix when Dynamic Method Invocation is enabled.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-11

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2023-22894 - Strapi Strapi (score 40)
**Strapi Cleartext Storage of Sensitive Information Vulnerability**  
Strapi contains a cleartext storage of sensitive information vulnerability that could allow attackers with access to the admin panel to discover sensitive user details via the query filter. The impacted product(s) could be end-of-life (EoL) and/or end-of-service (EoS). Users are advised to discontinue use and/or transition to a supported version. This vulnerability can be chained with CVE-2023-22621 to achieve remote code execution. 

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-11

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2021-3199 - ONLYOFFICE Docs (score 40)
**ONLYOFFICE Docs Server Path Traversal Vulnerability**  
ONLYOFFICE Docs contains a path traversal vulnerability that can occur when JWT is used, via a /.. sequence in an image upload parameter and could allow for remote code execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-11

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

### CVE-2015-3306 - ProFTPD ProFTPD (score 40)
**ProFTPD Improper Access Control Vulnerability**  
ProFTPD contains an improper access control vulnerability that could allow remote attackers to read and write to arbitrary files via the site cpfr and site cpto commands.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-11

Why it ranked here:
- Actively exploited in the wild (+10)
- Added to the catalog in the last 7 days (+15)
- Government patch deadline passed 1 days ago (+15)

## 🟡 WATCH

### CVE-2026-88779 - Citrix NetScaler (score 25)
**Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability**  
Citrix NetScaler ADC (formerly Citrix ADC) and Citrix NetScaler Gateway (formerly Citrix Gateway) contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for a denial of service.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-07

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 5 days ago (+15)

### CVE-2026-102490 - Zammad GmbH Zammad (score 25)
**Zammad GmbH Zammad Improper Privilege Management Vulnerability**  
Zammad GmbH Zammad contains an improper privilege management vulnerability that can allow the local zammad user to escalate privileges to root. This vulnerability can be chained with CVE-2026-102489.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-05

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-102489 - Zammad GmbH Zammad (score 25)
**Zammad GmbH Zammad Session Fixation Vulnerability**  
Zammad GmbH Zammad contains a session fixation vulnerability that can lead to remote code execution as the zammad user. This vulnerability can be chained with CVE-2026-102490.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-05

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 7 days ago (+15)

### CVE-2026-104286 - Fortinet FortiMail (score 25)
**Fortinet FortiMail Path Traversal Vulnerability**  
Fortinet FortiMail contains a path traversal and an improper neutralization of NULL byte or NULL character vulnerability that may allow an unauthenticated attacker to write arbitrary files on the underlying system via crafted HTTP or HTTPS requests.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-04

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 8 days ago (+15)

### CVE-2026-76504 - Cisco Catalyst SD-WAN Manager (score 25)
**Cisco Catalyst SD-WAN Manager Hex Encoding Vulnerability**  
Cisco Catalyst SD-WAN Manager contains a hex encoding vulnerability that could allow an unauthenticated, remote attacker to access an affected system with privileges of the admin user due to improper handling of URI encoding in an HTTP request.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-10-03

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 9 days ago (+15)

### CVE-2026-88772 - Citrix NetScaler (score 25)
**Citrix NetScaler Improper Restriction of Operations within the Bounds of a Memory Buffer Vulnerability**  
Citrix NetScaler ADC and NetScaler Gateway contain an improper restriction of operations within the bounds of a memory buffer vulnerability that could allow for remote code execution or denial of service

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-30

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 12 days ago (+15)

### CVE-2026-88771 - Citrix NetScaler (score 25)
**Citrix NetScaler Improper Input Validation Vulnerability**  
Citrix NetScaler ADC and NetScaler Gateway contain an improper input validation vulnerability that could allow an unauthenticated attacker to execute arbitrary commands.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-30

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 12 days ago (+15)

### CVE-2026-67279 - MikroTik RouterOS (score 25)
**Mikrotik RouterOS Improper Enforcement of Behavioral Workflow Vulnerability**  
Mikrotik RouterOS contains an improper enforcement of behavioral workflow vulnerability that could allow an unauthenticated client to open a session channel and send an exec request. This vulnerability can be chained to achieve unauthenticated exploitation of CVE-2026-86060.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-28

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 14 days ago (+15)

### CVE-2026-87902 - WordPress Core (score 25)
**WordPress Core Remote File Inclusion Vulnerability**  
WordPress Core contains a remote file inclusion vulnerability which could allow an unauthenticated attacker to make page-template resolution include a chosen readable local `.php` file outside the active theme directories, leading to remote code execution.

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-28

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 14 days ago (+15)

### CVE-2026-5430 - WSO2 Multiple Products (score 25)
**WSO2 Multiple Products Path Traversal Vulnerability **  
WSO2 API Control Plane, API Manager, Traffic Manager & Universal Gateway contain a path traversal vulnerability that could allow for unrestricted file upload and lead to remote code execution. 

**What to do:** Apply mitigations in accordance with vendor instructions, ensuring compliance with CISA’s BOD 26-04 Prioritizing Security Updates Based on Risk (see URL in Notes) guidance and CISA’s “Forensics Triage Requirements” (see URL in Notes). Follow applicable BOD 26-04 guidance for cloud services or discontinue use of the product if mitigations are unavailable. Stakeholders are responsible for evaluating each asset's internet exposure and ensuring adherence to BOD 26-04 patching guidelines.  
**Deadline (CISA):** 2026-09-27

Why it ranked here:
- Actively exploited in the wild (+10)
- Government patch deadline passed 15 days ago (+15)
