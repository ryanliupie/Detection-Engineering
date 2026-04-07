'''
Write a function that returns the users who performed 
a "delete actions"
'''

logs = [
    {"user": "ryan", "file": "report.docx", "action": "read"},
    {"user": "ryan", "file": "report.docx", "action": "read"}, 
    {"user": "ryan", "file": "secret.xlsx", "action": "delete"},
    {"user": "alex", "file": "notes.txt", "action": "read"},
    {"user": "alex", "file": "data.csv", "action": "delete"},
]

def detect_file_deletes(logs):
    suspicious_users = set() # we use a set for unique users to avoid duplicates

    for log in logs: 
        if log["action"] == "delete": 
            suspicious_users.add(log["user"])
    
    return suspicious_users

print(detect_file_deletes(logs))