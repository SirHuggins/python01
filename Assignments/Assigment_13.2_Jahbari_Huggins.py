import urllib
from BeautifulSoup import *

url = raw_input('Enter URL: ')
if len(url) < 1:
    url = "http://pr4e.dr-chuck.com/tsugi/mod/python-data/data/known_by_Fikret.html"
count = int(raw_input('Enter count: '))
pos = int(raw_input('Enter position: ')) - 1
taglist = list()
urllist = list()
urllist.append(url)

print 'Retrieving: ', urllist[0]


for i in range(count):
    html = urllib.urlopen(urllist[-1]).read()
    soup = BeautifulSoup(html)
    tags = soup('a')
    for tag in tags:
        taglist.append(tag)
    url = taglist[pos].get('href', None)
    print 'Retrieving: ', url
    urllist.append(url)
print 'Last Url: ', urllist[-1]