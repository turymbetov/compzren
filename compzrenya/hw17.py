import cv2 as cv
import numpy as np

image = cv.imread("Images/photo.jpg")
hsv=cv.cvtColor(image,cv.COLOR_BGR2HSV)

brown_lo=np.array([10,0,0])
brown_hi=np.array([20,255,255])

mask=cv.inRange(hsv,brown_lo,brown_hi)

image[mask>0]=(255,5,10)

cv.imshow("Matches", image)
cv.waitKey(0)