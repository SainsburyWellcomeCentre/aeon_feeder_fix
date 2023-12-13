# Import standard library modules.
import uasyncio
from machine import Pin, ADC
import utime

# Import SWC library modules.
import usbcdc
import harpsync
from bbdevice import BbDevice

# Instance a CDC, a harpsync interface, and an LED.
stream = usbcdc.usbcdc(1)
sync = harpsync.harpsync(0)
led = Pin(25, Pin.OUT)

# Instance Beam Break peripherals
adc = ADC(4)#should be 0 - using 3 for testing without circuit
out = Pin(1, Pin.OUT)
bbled = Pin(14, Pin.OUT)

# Instance the device object and launch its application.
theDevice = BbDevice(stream, sync, led, adc, out, bbled)
uasyncio.run(theDevice.main())