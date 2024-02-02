import serial


arduino_port_val = 'COM7'
arduino = serial.Serial(port=arduino_port_val, baudrate=9600, timeout = .03)

#arduino messaging api
def wr(data):
    arduino.write(bytes(str(data), 'utf-8'))

def rd():
    data = arduino.readline()
    return data

while True:
    activePin = input('enter active pin index: ')
    activePin = int(activePin)
    wr(activePin)
    serial_read = rd()
    print(serial_read)
