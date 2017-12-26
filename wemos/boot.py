# This file is executed on every boot (including wake-boot from deepsleep)
import esp
from wemos import PINS
esp.osdebug(None)
import gc
import webrepl
webrepl.start()
gc.collect()
import machine

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    print('woke from a deep sleep')
else:
    print('power on or hard reset')
    from safety_pin import probe_safety_pin
    if probe_safety_pin(PINS.D7):
        raise Exception("Safety pin is active")
    

import measure_and_sleep