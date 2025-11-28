##main logic
from utils import load_rules,log_attempt 

rules=load_rules() 

##this funtion checks all conditions and returns "strong" or "weak"
def check_password(password:str) -> str:
    checks=[] 
    checks.append(len(password)>=8)                   #len>=8
    checks.append(any(c.isupper() for c in password)) #atleast 1 upppercase
    checks.append(any(c.islower() for c in password)) #atleast 1 lowercase
    checks.append(any(c.isdigit() for c in password)) #atleast 1 digit
    specials=set("!@#$%^&*()_+=-[]{};:<>,.?/")
    checks.append(any(c in specials for c in password)) #atlest 1  special character
    if all(checks):
        return "Strong"
    else:
        return "Weak"
    
##cli interacion (take input,check,log,print)
if __name__=="__main__":
    password=input("Enter password: ") 

    strength=check_password(password) 
    print("password strength: ",strength)
    #log the attempt 
    log_attempt(password,strength)
    #show rules to user 
    print("\nPassword Rules: ")
    for r in rules:
        print("-",r)
