# Getting Started in Detection Engineering 

There are many great resources out on the internet such as the  MITRE ATT&CK framework. One thing that gets overlooked, is `Understanding your own environment and processes!`. For example, when accounts get created, how does that work in an environment. This helps you understand any diversions or anomalies. 

## Maturity Matrix
It is important to have a roadmap by starting small and expanding outwards. Detection engineering is essentially a `Scaling problem`, not just a detection-writing problem. 

<b>Detection Maturity</b> is defined by: 

- <b>Where you are today</b> (current detection coverage, telemetry, and tooling)
- <b>Where you want to be</b> (desired visibility, detection depth, response capabilities)

A good resource to check out is <a href ="https://detectionengineering.io/"> detectionengineering.io</a> which provides a roadmap to help start a detection engineering team or expand an existing one. 

## Challenges

<b>False Positive Tendencies</b>: We want to make sure that we have `High-fidelity` detections as they provide the most accurate, actionable, and low-false positive results. 

<b>Lack of Resources:</b> It is important to think about `scale`. When we think of detection engineering, we can think of it as a `three-legged stool`: 

1. <b>SSMEs (Security Subject Matter Expertise)</b>: These are critical to make sure we know what the threat land-scape is. `What should we detect and why?`

2. <b>Statistics</b>: This helps measure patterns, baselines, anomalies, false positives, and signal quality. `Is this activity unusual or meaningful?`

3. <b>Software-engineering</b>: Turns detection logic into scalable, maintainable, testable systems. `Can this detection run reliably at scale?`

## Common Mistakes Team Make 

1. `Thinking that more is better`

    - Taking on a lot of rules at once is not a great idea. If this is done, there is high chance of false-positives which is detrimental not only for the detection engineering team but also for SOC analysts. 

    - It is important for teams to prioritize things they want to detect. This is highly dependant on the type of business the team is in. 

2. `Keep it simple`

    - Not every suspicious event should become  a "high-alert detection"
    - If you try to detect everything, you are prone to creating false-positives
    - Detection engineering should focus on building high-quality, actionable alerts rather than large quantities of noisy detections

    Imagine you detect: 
    - powerShell execution 
    - admin tools 
    - mass login attempts 
        - If these are alerted, the SOC teams get exploded with noise. Instead you want `high fidelity` detections such as: 
            - encoded PowerShell from Word macro spawning cmd.exe
            - Local Security Authority Subsystem Service (LSASS - `lsass.exe`) access attempts. 
    
    <b>Example - Chained Authentication</b>
    
    - This is when one set of credentials is used to authenticate across multiple systems in a short period of time. If a threat actor compromises valid credentials, they may attempt to move laterally across the network by trying to use them to access other resources/hosts. 
    - However, internal employees can access many resources with their set of credentials, so within the detection, we must answer questions such as: 

        - Is this normal for the user?
        - Is the source host unusual?
        - Are the destination systems sensitive?
        - Is the authentication type interactive, remote, or service-based?
        - Did the activity happen outside normal working hours?
        - Was there a failed-login burst before the successful authentications?
        - Is the user authenticating to systems they normally never access?
    
    - `Important Distinction`, if for the following:  
    
         - Host A → authentication to Host B
         - Host B → authenticates to Host C 
         - Host C → authenticates elsewhere

        There is a high chance that it is a high fidelity detection as this is unusual. 

    - `Detect the links, not the chain`

        - Do not blindly alert on evert sequence of events. Instead, detect the suspicious relationship between events. 

## Blind Spots

A <b>detection blindspot</b> exists when the security team does not have the data or visibility needed to detect certain activity. Since full visibility is not always possible, detection engineers should place `“tripwires”` at key points where adversaries are likely to make mistakes or interact with monitored systems.

If you cannot detect the activity at the network layer, you may need to detect later in the attack chain or add controls directly on the resource they are trying to infiltrate. 

For example: 

- If source code or sensitive files might leave through an unmonitored split tunnel path, add monitoring and controls around the source code repository or file share itself.

