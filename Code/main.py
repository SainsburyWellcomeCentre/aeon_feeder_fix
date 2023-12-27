import utime
from machine import Pin, ADC

sensor = ADC(0)
out = Pin(1, Pin.OUT)
led = Pin(14, Pin.OUT)

READY = 0
PULSE = 1
BROKEN = 2

THRESHOLD = 30000
PULSE_INTERVAL = 3
SETTLE_INTERVAL = 300
BEAM_BURST_THRESHOLD = 3

state = READY
pulse_counter = 0
settle_counter = 0
beam_burst_counter = 0

while True:
    led.value(1)
    reading = sensor.read_u16()
    led.value(0)
    beam_active = reading < THRESHOLD
    if state == READY:
        if beam_active:
            state = PULSE
            pulse_counter = PULSE_INTERVAL
            settle_counter = SETTLE_INTERVAL
            beam_burst_counter = beam_burst_counter + 1
            out.value(1)
        else:
            settle_counter = settle_counter - 1
            if settle_counter <= 0:
                beam_burst_counter = 0
                settle_counter = 0
    elif state == PULSE:
        pulse_counter = pulse_counter - 1
        if pulse_counter <= 0:
            state = READY if beam_burst_counter < BEAM_BURST_THRESHOLD else BROKEN
            out.value(0)
    else:
        settle_counter = SETTLE_INTERVAL if beam_active else settle_counter - 1
        if settle_counter <= 0:
            state = READY
            beam_burst_counter = 0
    utime.sleep(0.003)