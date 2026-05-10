# Sigma

<b>Sigma</b> is an open source generic signature language that helps <b>describe behaviour in log events</b>. Indicators of Compromise (IOCs) are <i>artifacts</i> of an attack such as IP addresses, file hashes, or domain names. They are useful but brittle because attackers than easily change an IP or recompile a binary to get a new hash. 

For example, instead of saying "block this IP", a <b>Sigma rule</b> might say "alert when a process spawns Powershell with encoded commands from a Word document". This behavioural pattern is much harder for an attack to trivially change.  

### Gaps Sigma bridges 

Before Sigma, analysts who wrote a detection query in Splunk SPL could not easily share it with someone running Elastic or Microsoft Sentinel as the query languages are completely different. Sigma solves this by: 

1. Writing the detection logic <i>once</i> in a SIEM-agnostic YAML format 
2. Using a <b>converter(sigmac/pySigma)</b> to translate that rule into Splunk SPL, KQL, Elastic Query DSL, QRadar AQL, and many others. 
<hr>

### What is a Signature

A <b>Signature</b> is essentially a <b>pattern or fingerprint that identifies something malicious or suspicious</b>. It is like how a doctor diagnose an illness. A disease has specific symptoms such as a fever, rash or cough; in cybersecurity, a signature is equivalent of those symptoms. 

### Limitation of Signatures 

Signatures only catch <b>KNOWN</b> threats. If an attacker changes their patterns slightly, a signature can be evaded. This is why: 

- Behavioural signatures (like Sigma) are harder to evade than static ones (IPs). 
- Security teams constantly update and refine their signature libraries 
- Signature-based detection is usually paired with anomoly-based detection for better coverage. 

## Important Nuances 

In detection engineering, Sigma is a `amazing starting point`, but it is `not the finished product`. From professionals, open source detections help skip a huge amount of work, where Sigma gets you 80% there, but your team has to finish the last 20%. 

<b>Last 20%</b>

- Integration with your tools 
- Tuning the detection to match environment and reduce false positives 
- Matching business behaviour ("is this activity abnormal for us?")

<b>A Sigma rule might say:</b> Detect PowerShell downloading files from the internet. 

However, in your environment: 

- Developers may do this all day 
- SIEM may store logs differently 
- EDR has better fields 
- Admins use the files legitimately 

You `MUST understand your own tools` and not solely rely on Sigma rules. Mature detection engineering involves using Sigma and other open-source detections as a starting point, then `adapting and tuning them to your environment` and business behavior. This improves the signal-to-noise ratio and results in higher-fidelity alerts.