import time
import os

def initpin(pinnum, mode):
    '''
    pinnum: pin number, eg. 172, 175 etc.
    mode: pin mode, valid values: in or out
    '''
    with open('/sys/class/gpio/export' , 'w') as f:
        f.write(str(pinnum))

    with open('/sys/class/gpio/gpio' + str(pinnum) + '/direction', 'w') as f:
        f.write(str(mode))


def setpin(pinnum, value):
    with open('/sys/class/gpio/gpio' + str(pinnum) + '/value', 'w') as f:
        f.write(str(value))

if __name__ == '__main__':
    initpin(75, 'out')
    while True:
        setpin(75, 0)
        time.sleep(1)
        setpin(75, 1)
        time.sleep(1)

