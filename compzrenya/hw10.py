import cv2
import numpy as np

img = cv2.imread('Images/photo.jpg')

def tranform(img_param, x ,y):
    mat = np.float32([[1, 0, x], [0, 1, y]])
    return cv2.warpAffine(img_param, mat, (img_param.shape[1], img_param.shape[0]))

img = tranform(img, 10, 0)

cv2.imshow('Result', img)
cv2.waitKey(0)