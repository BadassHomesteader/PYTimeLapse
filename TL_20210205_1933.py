from picamera import PiCamera
from os import system
import datetime
from time import sleep

tlminutes = 10 #set this to the number of minutes you wish to run your timelapse camera
secondsinterval = 1 #number of seconds delay between each photo taken
fps = 30 #frames per second timelapse video
numphotos = int((tlminutes*60)/secondsinterval) #number of photos to take
print("number of photos to take = ", numphotos)

dateraw= datetime.datetime.now()
datetimeformat = dateraw.strftime("%Y-%m-%d_%H:%M")
print("RPi started taking photos for your timelapse at: " + datetimeformat)

camera = PiCamera()
camera.resolution = (1024, 768)

system('rm /home/pi/Pictures/*.jpg') #delete all photos in the Pictures folder before timelapse start

for i in range(numphotos):
    camera.capture('/home/pi/Pictures/image{}.jpg'.format(int(time.time())), img)
    sleep(secondsinterval)
print("Done taking photos.")
print("Please standby as your timelapse video is created.")

