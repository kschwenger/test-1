import RPi.GPIO as gpio # Import Raspberry Pi GPIO library
from time import sleep
gpio.setwarnings(False) # Ignore warning for now

in1, in2 = 20, 21
led1, led2, led3 = 4, 27, 13

gpio.setmode(gpio.BCM) 
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN) # Set pin 20 to be an input pin and set initial value to be pulled low (off)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN) # Set pin 21 to be an input pin and set initial value to be pulled low (off)
gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)
gpio.setup(led3, gpio.OUT)

pwm = gpio.PWM(led1, 100) # create PWM object @ 100 Hz

def button_callback(channel):
  print("Button was switched on pin %d" % channel)
  pwm.start(0) # initiate PWM at 0% duty cycle
  for dc in range(101): # loop duty cycle from 0 to 100
    pwm.ChangeDutyCycle(dc) # set duty cycle
    sleep(0.01) # sleep 10 ms
  sleep(.2)
  pwm.start(100)
  for dc in range(100,-1,-1):
    pwm.ChangeDutyCycle(dc)
    sleep(0.01)
  sleep(.2)

gpio.add_event_detect(in1,gpio.BOTH,callback=button_callback) # Setup event on pin 20 rising edge
gpio.add_event_detect(in2,gpio.BOTH,callback=button_callback) # Setup event on pin 21 rising edge

# continually blink led 3 at 1 hz unless keyboard interrupt
try:
  while True:
    gpio.output(led3, 0)
    sleep(0.5)
    gpio.output(led3, 1)
    sleep(0.5)
except KeyboardInterrupt: # if user hits ctrl-C
  print('\nExiting')
except Exception as e: # catch all other errors
  print('\ne')

gpio.cleanup() # Clean up
