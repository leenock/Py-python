import img as img
import requests
import bs4
from pip._internal.cli.cmdoptions import src

res = requests.get("https://en.wikipedia.org/wiki/Deep_Blue_(chess_computer)")

soup = bs4.BeautifulSoup(res.text,"lxml")
soup.select('img')
#print(soup.select('.thumbimage'))

computer = soup.select('.thumbimage')[0]
print(computer['src'])

comp = '<img src="upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg">'

# save an image in jpg file in your directory project

image_link = requests.get("https://upload.wikimedia.org/wikipedia/commons/thumb/b/be/Deep_Blue.jpg/220px-Deep_Blue.jpg")
print(image_link.content)
# wb means write an image binary
f = open('my_computer_image.jpg', 'wb')
f.write(image_link.content)
f.close()
