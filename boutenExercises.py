import numpy as np
import cv2 as cv
import math
    
def showBouten():
    img = cv.imread('images/bouten_moeren1.jpg')
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray,(5,5),0)
    ret,th = cv.threshold(imgBlur, 180, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(th,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    hierarchy = hierarchy[0]
    for cnr in range(len(contours)):
        cnt = contours[cnr]
        area = cv.contourArea(cnt)
        perimeter = cv.arcLength(cnt, True)
        factor = 4 * math.pi * area / perimeter**2
        holes = 0
        child = hierarchy[cnr][2]
        while child >= 0:
            holes += cv.contourArea(contours[child])
            child = hierarchy[child][0]

        if factor < 0.36:
            cv.drawContours(img, [cnt], -1, (0,255,0), 3) #GREEN
        elif factor > 0.36 and factor < 0.8:
            cv.drawContours(img, [cnt], -1, (255,0,0), 3) #BLUE
        elif factor > 0.8 and factor < 0.87 and hierarchy[cnr][2] != -1:
            cv.drawContours(img, [cnt], -1, (0,0,255), 3) #RED
        elif factor > 0.8 and factor < 0.87:
            cv.drawContours(img, [cnt], -1, (0,255,255), 3) #YELLOW
        

    #Output
    cv.imshow('bouten_moeren1', img)
    k = cv.waitKey(0)
    print(k)
    cv.destroyAllWindows()

showBouten()
