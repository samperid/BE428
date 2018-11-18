from PIL import Image
import numpy as np

#Pixel color object which will store RGB Value
class pix_color:
    def __init__(self,red,green,blue):
        self.red = red
        self.green = green
        self.blue = blue
        self.brightness = sum([red,green,blue])/3

imag = imag = Image.open("/home/pi/Desktop/BE428/Image_Skin/Images/DR3_B.jpg")
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
        #Append pix_color instance to list 
        pixel_dict[x].append(pix_color(R,G,B))

#Print outputs
total_R = 0
total_G = 0
total_B = 0
total_bright = 0
for x in range(width):
    for y in range(height):
        total_R = total_R + pixel_dict[x][y].red
        total_G = total_G + pixel_dict[x][y].green
        total_B = total_B + pixel_dict[x][y].blue
        total_bright = total_bright + pixel_dict[x][y].brightness
        '''
        print("Pixel %i,%i:" % (x,y))
        print("\n")
        print("Red = %i " % pixel_dict[x][y].red)
        print("\n")
        print("Green = %i " % pixel_dict[x][y].green)
        print("\n")
        print("Blue = %i " % pixel_dict[x][y].blue)
        print("\n")
        '''

avg_R = total_R / (width*height)
avg_G = total_G / (width*height)
avg_B = total_B / (width*height)
avg_bright = total_bright / (width*height)
print("\n")
print("Image File: DR3_B")
print("avg_R = %f" % avg_R)
print("avg_G = %f" % avg_G)
print("avg_B = %f" % avg_B)
print("avg_brightness = %f" % avg_bright)
print("\n")