'''
Write a function that returns users who had 
2 or more failed logins 
'''
logs = [
    {"user": "ryan", "status": "failed"},
    {"user": "ryan", "status": "failed"},
    {"user": "ryan", "status": "success"},
    {"user": "alex", "status": "failed"},
    {"user": "alex", "status": "failed"},
]

def detect_failed_logins(logs):
    failed_count = dict()

    for log in logs: 
        if log["status"] == "failed":
            user = log["user"]
        
        failed_count[user] = failed_count.get(user, 0) + 1 
    
    result = []
    for key, value in failed_count.items(): 
        if value >= 2: 
            result.append(key)
    
    return result
    
print(detect_failed_logins(logs))

