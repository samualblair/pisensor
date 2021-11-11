#!/usr/bin/env python

import grovepi
import math
import time
import logging

# Connect the Grove Temperature & Humidity Sensor Pro to digital port D4
# This example uses the blue colored sensor.
# SIG,NC,VCC,GND
sensor = 4  # The Sensor goes on digital port 4.

# temp_humidity_sensor_type
# Grove Base Kit comes with the blue sensor.
blue = 0    # The Blue colored sensor.
white = 1   # The White colored sensor.

#logging.basicConfig(filename='temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO) 
logging.basicConfig(filename='/var/log/pytemp/temperature.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO) 


    

while True:
    try:
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor,blue)
        if math.isnan(temp) == False and math.isnan(humidity) == False:

#REFERENCE# VALID old style format - works in python 2
#            logging.info('Temp=%.02f C and Humidity=%.02f% %'%(temp, humidity))
#REFERENCE# VALID old style format - works in python 3 after a few adjustments from python 2
#            logging.info('Temp=%.02f C and Humidity=%.02f '%(temp, humidity))

#REFERENCE# AS of 2.6 style format
            logging.info('Temp={} C and Humidity={}%' .format(temp, humidity))

#REFERNCE# AS of 3.6 style format
#SO Make sure either default is python3
#or , #!/usr/bin/env python3
#            logging.info( f'Temp={temp} C and Humidity={humidity}%' )

# Not sure if sleep is needed, but seems to be minimal enough not to hurt
            time.sleep(.5)


    except IOError:
        print ("Error")

## OR
# while True:     
#    h,t = adht.read_retry(adht.DHT22, 4)     
#    logging.info('Temp={0:0.1f} C and Humidity={1:0.1f} %'.format(t, h)) 
#


