import urllib.request
import requests
import urllib.parse
from bs4 import BeautifulSoup
import re
global i
i=0
url = "https://dgplug.org/irclogs/2017/"
url_open = urllib.request.urlopen(url)

""" create a file with all the logs aas text input """


def extract_links(url_open):
    soup = BeautifulSoup(url_open, 'lxml')
    # print(soup)
    for line in soup.find_all('a'):
            link = line.get('href')
            response = requests.get(url + link)
            with open('logfile.txt', 'a') as logobj:
                logobj.write(response.text)


""" working on logfile and extracting nicks: spokenlines"""


def spoken_lines():
   with open ('logfile.txt','r') as logobj:
       data = logobj.read()
       nicks = re.findall(r'<(.*?)>', data)
       nicks_set = set(nicks)
       print(nicks_set)

       for nick in nicks:
           if nick in nick_count:
               nick_count[nick] += 1
           else:
               nick_count[nick] = 1
       nick_count = {}
       print(nick_count)
       for keys, values in nick_count.items():
           print(keys, ":", values, "lines")

extract_links(url_open)
spoken_lines()
