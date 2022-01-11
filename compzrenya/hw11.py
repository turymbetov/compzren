import cv2
import numpy as np

img = cv2.imread('Images/photo.jpg')

hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV) #convert it to hsv

h, s, v = cv2.split(hsv)
v += 75
final_hsv = cv2.merge((h, s, v))

img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
cv2.imwrite("image_processed.jpg", img)

cv2.imshow('Result', img)
cv2.waitKey(0)