"""
import RPi.GPIO as gpio # Import Raspberry Pi GPIO library
in1, in2 = 20, 21
led1, led2, led3 = 4, 27, 13
gpio.setmode(gpio.BCM) # Use physical pin numbering
gpio.setup(in1, gpio.IN, pull_up_down=gpio.PUD_DOWN) # Set pin 20 to be an input pin and set initial value to be pulled low (off)
gpio.setup(in2, gpio.IN, pull_up_down=gpio.PUD_DOWN) # Set pin 21 to be an input pin and set initial value to be pulled low (off)
gpio.setup(led1, gpio.OUT)
gpio.setup(led2, gpio.OUT)
gpio.setup(led3, gpio.OUT)

def button_callback(pin, channel):
    print("Button was pushed on pin %d" % channel)
    gpio.output(pin, 1)
gpio.setwarnings(False) # Ignore warning for now


gpio.add_event_detect(in2,gpio.RISING,callback=button_callback) # Setup event on pin 20 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

gpio.cleanup() # Clean up
"""