import cv2

img = cv2.imread('Images/photo.jpg')


hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)
h += 70
final_hsv = cv2.merge((h, s, v))
img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)

cv2.imshow("IMG", img)
cv2.waitKey(0)