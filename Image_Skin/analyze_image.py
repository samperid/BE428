from PIL import Image
import numpy as np

imag = Image.open("/home/pi/Desktop/BE428/Image_Skin/Images/test0.jpg")

#Convert the image te RGB if it is a .gif for example
imag = imag.convert('RGB')

#Get size of image
width,height = imag.size

pixel_array = np.zeros(((width,height))

#Get RGB
for row in range(width):
    for column in range(height):
        pixelRGB = imag.getpixel((row,column))
        R,G,B = pixelRGB
        # RGB_vec = [R,G,B]
        # pixel_array(row,column) = RGB_vec
        #R,G,B = pixelRGB 

# print(pixel_array)

# from PIL import Image
# imag = imag = Image.open("/home/pi/Desktop/BE428/Image_Skin/Images/test0.jpg")
# #Convert the image te RGB if it is a .gif for example
# imag = imag.convert ('RGB')
# #coordinates of the pixel
# X,Y = 0,0
# #Get RGB
# pixelRGB = imag.getpixel((X,Y))
# R,G,B = pixelRGB 

# print(R)
# print(G)
# print(B)