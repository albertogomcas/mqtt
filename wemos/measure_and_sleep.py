import machine
import time
from dhtb import DHT12_I2C
import wemos
from umqtt.simple import MQTTClient

#'''Note that when the chip wakes from a deep-sleep it is completely reset,
#including all of the memory. The boot scripts will run as usual and you can put
#code in them to check the reset cause to perhaps do something different if the
#device just woke from a deep-sleep.'''

server = '192.168.1.103'

if machine.reset_cause() == machine.DEEPSLEEP_RESET:
    time.sleep_ms(10000)
    i2c = machine.I2C(scl=machine.Pin(wemos.PINS.D1), sda=machine.Pin(wemos.PINS.D2), freq=20000)
    d = DHT12_I2C(i2c, 92)
    d.measure()
    print(d.temperature(), d.humidity())

    try:
        c = MQTTClient("umqtt_client", server)
        c.connect()
        c.publish(b"sensor", b"T {} HUM {}".format(d.temperature(), d.humidity()))
        c.disconnect()
        time.sleep_ms(1000)
    except:
        pass
else:
    print('power on or hard reset')


# configure RTC.ALARM0 to be able to wake the device
rtc = machine.RTC()
rtc.irq(trigger=rtc.ALARM0, wake=machine.DEEPSLEEP)

# set RTC.ALARM0 to fire after 10 seconds (waking the device)
rtc.alarm(rtc.ALARM0, 10000)

# put the device to sleep
machine.deepsleep()