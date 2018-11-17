from PIL import Image
import numpy as np

imag = imag = Image.open("/home/pi/Desktop/BE428/Image_Skin/Images/test0.jpg")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')

#Get image size
width,height = imag.size

pixel_matrix = [[0]*width]*height

for x in range(width):
    for y in range(height):
        pixelRGB = imag.getpixel((x,y))
        R,G,B = pixelRGB 
        RGB_list = [R,G,B]
        pixel_matrix(x,y) = RGB_list
        #print(RGB_list)
        # print(R)
        # print(G)
        # print(B)
print(pixel_matrix)

# #coordinates of the pixel
# X,Y = 0,0
# #Get RGB
# pixelRGB = imag.getpixel((X,Y))
# R,G,B = pixelRGB 

# print(R)
# print(G)
# print(B)