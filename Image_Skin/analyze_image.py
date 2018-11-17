from PIL import Image

imag = imag = Image.open("/home/pi/Desktop/BE428/Image_Skin/Images/test0.jpg")
#Convert the image te RGB if it is a .gif for example
imag = imag.convert ('RGB')
#coordinates of the pixel
X,Y = 0,0
#Get RGB
pixelRGB = imag.getpixel((X,Y))
R,G,B = pixelRGB 

print(R)
print(G)
print(B)