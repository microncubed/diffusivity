from apscheduler.schedulers.blocking import BlockingScheduler
from time import sleep,time
from picamera import PiCamera
import RPi.GPIO as GPIO


GPIO.setmode(GPIO.BCM)
GPIO.setup(14,GPIO.OUT)
GPIO.output(14,0)
camera = PiCamera()
camera.resolution=(1640,1232)
#camera.iso=100

camera.exposure_mode='auto'
camera.meter_mode ='spot'

camera.start_preview()
# Wait for the automatic gain control to settle
sleep(2)
# Now fix the values
camera.stop_preview()

g = camera.awb_gains
camera.awb_mode = 'off'
camera.awb_gains = g
print(g)
print('running')

sched = BlockingScheduler()




def my_interval_job():
    GPIO.output(14,1)
    sleep(2)
    camera.start_preview()
    # Camera warm-up time
    sleep(2)
    camera.capture(str(int(time()))+'.png')
    #print(i)
    camera.stop_preview()
    GPIO.output(14,0)

sched.add_job(my_interval_job, 'interval', minutes=12,start_date='2020-6-01 20:00:00',end_date='2020-8-01 20:00:00' )
sched.start()
#print('finished')


