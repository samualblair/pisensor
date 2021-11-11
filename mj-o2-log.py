#!/usr/bin/env python
#
# GrovePi Example for using the  Grove Gas Sensor
#
# The GrovePi connects the Raspberry Pi and Grove sensors.  You can learn more about GrovePi here:  http://www.dexterindustries.com/GrovePi
#
# Have a question about this example?  Ask on the forums here:  http://forum.dexterindustries.com/c/grovepi
#
'''
## License

The MIT License (MIT)

GrovePi for the Raspberry Pi: an open source platform for connecting Grove Sensors to the Raspberry Pi.
Copyright (C) 2017  Dexter Industries

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in
all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
THE SOFTWARE.
'''

# NOTE:
# There are 5 gas sensors
# MQ2 - Combustible Gas, Smoke
# MQ3 - Alcohol Vapor
# MQ5 - LPG, Natural Gas, Town Gas
# MQ9 - Carbon Monoxide, Coal Gas, Liquefied Gas
# 02 - Oxygen
# The sensitivity can be adjusted by the onboard potentiometer
#
# http://www.seeedstudio.com/wiki/Grove_-_Gas_Sensor
# http://www.seeedstudio.com/wiki/Grove_-_Gas_Sensor(MQ5)
# http://www.seeedstudio.com/wiki/Grove_-_Gas_Sensor(O%E2%82%82)

import time
import grovepi
import logging

# Connect the Grove Gas Sensor to analog port A0
# SIG,NC,VCC,GND
gas_sensor = 0

grovepi.pinMode(gas_sensor,"INPUT")

logging.basicConfig(filename='/var/log/pytemp/o2.log', filemode='a', format='%(created)f %(message)s', level=logging.INFO)

while True:
    try:
        # Get sensor value
        sensor_value = grovepi.analogRead(gas_sensor)

        # Calculate gas density - large value means more dense gas
#        density = (float)(sensor_value / 1024)
        density = (sensor_value / 1024.00)
        d_percentage = "{:.0%}".format(density)

#REFERENCE# VALID old style format
#        logging.info('Sensor value=%.02f and Density=%.02f% % and Density_p=%s '%(sensor_value, density, d_percentage))

#REFERENCE# AS of 2.6 style format
        logging.info('Sensor value={} and Density={} and Density_p={} ' .format(sensor_value, density, d_percentage))

#REFERNCE# AS of 3.6 style format
#SO Make sure either default is python3
#or , #!/usr/bin/env python3
#        logging.info( f'Sensor value={sensor_value} and Density={density} and Density_p={d_percentage}' )

        time.sleep(.5)

    except IOError:
        print ("Error")
