import RPi.GPIO as gpio # Import Raspberry Pi GPIO library

led1, led2, led3 = 4, 17, 27
gpio.setup(led1, gpio.OUT)

def button_callback(channel):
    print("Button was pushed!")
    gpio.output(led1, 1)
gpio.setwarnings(False) # Ignore warning for now
gpio.setmode(gpio.BCM) # Use physical pin numbering
gpio.setup(20, gpio.IN, pull_up_down=gpio.PUD_DOWN) # Set pin 20 to be an input pin and set initial value to be pulled low (off)

gpio.add_event_detect(20,gpio.RISING,callback=button_callback) # Setup event on pin 20 rising edge

message = input("Press enter to quit\n\n") # Run until someone presses enter

gpio.cleanup() # Clean up