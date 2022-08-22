import requests
from bs4 import BeautifulSoup
  
URL = "https://www.imdb.com/title/tt0386676/episodes?season=1"
r = requests.get(URL)
  
soup = BeautifulSoup(r.content, 'html5lib') # If this line causes an error, run 'pip install html5lib' or install html5lib
print(soup.prettify())
# #test = soup.find_all('a', attrs={'class': 'tracked-offsite-link mini-watchbox__primary-button promoted-watch-ad'})
# f = open('test.txt', 'w')
# f.write(str(soup))
# f.close()
# # print(test)