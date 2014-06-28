from bs4 import BeautifulSoup

soup = BeautifulSoup(open("anthropology.html"))

allLinks = soup.find_all('a')

#for links in soup.find_all('a'):
    #print(links.get('href'))

#print(soup.get_text())

for word in soup.get_text().split():
    print(word)