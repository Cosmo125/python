import time

def initpin(pinnum, mode):
    '''
    pinnum: pin number, eg. 172, 175 etc.
    mode: pin mode, valid values: in or out
    '''
    try:
        with open('/sys/class/gpio/export' , 'w') as f:
            
                f.write(str(pinnum))
                
    except OSError:
        print("Ya se ejecuto correctamente")
 

    with open('/sys/class/gpio/gpio' + str(pinnum) + '/direction', 'w') as f:
        f.write(str(mode))


def setpin(pinnum, value):
    with open('/sys/class/gpio/gpio' + str(pinnum) + '/value', 'w') as f:
        f.write(str(value))
def closedpin(pinnum):
    with open('/sys/class/gpio/gpio' + str(pinnum) + '/value', 'w') as f:
        f.write(str(0))
        
if __name__ == '__main__':
    initpin(157, 'out')
    a=0
    while True:
        a+=1
        if a<5:
            setpin(157, 0)
            time.sleep(1)
            setpin(157, 1)
            time.sleep(1)
            print(a)
        else:
            closedpin(157)
            break
