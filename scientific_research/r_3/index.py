import serial
import time
from pencil_recognize_color import color_diff, ColorIdentifier
import numpy as np
import cv2 as cv


arduino = serial.Serial(port='COM6', baudrate=9600, timeout=.1)
def write_read(val):
    arduino.write(bytes(str(val), 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline().decode('ascii')
    return data

def wr(val):
    arduino.write(bytes(str(val), 'utf-8'))
    print(val)

#while True:
    #angle = int(input('enter angle: '))
    #wr(angle)
    #time.sleep(5)

iteration_time = 5
fps = 30
time_per_frame = 1000 // fps
vid_cap = cv.VideoCapture(1)
pencil_boundaries = ((320, 380), (400, 400))
colorIdentifier = ColorIdentifier(vid_cap, pencil_boundaries)
frame_number = 0

RED = np.array([0, 0, 255])
BLUE = np.array([255, 0, 0])
GREEN = np.array([0, 255, 0])

CLRS_COUNT = 3
clrs = np.empty((CLRS_COUNT, 3), np.int16)
clrs[0,:] = RED
clrs[1,:] = BLUE
clrs[2,:] = GREEN
clrs_list = [RED, BLUE, GREEN]
clrs_names = (
    'RED',
    'BLUE',
    'GREEN'
)

clrs_to_angles = {
    'RED': -20,
    'BLUE': 20,
    'GREEN': -40
}
#clrs_to_angles = np.empty((CLRS_COUNT, 4), np.int16)
#clrs_to_angles[:, :3] = clrs
#clrs_to_angles[0, 3] = 0
#clrs_to_angles[1, 3] = 40
#clrs_to_angles[2, 3] = -40

def recognize_clr(clr):
    clr_diff = np.array([color_diff(clr_case, clr) for clr_case in clrs_list])
    clr_index = np.argmin(clr_diff)
    return clrs_names[clr_index]

while True:
    avg_clr = colorIdentifier.nextFrame()
    if frame_number % (fps * iteration_time) == 0:
        clr = recognize_clr(avg_clr)
        angle = clrs_to_angles[clr]
        wr(angle)
        print(clr)

    frame_number += 1
    if cv.waitKey(time_per_frame) == ord('q'):
        break
