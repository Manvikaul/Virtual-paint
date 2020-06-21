# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 11:51:40 2020

@author: DELL
"""

import cv2
import numpy as np

frameWidth = 640
frameHeight = 480
cap = cv2.VideoCapture(0)
cap.set(3, frameWidth)
cap.set(4, frameHeight)
cap.set(10,150)

myColors = [[158,179,113,255,114,255],        #red
            [64,120,106,255,116,255]]     #blue

myColorValues = [[51,153,255],          ## BGR
                 [255,0,255],
                 [0,255,0],
                 [255,0,0]]

def findColor(img,myColors):
    imgHSV = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    for color in myColors:
        lower = np.array(color[0:3])
        upper = np.array(color[3:6])
        mask = cv2.inRange(imgHSV,lower,upper)
        cv2.imshow(str(color[0]),mask)

while True:
    success, img = cap.read()
    findColor(img,myColors)
    cv2.imshow("Result", img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

 