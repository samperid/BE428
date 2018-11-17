from picamera import PiCamera
from time import sleep

camera = PiCamera()

name = raw_input("Insert name for images: ")

camera.start_preview()
for i in range(3):
    sleep(5)
    camera.capture('/home/pi/Desktop//BE428/Image_Skin/Images/%s%s.jpg' % name,i)
camera.stop_preview()

