import requests
import bs4


res = requests.get("https://en.wikipedia.org/wiki/Grace_Hopper")

soup = bs4.BeautifulSoup(res.text,"lxml")
print(soup.select('.toctext')[0])

first_item = soup.select('.toctext')[0]

for item in soup.select('.toctext'):
    print(item.text)
