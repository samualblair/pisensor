#!/usr/bin/env python3

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

# Connect the Grove Gas Sensor to analog port A0
# SIG,NC,VCC,GND
gas_sensor = 0

grovepi.pinMode(gas_sensor,"INPUT")

logging.basicConfig(filename='/var/log/pytemp/all.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)



while True:
    try:
        # Get Temp and Humidity value
        # This example uses the blue colored sensor.
        # The first parameter is the port, the second parameter is the type of sensor.
        [temp,humidity] = grovepi.dht(sensor,blue)
        #if math.isnan(temp) == False and math.isnan(humidity) == False:
            #logging.info( f'Temp={temp} C and Humidity={humidity}%' )
            # Not sure if sleep is needed, but seems to be minimal enough not to hurt
            #time.sleep(.5)

        # Get Gas sensor value
        sensor_value = grovepi.analogRead(gas_sensor)

        if math.isnan(temp) == False and math.isnan(humidity) == False and math.isnan(sensor_value) == False:

        # Calculate gas density - large value means more dense gas
            density = (sensor_value / 1024.00)
            d_percentage = "{:.0%}".format(density)
#        logging.info( f'Sensor value={sensor_value} and Density={density} and Density_p={d_percentage}' )
#        time.sleep(.5)

        # Combined sensor log value
#        if math.isnan(temp) == False and math.isnan(humidity) == False:
            logging.info( f'Sensor value={sensor_value} and Density={density} and D_Percentage={d_percentage} % and Temp={temp} C and Humidity={humidity} %' )
            time.sleep(.5)

    except IOError:
        print ("Error")


