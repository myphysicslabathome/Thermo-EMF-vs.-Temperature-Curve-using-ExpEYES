''' Program for ET Curve by DAS1115
    using PT1000 and T-type thermocouple
    on 05/07/2024 
'''

# Establish Connection
import eyes17.eyes
p = eyes17.eyes.open()

# Import python libreary 
import time, math
import numpy as np
from eyes17.SENSORS import ADS1115 

# Define the function to mesaure the temperature
def temperature():
    """Function to measure the instanteneous temperature"""
    R0 = 1000                    # PT1000 (RTD Name)
    Alpha = 3.85/1000            # Temperature coefficient 
    t0 = time.time()             # Time initialization
    n = 1                        # NO of measurements for averaging
    Rsum = 0
    for x in range (0,n):        # Loop for averaging
        r = p.get_resistance()   # Measure the resistance in ohm
        Rsum = Rsum+r            # Sum of resistance
    R = Rsum/n                   # Average resistance
    T = (1/Alpha)*((R/R0)-1)     # Calculate Temperature from Resistance
    return T 


t0=time.time()                     # Time initialization
while True:
    T = temperature()    
    ADC = ADS1115.connect(p.I2C)   # Measure the ADC
    ADC.setGain('GAIN_SIXTEEN')    # options : 'GAIN_TWOTHIRDS','GAIN_ONE','GAIN_TWO','GAIN_FOUR','GAIN_EIGHT','GAIN_SIXTEEN'
    emf = ADC.readADC_SingleEnded(0) # ADC reading in Channel A0
    ts=time.time()                   # current time
    t=ts-t0                         # Time difference
    print("%4.2f" % t, "S", "%4.2f" % T, "°C", "  ","%4.2f" % emf,"mV")
    file = open ("ET.dat", "a") # Appending file
    file.write("{0:4.2f} {1:4.2f} {2:4.2f}\n".format(t,T,emf))
    time.sleep(20)

