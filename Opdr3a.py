import numpy as np
import cv2 as cv
# Exercise 3 cut in an image

def showBlue():
    frame = cv.imread('images/tek1.png')
    while True:
        # Convert BGR to HSV
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        # define range of blue color in HSV. In this case only look at first value of both arrays.
        lower_blue = np.array([110,50,50])
        upper_blue = np.array([130,255,255])
        # Threshold the HSV image to get only blue colors
        mask = cv.inRange(hsv, lower_blue, upper_blue)
        # Grab original picture and mask found object
        res = cv.bitwise_and(frame,frame, mask= mask)
        # Show mask only
        cv.imshow('res', res)

        # Close window with Q after one second.
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # Destroy windows when loop has ended
    cv.destroyAllWindows()

def showGreen():
    frame = cv.imread('images/tek1.png')
    while True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_green = np.array([40,50,50])
        upper_green = np.array([80,255,255])
        mask = cv.inRange(hsv, lower_green, upper_green)
        res = cv.bitwise_and(frame,frame, mask= mask)
        cv.imshow('res',res)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()

def showRed():
    frame = cv.imread('images/tek1.png')
    while True:
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_red = np.array([0,150,150])
        upper_red = np.array([20,255,255])
        mask = cv.inRange(hsv, lower_red, upper_red)
        res = cv.bitwise_and(frame,frame, mask= mask)
        cv.imshow('frame',frame)
        cv.imshow('mask',mask)
        cv.imshow('res',res)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    cv.destroyAllWindows()

showBlue()