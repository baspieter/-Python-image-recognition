import numpy as np
import sys
import cv2 as cv
import math
np.set_printoptions(threshold=sys.maxsize)

def displayImage(image):
    cv.namedWindow('image')
    cv.imshow('image',image)
    cv.waitKey(0)
    cv.destroyWindow('image')
    cv.waitKey(1)

def showDobbelstenen(count=None):
    img = cv.imread('images/dobbelstenen.png')
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 0)
    ret, th = cv.threshold(imgBlur, 30, 40, cv.THRESH_TRUNC)
    dobbelsteen_contours, hierarchy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    dobbelstenen = 0
    dobbelsteen_ogen = 0

    for c in dobbelsteen_contours:
        dobbelstenen += 1

        (x, y, w, h) = cv.boundingRect(c)
        dobbelsteen = img[y:y+h, x:x+w]
        dobbelsteenGray = cv.cvtColor(dobbelsteen, cv.COLOR_RGB2GRAY)

        ret2, dobbelsteen2 = cv.threshold(dobbelsteenGray, 190, 255, cv.THRESH_BINARY)

        contours_in_dobbelsteen, hierarchy = cv.findContours(dobbelsteen2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)
        for cnr_in_dobbelsteen in contours_in_dobbelsteen:
            perimeter = cv.arcLength(cnr_in_dobbelsteen, True)
            area = cv.contourArea(cnr_in_dobbelsteen)
            if perimeter > 0 and area > 0:
                factor = 4 * math.pi * area / perimeter ** 2
                if factor > 0.81:
                    # cv.drawContours(dobbelsteen, [cnr_in_dobbelsteen], -1, (255, 0, 0), 3)
                    dobbelsteen_ogen += 1

    print('Aantal dobbelstenen:', dobbelstenen)
    print('Dobbelstenen bij elkaar op geteld:', dobbelsteen_ogen)

showDobbelstenen()