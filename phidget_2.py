import csv
import datetime
import keyboard
import time

from Phidget22.Devices.Spatial import *
from Phidget22.PhidgetException import *

f_name='phidget_all_actuator_25.csv'

# Define the callback function that will be called when Spatial data is received
def onSpatialDataHandler(self, acceleration, angularRate, magneticField, timestamp):
    print("Acceleration: " + str(acceleration))
    print("Angular Rate: " + str(angularRate))
    print("Magnetic Field: " + str(magneticField))
    print("Timestamp: " + str(timestamp) + "\n")

    # Append the data to the CSV file
    with open(f_name, mode='a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([timestamp, datetime.datetime.now(), acceleration[0], acceleration[1], acceleration[2], angularRate[0], angularRate[1], angularRate[2], magneticField[0], magneticField[1], magneticField[2]])


# Create a Spatial Phidget object
spatial = Spatial()

# Open the Spatial Phidget and wait for it to be attached
try:
    spatial.openWaitForAttachment(5000)
except PhidgetException as e:
    print("Phidget Exception %i: %s" % (e.code, e.details))

# Set the data interval to 16ms (62.5Hz)
spatial.setDataInterval(100)

# Set the Spatial data callback function
spatial.setOnSpatialDataHandler(onSpatialDataHandler)

# Initialize the CSV file with header row
with open(f_name, mode='w') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(['Timestamp', 'Date/Time', 'Acceleration X', 'Acceleration Y', 'Acceleration Z', 'Angular Rate X', 'Angular Rate Y', 'Angular Rate Z', 'Magnetic Field X', 'Magnetic Field Y', 'Magnetic Field Z'])

# Loop until the user presses 'q' on the keyboard
while(True):
    if keyboard.is_pressed('q'):
        # Close the CSV file and exit the loop
        with open(f_name, mode='a') as csv_file:
            csv_file.close()
        break
    time.sleep(0.1)

# Close the Spatial Phidget
spatial.close()
