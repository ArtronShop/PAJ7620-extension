from machine import Pin
from machine import I2C
from time import sleep

WAVE = 1 << 8
COUNTER_CLOCKWISE = 1 << 7
CLOCKWISE = 1 << 6
BACKWORD = 1 << 5
FORWARD = 1 << 4
RIGHT = 1 << 3
LEFT = 1 << 2
DOWN = 1 << 1
UP = 1 << 0

PAJ7620_ADDR = 0x73

i2c1 = I2C(1, scl=Pin(5), sda=Pin(4), freq=100000)

def setup():
    init = [ (0xEF, b'\x01'), (0x72, b'\x01'), (0xEF, b'\x00') ]
    for c in init:
        i2c1.writeto_mem(PAJ7620_ADDR, c[0], c[1])

def read():
    d = i2c1.readfrom_mem(PAJ7620_ADDR, 0x43, 2)
    return d[0]|(d[1] << 8)

gestureSave = 0
def isGesture(g):
    global gestureSave
    gestureSave = gestureSave | read()
    check = True if g & gestureSave else False
    gestureSave = gestureSave & (~g)
    return check

setup()
