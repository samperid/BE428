import time
from neopixel import *
import argparse
import smbus
import time

# LED strip configuration:
LED_COUNT      = 16      # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 255     # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()

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