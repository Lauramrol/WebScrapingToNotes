import requests
from bs4 import BeautifulSoup

# Dirección WEB

url = 'https://elblogdeidiomas.es/conectores/'

page = requests.get(url)
bsObj = BeautifulSoup(page.content, "html.parser")
# Identificar el bloque HTML que se desea
lista = bsObj.find_all('div', class_='entry-inner')

apuntes = open('./conectores.txt', 'w')

for name in lista:
    apuntes.write(name.text)
apuntes.close()
