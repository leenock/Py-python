import requests
import bs4


result = requests.get("http://example.com/")

type(result)
# make it a beautiful outfit 
soup = bs4.BeautifulSoup(result.text,"lxml")
print(soup)

print('\n')
# grap the title of the page without the tags included.
print(soup.select('title')[0].getText())

# grap the paragraphs
print(soup.select('p'))

#grap the headers
print(soup.select('h1'))
