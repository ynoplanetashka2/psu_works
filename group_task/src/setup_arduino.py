import serial
import time

#connecting to arduino
def setup_arduino(arduino_port_val, timeout, baudrate=9600):
    arduino = serial.Serial(port=arduino_port_val, baudrate=baudrate, timeout=timeout)
    time.sleep(timeout + 3)
    return arduino

class __Arduino_mock:
    def write(*args):
        return ''
    def readline():
        return 'lineread'

#mock setup
def setup_arduino_mock(arduino_port_val, timeout, *args):
    time.sleep(timeout + 3)

    return __Arduino_mock()
