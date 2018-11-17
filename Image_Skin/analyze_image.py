from PIL import Image
import numpy as np

imag = imag = Image.open("/home/pi/Desktop/BE428/Image_Skin/Images/test0.jpg")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')

#Get image size
width,height = imag.size

arr_width = int(width)
arr_height = int(height)

pixel_array = np.zeros(arr_width,arr_height)

for x in range(width):
    for y in range(height):
        pixelRGB = imag.getpixel((x,y))
        R,G,B = pixelRGB 
        # print(R)
        # print(G)
        # print(B)

#coordinates of the pixel
X,Y = 0,0
#Get RGB
pixelRGB = imag.getpixel((X,Y))
R,G,B = pixelRGB 

print(R)
print(G)
print(B)