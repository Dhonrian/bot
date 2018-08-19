from lxml import html
from bs4 import BeautifulSoup as bs
import requests
import re


pag = requests.get('https://www.cifraclub.com.br/mais-acessadas/rock/')
s = bs(pag.content, 'lxml')


musicas = s.find_all('a', href=re.compile("/"))


links = []

file = open('input.txt','w')
#Finds all links that begin with a "/"
for link in musicas:
    if link.attrs['href'] is not None:
        if link.attrs['href'] not in links:
            if(link.attrs['href'].startswith("/")):
                links.append(link.attrs['href'])
            else:
                links.append(link.attrs['href'])

links = links[2:102]


for url in links:
    pag_url = requests.get('https://www.cifraclub.com.br'+url)
    soup = bs(pag_url.content, 'lxml')
    notas = soup.find('pre').findChildren('b')

    for nota in notas:
        z = nota.string
        print(z)
        file.write(z)
        file.write(" ")

    file.write("\n")

file.close()




