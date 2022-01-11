import cv2

img = cv2.imread('Images/photo.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.Canny(img, 40, 40)

cv2.imshow('Result', img)
cv2.waitKey(0)