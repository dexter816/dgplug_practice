#!/usr/bin/python3

from bs4 import BeautifulSoup
import urllib3,requests

page_url ="https://stackoverflow.com/questions/36516183/what-should-i-use-instead-of-urlopen-in-urllib3"
response =requests.get(page_url)
soup = BeautifulSoup(response.content, 'html.parser')

for lines in soup:
    print(soup.find('http://'))

