
from PIL import Image

#Load the image
#Read an image & convert it to gray-scale
filename = Image.open('nairobi.jpg').convert('L')
#resixe the image
newimage = filename.resize((500, 500))
newimage.save('nairobi.jpg')
print(type(filename))

#Get basic details about the image
print(filename.format)
print(filename.mode)
print(filename.size)

#show the image

newimage.show()