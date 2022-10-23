import numpy as np
import cv2 as cv
# Exercise 3 cut in an image

def showBlue():
    frame = cv.imread('images/tek1.png')
    while(1):
        # Convert BGR to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        # Bitwise-AND mask and original image
        res = cv.bitwise_and(frame,frame, mask= mask)
        cv.imshow('frame',frame)
        cv.imshow('mask',mask)
        cv.imshow('res',res)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()

def showGreen():
    frame = cv.imread('images/tek1.png')
    while(1):
        # Convert BGR to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_red = np.array([170,50,50])
        upper_red = np.array([180,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_red, upper_red)
        # Bitwise-AND mask and original image
        res = cv.bitwise_and(frame,frame, mask= mask)
        cv.imshow('frame',frame)
        cv.imshow('mask',mask)
        cv.imshow('res',res)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()

def showRed():
    frame = cv.imread('images/tek1.png')
    while(1):
        # Convert BGR to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # define range of blue color in HSV
        lower_red = np.array([0,150,150])
        upper_red = np.array([20,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_red, upper_red)
        # Bitwise-AND mask and original image
        res = cv.bitwise_and(frame,frame, mask= mask)
        cv.imshow('frame',frame)
        cv.imshow('mask',mask)
        cv.imshow('res',res)
        k = cv.waitKey(5) & 0xFF
        if k == 27:
            break
    cv.destroyAllWindows()

showRed()