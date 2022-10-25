#Implicit, make sure you have lxml:
#python3 -m pip install lxml
import requests
from bs4 import BeautifulSoup

fileName = 'password.txt'
f = open(fileName,'r')
count = 1
for line in f:
    if count == 1:
        line = line.replace('\n', '')
        username = line
    else:
        line = line.replace('\n', '')
        password = line
    count = count + 1
print(username)
print(password)

url = 'https://quotes.toscrape.com/'
response = requests.get(url, auth=(username, password))
soup = BeautifulSoup(response.text,'lxml')
quotes = soup.find_all("span", class_="text")
authors = soup.find_all("small", class_="author")
tags = soup.find_all("div", class_="tags")
for i in range(0,len(quotes)):
    print(quotes[i].text)
    print(authors[i].text)
    quoteTags = tags[i].find_all('a',class_='tag')
    for quoteTag in quoteTags:
        print(quoteTag.text)
