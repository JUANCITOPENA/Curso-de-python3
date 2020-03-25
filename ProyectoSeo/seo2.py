import urllib.request as request
#from bs4 import BeautifulSoup
from urllib.request import  urlopen
import os
import re
#from lxml.html._diffCommand import description



#Verificacion de los h1
"""
site = request.urlopen("http://python.org")
soup = beautifulSoup(site)
for h1 in soup.find_all("h1"):
    print("Este es un h1: " , h1)

print("En total son: ", len(soup.find_all("h1")))
"""

#Verificacion de  = beautifulSoup(site)links

"""
site = request.urlopen("http://python.org")
soup =BeautifulSoup(site)
links = []
elements = soup.select("a")

for element in elements:
    link = element.get("href")
    if link.startswith("http"):
        links.append(link)
print(links)

for link in links[:10]:
    petition = urlopen(link)
    print("enlace: ", link, "Respuesta: ", petition.code)
"""

#Verificacion de existencia dea archivos
"""
for file in os.listdir("/RutaX"):
    if file.endswith((".Extencion"):
        print("se encontro el archivo ", os.path("/RutaX"), file)


"""

#Verificacion de fanvico
url = "http://python.org"
page = request.urlopen(url)
soup = BeautifulSoup(page)
icon_link = soup.find("link", rel = "icon")
icon = request.urlopen(url+icon_link["href"])
with open ("test.ico", "wb" ) as f:
    try:
        f.write(icon.read())
        print("Succes!")
    except:
        print("No hay icono")

#Verificacion de Analytics
page = request.urlopen("http://python.org")
soup = BeautifulSoup(page)
if(soup.findAll(text= re.compile(".google-analytics"))):
    print("contiene googleAnalytics")
else:
    print("No contiene analytics")

#Verificacion de Idioma
site = request.urlopen("https://python.org")
soup = BeautifulSoup(site, "html.parse")
lang = soup.find("html")["lang"]
print("El idioma del sitio web es, lang = ", lang)

#Verificacion del Charset
site = "https://python.org"
print("pagina: " , site)
peticion = request.urlopen(site)
meta = petition.info()
print(meta)

#Verificacion del Viwport
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
if(soup.find("meta", attrs={"name":"viewport"})):
    print("Viewport: " , description.get("content"))
else:
    print("No cuenta con viewport")