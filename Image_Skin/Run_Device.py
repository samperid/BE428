import requests
import time
from neopixel import *
import argparse
import smbus
import time
import numpy as np
'''
from plotly import plotly
import plotly.graph_objs as go
from plotly.offline import download_plotlyjs, init_notebook_mode, plot, iplot
'''

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53


def wavelength_to_rgb(wavelength, gamma=0.8):

    '''This converts a given wavelength of light to an 
    approximate RGB color value. The wavelength must be given
    in nanometers in the range from 380 nm through 750 nm
    (789 THz through 400 THz).

    Based on code by Dan Bruton
    http://www.physics.sfasu.edu/astro/color/spectra.html
    '''

    wavelength = float(wavelength)
    if wavelength >= 380 and wavelength <= 440:
        attenuation = 0.3 + 0.7 * (wavelength - 380) / (440 - 380)
        R = ((-(wavelength - 440) / (440 - 380)) * attenuation) ** gamma
        G = 0.0
        B = (1.0 * attenuation) ** gamma
    elif wavelength >= 440 and wavelength <= 490:
        R = 0.0
        G = ((wavelength - 440) / (490 - 440)) ** gamma
        B = 1.0
    elif wavelength >= 490 and wavelength <= 510:
        R = 0.0
        G = 1.0
        B = (-(wavelength - 510) / (510 - 490)) ** gamma
    elif wavelength >= 510 and wavelength <= 580:
        R = ((wavelength - 510) / (580 - 510)) ** gamma
        G = 1.0
        B = 0.0
    elif wavelength >= 580 and wavelength <= 645:
        R = 1.0
        G = (-(wavelength - 645) / (645 - 580)) ** gamma
        B = 0.0
    elif wavelength >= 645 and wavelength <= 750:
        attenuation = 0.3 + 0.7 * (750 - wavelength) / (750 - 645)
        R = (1.0 * attenuation) ** gamma
        G = 0.0
        B = 0.0
    else:
        R = 0.0
        G = 0.0
        B = 0.0
    R *= 255
    G *= 255
    B *= 255
    return (int(R), int(G), int(B))


# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

#Prompt user input
user = raw_input("Please Insert File Name: ")
check = raw_input("When device placed over skin insert 'R' to begin: ")

if check == "R":

    #Assign array of 15 for wavelength values, and for corresponding intensities 
    wavelengths = np.zeros(16)
    Full_Spectrum = np.zeros(16)
    Infared_Value = np.zeros(16)
    Visible_Value = np.zeros(16)

    for i in range(16):
        add = i * 20
        wavelengths[i] = 400 + add 
    
    #Iterate through each wavelength
    counter = 0
    for l in wavelengths:
        #Calculate R,G,B Concentration for Wavlength 
        R,G,B = wavelength_to_rgb(l)
        for i in range(12):
            wait_ms = 50
            strip.setPixelColor(i,Color(G,R,B))
            strip.show()
            time.sleep(wait_ms/1000.0)
        
        # Get I2C bus
        bus = smbus.SMBus(1)

        # TSL2561 address, 0x39(57)
        # Select control register, 0x00(00) with command register, 0x80(128)
        #		0x03(03)	Power ON mode
        bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
        # TSL2561 address, 0x39(57)
        # Select timing register, 0x01(01) with command register, 0x80(128)
        #		0x02(02)	Nominal integration time = 402ms
        bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

        time.sleep(0.5)

        # Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
        # ch0 LSB, ch0 MSB
        data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

        # Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
        # ch1 LSB, ch1 MSB
        data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

        # Convert the data
        ch0 = data[1] * 256 + data[0]
        ch1 = data1[1] * 256 + data1[0]

        #Store intensity values in corresponding arrays
        Full_Spectrum[counter] = ch0
        Infared_Value[counter] = ch1
        Visible_Value[counter] = ch0-ch1

        #Increment counter
        counter = counter + 1
    
    '''
    print("Full Spectrum")
    print(Full_Spectrum)
    print("Infared Value")
    print(Infared_Value)
    print("Visible Value")
    print(Visible_Value)
    '''

    for i in range(12):
        wait_ms = 50
        strip.setPixelColor(i,Color(0,0,0))
        strip.show()
        time.sleep(wait_ms/1000.0)

    
    #Create Trace for Each Spectrum 
    trace_FS = go.Scatter(
        x = wavelengths,
        y = Full_Spectrum,
        mode = 'lines+markers',
        name = 'Full Spectrum'
    )

    trace_IV = go.Scatter(
        x = wavelengths,
        y = Infared_Value,
        mode = 'lines+markers',
        name = 'Infrared Value'
    )

    trace_VS = go.Scatter(
        x = wavelengths,
        y = Visible_Value,
        mode = 'lines+markers',
        name = 'Full Spectrum'
    )

    data = [trace_FS,trace_IV,trace_VS]
    
    layout = go.Layout(
        title='Imaging Results',
        xaxis=dict(
            title='Wavelength (nm)'
        ),
        yaxis=dict(
            title='Light Intensity (lux)'
        )
    )

    fig = go.Figure(data=data, layout=layout)
    plot(fig, filename='Graphs/%s.html' % user)

