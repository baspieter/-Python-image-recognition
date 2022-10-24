import numpy as np
import cv2 as cv
# Exercise 3B show contour

def showContour():
    img = cv.imread('images/tek1.png')

    # Convert BGR to HSV
    hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
    # define range of red color in HSV
    lower_red = np.array([0, 150, 150])
    upper_red = np.array([20, 255, 255])
    # Threshold the HSV image to get only blue colors
    mask = cv.inRange(hsv, lower_red, upper_red)
    # Find contours in given mask
    contours, hierarchy = cv.findContours(mask, cv.RETR_TREE, cv.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv.contourArea(cnt)
        # Draw only contours with a higher area (oppervlakte) than 100
        if area > 100:
            # Draw circle in middle of contour.
            m = cv.moments(cnt)
            cx = int(m['m10'] / m['m00'])
            cy = int(m['m01'] / m['m00'])
            cv.circle(img, (cx, cy), 2, (0, 0, 255), -1)

            # Draw hull (Hull means the shape of the object.)
            hull = cv.convexHull(cnt)
            cv.drawContours(img, [hull], -1, (0, 255, 255), 3)

    cv.imshow('tek1', img)
    k = cv.waitKey(0)
    print(k)
    cv.destroyAllWindows()

showContour()