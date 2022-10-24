import cv2
# Exercise 1 show image

def test1():
    img = cv2.imread('images/tek1.png')
    cv2.imshow('logo', img)
    # Waits till user hits key
    cv2.waitKey(0)
    cv2.destroyAllWindows()

test1()
