from picamera import PiCamera
from time import sleep

camera = PiCamera()

name = raw_input("Insert name for images: ")

camera.start_preview()
for i in range(2):
    sleep(5)
    num = str(i)
    full_str = name+num
    camera.capture('/home/pi/Desktop//BE428/Image_Skin/Images/%s.jpg' % full_str)
camera.stop_preview()

