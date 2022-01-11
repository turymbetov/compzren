import cv2

img = cv2.imread('Images/photo.jpg')

img = cv2.GaussianBlur(img, (9, 9), 0)

cv2.imshow('Result', img)
cv2.waitKey(0)