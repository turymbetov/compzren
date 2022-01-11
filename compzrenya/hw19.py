import cv2

img = cv2.imread('Images/photo.jpg')

img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img = cv2.GaussianBlur(img, (9, 9), 0)
img = cv2.Canny(img, 100, 130)

con, hir = cv2.findContours(img, cv2.RETR_LIST, cv2.CHAIN_APPROX_NONE)

print(con)

cv2.imshow('Result', img)
cv2.waitKey(0)