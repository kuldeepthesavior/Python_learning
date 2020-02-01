import requests

# getting the url,s html code

r=requests.get('https://www.flipkart.com/')
c=r.content
# print(c)

# proper view of html code

from bs4 import BeautifulSoup

soup=BeautifulSoup(c,'html.parser')

print(soup.prettify())

links=[]

for link in soup.find_all('a'):
    print('link in page',link.get('href'))
    links.append(link)


# print(links)

#  select by class

for price in soup.find_all('span',class_='le_eco'):
    print('price ',price)