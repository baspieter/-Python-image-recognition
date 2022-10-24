import cv2 as cv
import math
# Exercise 4 bouten en moeren
    
def showBouten():
    img = cv.imread('images/bouten_moeren1.jpg')
    imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    imgBlur = cv.GaussianBlur(imgGray,(5,5),0)
    ret,th = cv.threshold(imgBlur, 180, 255, cv.THRESH_BINARY_INV)
    contours, hierarchy = cv.findContours(th,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)

    hierarchy = hierarchy[0]
    for cnr in range(len(contours)):
        cnt = contours[cnr]
        # Get area (oppervlakte)
        area = cv.contourArea(cnt)
        # Get perimeter (omtrek)
        perimeter = cv.arcLength(cnt, True)
        # Calculate factor.
        factor = 4 * math.pi * area / perimeter**2
        holes = 0
        child = hierarchy[cnr][2]
        while child >= 0:
            holes += cv.contourArea(contours[child])
            child = hierarchy[child][0]

        # Check if contour matches green shapes objects. Draw it on image.
        if factor < 0.36:
            cv.drawContours(img, [cnt], -1, (0,255,0), 3)
        # Check if contour matches the blue shaped objects Draw it on image.
        elif factor > 0.36 and factor < 0.8:
            cv.drawContours(img, [cnt], -1, (255,0,0), 3)
        # Check if contour matches the red shaped objects. Extra check if there are any holes. The red shapes are the only ones with holes. Draw it on image.
        elif factor > 0.8 and factor < 0.87 and holes != 0:
            cv.drawContours(img, [cnt], -1, (0,0,255), 3)
        # Check if contour matches the yellow shaped objects. Draw it on image.
        elif factor > 0.8 and factor < 0.87:
            cv.drawContours(img, [cnt], -1, (0,255,255), 3)
        

    cv.imshow('bouten_moeren1', img)
    k = cv.waitKey(0)
    print(k)
    cv.destroyAllWindows()

showBouten()
