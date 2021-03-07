from bs4 import BeautifulSoup
import urllib.request

url = input("Enter a url: ")
html = urllib.request.urlopen(url).read()
soup = BeautifulSoup(html, "html.parser")

anchors = soup('a')
for a in anchors:
	print(a.get("href", None))