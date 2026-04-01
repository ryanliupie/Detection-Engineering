### What is Detection Engineering? 

It is the continuous lifecycle-based process of building, testing, and refining security analytics to identify malicious activity or misconfiguration, often leveraging frameworks such as the MITRE ATT&CK. It requires close collaboration between threat intelligence, security operations (SOC), and red teams to create high-fidelity, actionable alerts that reduce false positives and improve detection speed. 

### Detection Types 

There are two perspectives when it comes to threat detection: 

1. <b>Environment-based:</b> This focuses looking at changes in an environment based on configurations and defined baseline activities. In this detection, there are two important subactivies: 

    - <b>Configuration Detection:</b> For this detection, we use the current knowledge of the known environment and infrastructure to identify misconfigurations.  

        | Benefits    | Challenges |
        | -------- | ------- |
        | Easy detection to maintain in static environments  | Hard detection to maintain in dynamic environments  |
        | Easy to combine with other detections for forensics and response | Frequent configuration changes leads to large volumes of false positives    |
        | Individuals of different expertise can easily execute detection    | Assumption of knowledge of configurations and the working infrastructure.    |

     <b>Modelling:</b> Threat detection under this type is done by defining baseline activities such as expected ingress and egress traffic during different times throughout the day, and recording for any deviations that occur. This approach assumes that even from benign activity, it may be malicious. 
     


- <b>Threat-based:</b> This focuses on elements associated with an adversary's activity. There are different tactics, techniques and procedures an attacker utilizes as well as the artifacts they leave behind. Understanding these components can significant help with identifying there is Indicators and Threat Behaviour detections. 