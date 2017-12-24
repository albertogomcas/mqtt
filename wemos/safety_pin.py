from machine import Pin

def probe_safety_pin(pin):

    safety_pin = Pin(pin, Pin.IN, Pin.PULL_UP)
    return not safety_pin()
    