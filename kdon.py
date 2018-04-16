import urllib2
from os import system
from bs4 import BeautifulSoup
import wget

system('figlet "KDON"')

url = raw_input("Enter the serial URL:")

conn = urllib2.urlopen(url)
html = conn.read()

soup = BeautifulSoup(html,"html.parser")
links = soup.find_all('a')

for tag in links:
    link = tag.get('href',None)
    if link is not None:
        print(url+str(link))

        wget.download(url+str(link))
