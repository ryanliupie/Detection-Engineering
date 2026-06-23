# What is Threat Modeling?

Threat modeling is the structured process of identifying, analyzing, and addressing threats to a system, application, network, or business process before they can be exploited.

> "What could go wrong, and what are we going to do about it?"

Believe it or not, humans perform a form of threat modeling every day.

For example, when making a left turn at an intersection, you naturally assess potential risks before acting:

- Are pedestrians crossing?
- Is there incoming traffic?
- Is the traffic light changing?
- Is it safe to proceed?
- Can I complete the turn before the light changes?

Without realizing it, you are:

1. Identifying assets
2. Identifying threats
3. Assessing risk
4. Determining mitigations

<hr>

## The Four-Question Framework

These four questions form the foundation of most threat modeling exercises.

### 1. What Are We Building?

Before identifying threats, we must understand the system itself.

This includes:

- Business purpose
- Assets and data
- Architecture and components
- Data flows
- Trust boundaries
- Users and administrators

Examples of assets:

- Customer information
- Authentication credentials
- Financial records
- Intellectual property

Understanding what we are protecting is the foundation of threat modeling.

---

### 2. What Can Go Wrong?

This stage focuses on identifying threats, vulnerabilities, and attack paths.

Some common questions include:

- How could an attacker gain access?
- What data could be stolen?
- What services could be disrupted?
- What components could be abused?

One popular methodology is <b>STRIDE</b>:

| Threat | Description |
|----------|-------------|
| Spoofing | Pretending to be another user or system |
| Tampering | Modifying data or code |
| Repudiation | Denying actions without proof |
| Information Disclosure | Unauthorized access to sensitive data |
| Denial of Service | Making a service unavailable |
| Elevation of Privilege | Gaining unauthorized permissions |

The goal is to identify realistic threats before they can be exploited.

---

### 3. What Are We Going To Do About It?

Once threats are identified, organizations determine how they will address them.

Common risk treatment options include:

- Mitigate
- Transfer
- Accept
- Avoid

Examples of security controls:

- Multi-Factor Authentication (MFA)
- Encryption
- Input Validation
- Network Segmentation
- Security Monitoring
- Rate Limiting

The objective is to reduce risk to an acceptable level.

---

### 4. Did We Do A Good Job?

Threat modeling should be reviewed continuously.

Questions to ask:

- Were important threats missed?
- Were mitigations effective?
- Did new risks emerge?
- What lessons were learned?

Threat modeling is not a one-time activity. As systems evolve, new threats will emerge.

<hr>

## Key Concepts

### Assets

Assets are anything valuable that requires protection.

Examples include:

- Customer data
- Source code
- User credentials
- Databases
- Financial information

### Data Flows

Data flows describe how information moves between components.

Examples:

- User → Web Application
- Web Application → Database
- Application → Third-Party API

Understanding data flows helps identify where attacks may occur.

### Trust Boundaries

A trust boundary exists whenever data moves between components that have different levels of trust.

Examples:

- Internet → DMZ
- DMZ → Internal Network
- User → Administrator Functions
- Application → Database

Whenever data crosses a trust boundary, additional validation and security controls should be considered.

<hr>

## Benefits of Threat Modeling

- Early risk identification
- Reduced remediation costs
- Improved system design
- Better resource allocation
- Stronger security posture
- Security by Design
- Compliance and regulatory alignment
- Better Agile and DevOps integration

Threat modeling allows organizations to identify and address security risks before they become vulnerabilities in production.