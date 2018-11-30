"""
The script runs with DHT11 temperature and humidity sensor
"""

from datetime import datetime
import sys
import Adafruit_DHT

SENSOR = Adafruit_DHT.DHT11
GPIO = 4

HUMIDITY, TEMPERATURE = Adafruit_DHT.read_retry(SENSOR, GPIO)

RUN_TIME = sys.stdout

class STAMP:
    """
    Setting up timestamps
    """
NL = True

def write(self, message):
    """
    Add timestamp to stdout
    """

    if message == "\n":
        RUN_TIME.write(message)
        self.NL = True
    elif self.NL:
        RUN_TIME.write("%s >>> %s" % (str(datetime.now().strftime("%Y-%m-%d %H:%M:%S")), message))
        self.NL = False
    else:
        RUN_TIME.write(message)

sys.stdout = STAMP()

if TEMPERATURE is not None and HUMIDITY is not None:
    print "Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(TEMPERATURE, HUMIDITY)
else:
    print "Failed to get data. Try again!"
