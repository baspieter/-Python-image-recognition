import numpy as np
import sys
import cv2 as cv
import math
np.set_printoptions(threshold=sys.maxsize)
# Exercise 5 dobbelstenen

# Created separate function to display image. Helps with testing.
def displayImage(image):
    cv.namedWindow('image')
    cv.imshow('image', image)
    cv.waitKey(0)
    cv.destroyWindow('image')
    cv.waitKey(1)

def showDobbelstenen():
    img = cv.imread('images/dobbelstenen.png')
    # Prepare image
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray, (5, 5), 0)
    # Filter image with threshold.
    ret, th = cv.threshold(imgBlur, 30, 40, cv.THRESH_TRUNC)
    # Find dice contours
    dobbelsteen_contours, hierarchy = cv.findContours(th, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    # Set counting variables.
    dobbelstenen = 0
    dobbelsteen_ogen = 0

    for c in dobbelsteen_contours:
        dobbelstenen += 1

        # Get position about current dice.
        (x, y, w, h) = cv.boundingRect(c)
        # Create new image with only current dice.
        dobbelsteen = img[y:y+h, x:x+w]
        # Prepare dice image.
        dobbelsteenGray = cv.cvtColor(dobbelsteen, cv.COLOR_RGB2GRAY)
        # Threshold dice image so eyes on dice are better detectable.
        ret2, dobbelsteen2 = cv.threshold(dobbelsteenGray, 190, 255, cv.THRESH_BINARY)
        # Find contours (eyes)
        contours_in_dobbelsteen, hierarchy = cv.findContours(dobbelsteen2, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

        # Loop through contours.
        for cnr_in_dobbelsteen in contours_in_dobbelsteen:
            # Calculate factor with oppervlakte & omtrek. A perfect round object has factor of 1.
            # Because of filtering the image, some eye circles have been changed
            perimeter = cv.arcLength(cnr_in_dobbelsteen, True)
            area = cv.contourArea(cnr_in_dobbelsteen)
            if perimeter > 0 and area > 0:
                factor = 4 * math.pi * area / perimeter ** 2
                # The contour is a die eye whenever the factor is above 0.81
                if factor > 0.81:
                    # Optionally, draw contours in dice image.
                    # cv.drawContours(dobbelsteen, [cnr_in_dobbelsteen], -1, (255, 0, 0), 3)
                    dobbelsteen_ogen += 1

        # Optionally, show contours in dice image.
        # displayImage(dobbelsteen)

    print('Aantal dobbelstenen:', dobbelstenen)
    print('Dobbelstenen bij elkaar op geteld:', dobbelsteen_ogen)

showDobbelstenen()