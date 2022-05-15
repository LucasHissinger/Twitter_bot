##
## PERSONAL PROJECT 2022
## script web
## File description:
## script
##

import requests
from bs4 import BeautifulSoup

def get_str(str, f):
    f.write(str)

url = input('Webpage to grab source from: ')
file_name = input('name of the file : ')

req = requests.get(url, 'html.parser')
soup = BeautifulSoup(req.text, 'html.parser')
with open(file_name, 'w') as f:
    for p in soup.find_all('p'):
        get_str(p.text, f)
