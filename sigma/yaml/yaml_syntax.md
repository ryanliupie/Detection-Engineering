## YAML Syntax

- We use the "#" for comments 
- Key value pairs denoted with ":"
- Array elements denoted with "-"
<hr>

- <b>Title</b>: Names the rule based on what it is supposed to detect (short and clear)

- <b>ID</b>: A globally unique identifier used to keep track of the rule submitted to the public repo found in UUID format. For example it could be ` 0f06a3a5-6a09-413f-8743-e6cf35561297`

- <b>Status</b>: Describes the state in which the rule maturity is at while in use: 
    - `Stable`: The rule may be used in production environments
    - `Test`: Trials being done and could require fine-tuning
    - ` Experimental`: The rule is generic and being tested (may lead to false positives)
    - `Depreciated`: The rule has been replaced and would no longer yield results 
    - `Unsupported`: The rule is not useable in its current state

- <b>Description</b>: Provides more context about the rule and what it is supposed to do. 

- <b>Logsource</b>: Describes the log data used for the detection
    - `Product`: Selects all log outputs of a particular product (e.g., Windows)
    - `Category`: Selects the log files written by the selected product 
    - `Service`: Selects only a subset of the logs from the selected product 
    - `Definition`: Describes the log source and any applied configurations 