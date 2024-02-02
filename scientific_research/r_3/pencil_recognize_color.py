import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from scipy.spatial import distance

def color_diff(color1, color2):
    return distance.euclidean(color1, color2)


class ColorIdentifier:
    def __init__(self, vid_cap, rect_boundaries):
        self._vid_cap = vid_cap
        self.rect_boundaries = rect_boundaries

    def __del__(self):
        self._vid_cap.release()

    def nextFrame(self):
        ret, img = self._vid_cap.read()

        rect_boundaries = self.rect_boundaries
        rect_width = np.abs(rect_boundaries[0][0] - rect_boundaries[1][0])
        rect_height = np.abs(rect_boundaries[0][1] - rect_boundaries[1][1])
        
        sub_img = img[rect_boundaries[0][1]:rect_boundaries[1][1], rect_boundaries[0][0]:rect_boundaries[1][0]]
        average_color = np.average(np.average(sub_img, axis = 0), axis = 0)
        cv.rectangle(img, *rect_boundaries, average_color, 4)
        cv.imshow('frame', img)

        return average_color

