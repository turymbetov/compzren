import cv2

img1 = cv2.imread('Images/photo.jpg', cv2.IMREAD_GRAYSCALE)

img1 = cv2.resize(img1, (300, 300), interpolation=cv2.INTER_AREA)
cv2.imshow('img1', img1)

ret, binary = cv2.threshold(img1, 175, 255, cv2.THRESH_BINARY)
ret, binaryinv = cv2.threshold(img1, 175, 255, cv2.THRESH_BINARY_INV)
ret, trunc = cv2.threshold(img1, 175, 255, cv2.THRESH_TRUNC)
ret, tozero = cv2.threshold(img1, 175, 255, cv2.THRESH_TOZERO)
ret, tozeroinv = cv2.threshold(img1, 175, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('binary', binary)
cv2.imshow('binaryinv', binaryinv)
cv2.imshow('trunc', trunc)
cv2.imshow('tozero', tozero)
cv2.imshow('tozeroinv', tozeroinv)
cv2.waitKey(0)