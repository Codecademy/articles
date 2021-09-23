import requests
from bs4 import BeautifulSoup

req=requests.get("https://www.python.org/")
s=BeautifulSoup(req.content,"html.parser")

# Extract all text content from website
print(s.get_text())

# Extract title of webpage
#tit=s.title
#print(tit.prettify())

# Extract title without HTML tags
#tit=s.title
#print(tit.get_text())
