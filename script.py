##
## PERSONAL PROJECT 2022
## script web
## File description:
## script
##

import requests
from bs4 import BeautifulSoup

def get_str(str, f):
    print(str.rstrip("\n"))
    f.write(str)

url = input('Webpage to grab source from: ')

req = requests.get(url, 'html.parser')
soup = BeautifulSoup(req.text, 'html.parser')
i = 0
with open('response.txt', 'w') as f:
    for p in soup.find_all('p'):
        get_str(p.text, f)
