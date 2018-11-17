import Image
import numpy as np

imag = Image.open("/home/pi/Desktop//BE428/Image_Skin/Images/")

#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')

#Get size of image
width,height = imag.size

pixel_array = np.zeros(width,height)

#Get RGB
pixelRGB = imag.getpixel((X,Y))
R,G,B = pixelRGB 