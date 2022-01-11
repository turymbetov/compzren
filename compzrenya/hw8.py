import cv2

img = cv2.imread('Images/photo.jpg')

def rotate(img_param,angle):
    height, width = img.shape[:2]
    point = (width // 2, height // 2)
    mat = cv2.getRotationMatrix2D(point, angle, 1)
    return cv2.warpAffine(img_param, mat, (width, height))

img = rotate(img, 45)

cv2.imshow('Result', img)
cv2.waitKey(0)