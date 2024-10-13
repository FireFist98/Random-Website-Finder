import random
import string
import requests
import webbrowser
import colorama
import logging
from colorama import Fore, Style, init
init(autoreset=True)
invalid_sites = 0
valid_sites = 0
amount = int(input("Amount of Sites you want to check"))
logging.basicConfig(filename='Sites', level=logging.DEBUG)
for _ in range(amount):
 def generate_random_domain(length=8, endings=None):
    letters = string.ascii_lowercase
    
    random_name = ''.join(random.choice(letters) for _ in range(length))
    
    if endings:
        random_ending = random.choice(endings)
    else:
        random_ending = '.com'
    
    return random_name + random_ending

 possible_endings = ['.com', '.org', '.net', '.io', '.xyz']



 def check_website(url):
    global invalid_sites, valid_sites
    try:
        response = requests.get(url)

        if response.status_code == 404:
            print("Invalid site (Error 404)")
        else:
            print(f"Site is valid, status code: {response.status_code}")
            webbrowser.open('url')
            valid_sites += 1

    
    except requests.exceptions.RequestException as e:
        print(Fore.RED +"Invalid site")
        invalid_sites += 1
        
 url = ("https://" + generate_random_domain(8, possible_endings))
 
 check_website(url)
print(Fore.RED +"invalid sites: ", invalid_sites)
print(Fore.GREEN +"valid sites", valid_sites)
logging.debug(valid_sites)
logging.debug(invalid_sites)