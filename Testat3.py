import gpiozero
import time

if __name__ == '__main__':
    x=gpiozero.Motor(16,13,26)
    y=gpiozero.Motor(6,5,12)
    x.forward(0.25)
    time.sleep(2)
    x.backward(0.25)
    time.sleep(2)
    x.stop()
    time.sleep(1)
    y.forward(0.25)
    time.sleep(2)
    y.backward(0.25)
    time.sleep(2)
    y.stop()
    time.sleep(1)
    x.forward(0.25)
    y.forward(0.25)
    time.sleep(2)
    x.backward(0.25)
    y.backward(0.25)
    time.sleep(2)
    x.backward(0.5)
    y.backward(0.5)
    time.sleep(2)
    x.stop()
    y.stop()
    x.close()
    y.close()