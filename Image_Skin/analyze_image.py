from PIL import Image
import numpy as np

#Pixel color object which will store RGB Value
class pix_color:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue

imag = imag = Image.open("/home/pi/Desktop/BE428/Image_Skin/Images/test0.jpg")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')

#Get image size
width,height = imag.size

#Pixel dictionary will store pixel color instance
pixel_dict = {}

for x in range(width):
    #Each key in dictionary is a list which stores pix_color instance for every column
    pixel_dict[x] = []
    for y in range(height):
        #Get each pixel from image
        pixelRGB = imag.getpixel((x,y))
        #Get specific RGB value from pixel
        R,G,B = pixelRGB 
        #Append 
        pixel_dict[x].append(pix_color(R,G,B))

for x in range(width):
    for y in range(height):
        print(pixel_dict[x][y].red)
        print(pixel_dict[x][y].green)
        print(pixel_dict[x][y].blue)

# #coordinates of the pixel
# X,Y = 0,0
# #Get RGB
# pixelRGB = imag.getpixel((X,Y))
# R,G,B = pixelRGB 

# print(R)
# print(G)
# print(B)