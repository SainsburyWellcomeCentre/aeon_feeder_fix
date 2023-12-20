from machine import Pin, Timer, ADC
import utime

sensor = ADC(0)
out = Pin(1, Pin.OUT)
led = Pin(14, Pin.OUT)

#tim = Timer()

#def tick(timer):
#    global led
#    led.toggle()

#tim.init(freq=1000, mode=Timer.PERIODIC, callback=tick)
count = 0
conversion_factor = 3.3 / (65535)
ready = 0

while True:
    led.value(1)
    reading = sensor.read_u16()# * conversion_factor
    led.value(0)
    if reading < 30000:
        ready = 3
        out.value(1)
        count=count+1
    elif ready > 1:
        ready = ready - 1
    else:
        out.value(0)
        ready = 0
#    print(reading)
    print(count)
    utime.sleep(0.003)