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

    - 