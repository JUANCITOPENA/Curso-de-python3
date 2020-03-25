#Auditoria SEO
import urllib.request as request
import os
#from urllib.request import_urlopen
#import BeautifulSoup

#Verificacion del https y www
req = request.Request("http://python.org")
res = request.urlopen(req)
print(res.geturl())

#Verificacion del peso de la pagina
url = "https://python.org"
print("url:", url)

site = request.urlopen(url)
meta = site.info()
print(" content-Length: ", site.headers["content-length"])

f = open("out.txt", "r")
print("file on disk:", len(f.read()))
f.close()

f = open("out.txt",  "wb")
f.write(site.read())
site.close()

f = open("out.txt", "r")
print("file on disk after download: " , len(f.read()))
f.close()

print("os.stat(.st_size returns:", os.stat("out.txt").st_size)

#Verificar Metas
"""
site = request.urlopen("https://www.python.org")
soup = BeautifulSoup(site)
description = soup.find("meta", attrs ={"name" : "description"})
print("El tamaño de meta description es: ", len(description.get("content")))

if (len(description.get("content"))) < 154:
    print("el meta description en menor a 154")
"""

#Verificar Etiqueta title
html = request.urlopen("https://www.python.org")
soup = BeautifulSoup(html.read())
print("El tamaño del title es: ", len(soup.html.head.title.string))
print("El title dice: ", soup.html.head.title.string)

#Verificar parabras claves
site = request.urlopen("http://python.org")
soup = BeautifulSoup(site)
keywords = soup.find("meta", attrs = {"name": "keywords"})
print("Python.org Keywords: ", keywords.get("content"))
words = keywords.get("content").split()
print(words)
for word in words:
    print(word.len(soup.findAll(text=re.compile(word))))

#Verificar alt de la imagen
site = request.urlopent("http://python.org")
soup = BeautifulSoup(site)
count = 1
for image in soup.findAll("img")
    print("Imgen #", count, ":", image["src"])
    print("Alt de imgen #", count, ":", image.get("alt", "None"))