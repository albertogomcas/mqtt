import machine
import time
from dhtb import DHT12_I2C

# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
machine.deepsleep()

#'''Note that when the chip wakes from a deep-sleep it is completely reset,
#including all of the memory. The boot scripts will run as usual and you can put
#code in them to check the reset cause to perhaps do something different if the
#device just woke from a deep-sleep.'''

#if machine.reset_cause() == machine.DEEPSLEEP_RESET:
#    print('woke from a deep sleep')
#    time.sleep_ms(5000)
#    i2c = I2C(scl=Pin(5), sda=Pin(4), freq=20000)
#    d = DHT12_I2C(i2c, 92)
#    d.measure()
#    print(d.temperature(), d.humidity())

#else:
#    print('power on or hard reset')