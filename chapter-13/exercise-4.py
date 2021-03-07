import urllib.request
from bs4 import BeautifulSoup

url = input("Enter a url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

paragraphs = soup("p")
print(len(paragraphs))