else:
    print("Error Aborting Reading")

#Plotting Function
'''
trace1 = go.Scatter(
    x=store_t,
    y=store_mols_1,
    mode = 'lines+markers',
    name = 'E.Coli'
)


trace2 = go.Scatter(
    x=store_t,
    y=store_mols_2,
    mode = 'lines+markers',
    name = 'Dead E.Coli'
)

trace3 = go.Scatter(
    x=store_t,
    y=store_mols_3,
    mode = 'lines+markers',
    name = 'Antibiotic Resistant E.Coli'
)


trace4 = go.Scatter(
    x=store_t,
    y=store_mols_4,
    mode = 'lines+markers',
    name = 'A'
)


data = [trace1,trace2,trace3]

layout = go.Layout(
    title='Carbenicillin Simulation Results',
    xaxis=dict(
        title='Time'
    ),
    yaxis=dict(
        title='Number of Cells'
    )
)

fig = go.Figure(data=data, layout=layout)
plot(fig, filename='Graphs/gillespie_automated.html')
'''


#Example Code Running Sensor/LED Ring
'''
##############################################################################################################################

#Green 
for i in range(12):
    wait_ms = 50
    strip.setPixelColor(i,Color(255,0,0))
    strip.show()
    time.sleep(wait_ms/1000.0)

# Get I2C bus
bus = smbus.SMBus(1)

# TSL2561 address, 0x39(57)
# Select control register, 0x00(00) with command register, 0x80(128)
#		0x03(03)	Power ON mode
bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
# TSL2561 address, 0x39(57)
# Select timing register, 0x01(01) with command register, 0x80(128)
#		0x02(02)	Nominal integration time = 402ms
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

# Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
# ch0 LSB, ch0 MSB
data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

# Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
# ch1 LSB, ch1 MSB
data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

# Convert the data
ch0 = data[1] * 256 + data[0]
ch1 = data1[1] * 256 + data1[0]

# Output data to screen
print("\n")
print("Green Light")
print("Full Spectrum(IR + Visible) :%d lux" %ch0)
print("Infrared Value :%d lux" %ch1)
print("Visible Value :%d lux" %(ch0 - ch1))
print("\n")

time.sleep(5)

##############################################################################################################################

#Red
for i in range(12):
    wait_ms = 50
    strip.setPixelColor(i,Color(0,255,0))
    strip.show()
    time.sleep(wait_ms/1000.0)

# Get I2C bus
bus = smbus.SMBus(1)

# TSL2561 address, 0x39(57)
# Select control register, 0x00(00) with command register, 0x80(128)
#		0x03(03)	Power ON mode
bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
# TSL2561 address, 0x39(57)
# Select timing register, 0x01(01) with command register, 0x80(128)
#		0x02(02)	Nominal integration time = 402ms
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

# Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
# ch0 LSB, ch0 MSB
data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

# Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
# ch1 LSB, ch1 MSB
data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

# Convert the data
ch0 = data[1] * 256 + data[0]
ch1 = data1[1] * 256 + data1[0]

# Output data to screen
print("Red Light")
print("Full Spectrum(IR + Visible) :%d lux" %ch0)
print("Infrared Value :%d lux" %ch1)
print("Visible Value :%d lux" %(ch0 - ch1))
print("\n")

time.sleep(5)

##############################################################################################################################

#Blue
for i in range(12):
    wait_ms = 50
    strip.setPixelColor(i,Color(0,0,255))
    strip.show()
    time.sleep(wait_ms/1000.0)

# Get I2C bus
bus = smbus.SMBus(1)

# TSL2561 address, 0x39(57)
# Select control register, 0x00(00) with command register, 0x80(128)
#		0x03(03)	Power ON mode
bus.write_byte_data(0x39, 0x00 | 0x80, 0x03)
# TSL2561 address, 0x39(57)
# Select timing register, 0x01(01) with command register, 0x80(128)
#		0x02(02)	Nominal integration time = 402ms
bus.write_byte_data(0x39, 0x01 | 0x80, 0x02)

time.sleep(0.5)

# Read data back from 0x0C(12) with command register, 0x80(128), 2 bytes
# ch0 LSB, ch0 MSB
data = bus.read_i2c_block_data(0x39, 0x0C | 0x80, 2)

# Read data back from 0x0E(14) with command register, 0x80(128), 2 bytes
# ch1 LSB, ch1 MSB
data1 = bus.read_i2c_block_data(0x39, 0x0E | 0x80, 2)

# Convert the data
ch0 = data[1] * 256 + data[0]
ch1 = data1[1] * 256 + data1[0]

# Output data to screen
print("Blue Light")
print("Full Spectrum(IR + Visible) :%d lux" %ch0)
print("Infrared Value :%d lux" %ch1)
print("Visible Value :%d lux" %(ch0 - ch1))
print("\n")

time.sleep(5)

##############################################################################################################################

#Turn Off
for i in range(12):
    wait_ms = 50
    strip.setPixelColor(i,Color(0,0,0))
    strip.show()
    time.sleep(wait_ms/1000.0)
'''