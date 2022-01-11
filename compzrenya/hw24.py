import numpy as np
import cv2

img = cv2.imread('Images/photo.jpg', 1)
cv2.imshow('Original', img)

kernel = np.ones((5, 5), 'uint8')

eroziya_img = cv2.erode(img, kernel, iterations=1)
cv2.imshow('Eroziya', eroziya_img)
cv2.waitKey(0)
cv2.destroyAllWindows()