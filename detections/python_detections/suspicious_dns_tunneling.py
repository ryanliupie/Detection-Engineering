def detect_dns_tunneling(logs):
    '''
    A query is suspicious if: 

    1. the first subdomain is longer than 15 characters 
    2. the first subdomain contains both letters and characters
    '''
    suspicious_counts= dict()

    for log in logs: 
        domain = log["query"]

        if "." not in domain: 
            continue 
        
        split = domain.split(".")
        subdomain = split[0]


        if len(subdomain) > 15:
            has_letter = False 
            has_number = False 

            for char in subdomain:
                if char.isalpha(): 
                    has_letter = True 
                if char.isdigit(): 
                    has_number = True

            if has_letter and has_number: 
                ip = log["src_ip"]
                suspicious_counts[ip] = suspicious_counts.get(ip, 0) + 1
        
    result = []

    for ip, count in suspicious_counts.items():
        if count >= 3: 
            result.append(ip)
    
    return result

print(detect_dns_tunneling([
    {"timestamp": "2026-04-28T10:01:00", "src_ip": "10.0.0.5", "query": "google.com"},
    {"timestamp": "2026-04-28T10:01:05", "src_ip": "10.0.0.5", "query": "a8f9sd7f9sdf9sdf9sdf9.example.com"},
    {"timestamp": "2026-04-28T10:01:09", "src_ip": "10.0.0.5", "query": "b7x92kslqpw83mskd.example.com"},
    {"timestamp": "2026-04-28T10:01:13", "src_ip": "10.0.0.5", "query": "z9q8w7e6r5t4y3u2i.example.com"},
    {"timestamp": "2026-04-28T10:02:00", "src_ip": "10.0.0.8", "query": "github.com"},
    ]))