One can measure the sensitivity of a thermocouple by measuring the thermo-emf as a function of temperature and hence can estimate the room temperature. 
Here, we use ExpEYES as a real-time data acquisition system, an analog-to-digital converter (ADS1115) to measure the emf and a PT1000 sensor to measure temperature. 

Download the "ET_Curve.exe" file and run directly.

![ExpEYES](https://github.com/myphysicslabathome/Thermo-EMF-vs.-Temperature-Curve-using-ExpEYES/assets/175300150/37934e04-5e53-4eae-aab8-8b82c9b8f9f9)

Required Apparatus:
1. ExpEYES latest model (SEELAB 3.0, with I2C expansion bus)
2. Analog to digital converter (ADS1115)
3. Temperature Sensor (PT1000)
4. T/K-type thermocouple 
5. Jumper wires (with alligator clips, optional)
6. Glass beaker (100 ml)
6. Mini Immersion water heater (optional)


PROCEDURE :
1. Take 40 ml of hot water (temperature around 90 degrees Celsius)
2. Dip PT1000 and T/K-type thermocouple inside the hot water
3. Connect PT1000 between SEN and Ground
4. Connect 5V, GND, SCL, SDA of ExpEYES respectively with VCC, GND, SCL, SDA of ADS1115 
5. Connect ExpEYES with PC via USB cable
5. Run the Python script or .exe file 
6. Set the time interval (20 or 30 sec) according to you system
7. Time (sec), temperature (degree Celsius) and thermo-emf (mv) data will be displayed on the screen and saved in "ET.dat" file
8. Plot 2nd and 3rd column
9. Fit Linear to estimate the thermocouple sensitivity (slope) and room temperature (intercept)
10. Don't forget to delete the existing data file "ET.dat", if you are running the Python script or .exe file for multiple times.

Experimental Setup and Connections:
![Experimental Setup](https://github.com/myphysicslabathome/Thermo-EMF-vs.-Temperature-Curve-using-ExpEYES/assets/175300150/fa5fac3e-fe3e-40e1-a1d9-9284caa9c80a)
![Connections for ET Curve](https://github.com/myphysicslabathome/Thermo-EMF-vs.-Temperature-Curve-using-ExpEYES/assets/175300150/b239d757-05d3-4baf-9d44-49ee344cdc3d)

Results: 
![ET Curve](https://github.com/myphysicslabathome/Thermo-EMF-vs.-Temperature-Curve-using-ExpEYES/assets/175300150/454319d0-f009-40e3-b365-f841a9f26ccf)

NOTE :
A sample data ('T-type.dat') and the corresponding graph ('ET Curve.png') for t-type thermocouple is also provided for reference. 
Please see the 'Experimental Setup.jpeg' and 'Connections for ET Curve.jpeg' images for setup and connection. 

Acknowledgement:

Heartfelt thanks to Dr. Jithin B.P. from CSpark Research for his invaluable assistance and support. His expertise and guidance were instrumental in the successful completion of this project. Dr. Jithin, your unwavering help and dedication are deeply appreciated.

Thanks

Dr. Ujjwal Ghanta
