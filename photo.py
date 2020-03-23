from time import sleep
from picamera import PiCamera
import datetime

camera = PiCamera()
camera.resolution = (3280, 2464)
camera.awb_mode = "off"
camera.awb_gains = (0.92, 0.97)

#camera.start_preview()

#camera warm-up time
sleep(2)

while 1:
  filename = str(datetime.datetime.now()) + ".jpg"
  sleep(1)
  print(filename)
  camera.capture(filename)
