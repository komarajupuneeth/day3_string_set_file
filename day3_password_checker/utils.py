#this file will contain helper functions used by  checker.py 
def load_rules(): #reads password_rules.txt and returns a list of rule strings
    with open("password_rules.txt","r") as f:
        rules=[line.strip()    for line in f.readlines()]
    return rules

def log_attempt(password: str, result:str):
    with open("log.txt","a") as f:     #appends a log entry to og.txt with password and result
        f.write(f"{password}:{result}\n")  

