import numpy as np
import cv2 as cv
import math

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




    

def showContour():
    img = cv.imread('images/tek1.png')

    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_red = np.array([0,150,150])
    upper_red = np.array([20,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_red, upper_red)
    
    imgray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgblur = cv.GaussianBlur(imgray,(5,5),0)
    ret,thresh = cv.threshold(imgblur, 0, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        # teken alleen contouren met een oppervlakte groter dan 100
        if area > 100:
            hull = cv.convexHull(cnt)
            M = cv.moments(cnt)
            cx = int(M['m10']/M['m00'])
            cy = int(M['m01']/M['m00'])
            cv.circle(img,(cx,cy), 2, (0,0,255), -1)
            cv.drawContours(img, [hull], -1, (0,255,255), 3)


    M = cv.moments(cnt)
    hull = cv.convexHull(cnt)

    cv.imshow('tek1', img)
    k = cv.waitKey(0)
    print(k)
    cv.destroyAllWindows()
    

    
showContour()
















