from picamera import PiCamera
from time import sleep

camera = PiCamera()

name = raw_input("Insert name for images: ")

camera.start_preview()
for i in range(1):
    sleep(10)
    #num = str(i)
    #full_str = name+num
    full_str = name
    camera.capture('/home/pi/Desktop//BE428/Image_Skin/Images/%s.jpg' % full_str)
camera.stop_preview()

