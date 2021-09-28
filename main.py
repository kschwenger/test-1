import RPi.GPIO as gpio # Import Raspberry Pi GPIO library
from time import sleep
gpio.setwarnings(False) # Ignore warning for now

button1pressed = False
button2pressed = False
in1, in2 = 20, 21
led1, led2, led3 = 4, 27, 13

gpio.setmode(gpio.BCM) 
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN) # Set pin 20 to be an input pin and set initial value to be pulled low (off)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN) # Set pin 21 to be an input pin and set initial value to be pulled low (off)
gpio.setup(led1, gpio.OUT)      # set led pins as output pins
gpio.setup(led2, gpio.OUT)
gpio.setup(led3, gpio.OUT)

pwm1 = gpio.PWM(led1, 1) # create PWM object @ 100 Hz for both leds
pwm2 = gpio.PWM(led2, 1) 

def button_callback(channel):
  if channel == in1:
    pwm1.start(0) # initiate PWM at 0% duty cycle
    for dc in range(101): # loop duty cycle from 0 to 100
      pwm1.ChangeDutyCycle(dc) # set duty cycle
      sleep(0.01) # sleep 10 ms
    pwm1.start(100)
    for dc in range(100,-1,-1):
      pwm1.ChangeDutyCycle(dc)
      sleep(0.01)
  
  if channel == in2:
      pwm2.start(0) # initiate PWM at 0% duty cycle
      for dc in range(101): # loop duty cycle from 0 to 100
        pwm2.ChangeDutyCycle(dc) # set duty cycle
        sleep(0.01) # sleep 10 ms
      pwm2.start(100)
      for dc in range(100,-1,-1):
        pwm2.ChangeDutyCycle(dc)
        sleep(0.01)


gpio.add_event_detect(in1,gpio.RISING,callback=button_callback) # Setup event on pin 20 on RISING
gpio.add_event_detect(in2,gpio.RISING,callback=button_callback) # Setup event on pin 21 on RISING

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
