import cv2

img = cv2.imread('Images/photo.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


cv2.imshow('Result', img)
cv2.waitKey(0)