import cv2

qwery_img = cv2.imread('Images/photo.jpg')
asdfg_img = cv2.imread('Images/photo2.jpg')

qwery_img_bw = cv2.cvtColor(qwery_img, cv2.COLOR_BGR2GRAY)
asdfg_img_bw = cv2.cvtColor(asdfg_img, cv2.COLOR_BGR2GRAY)

orb = cv2.ORB_create()

queryKeypoints, queryDescriptors = orb.detectAndCompute(qwery_img_bw, None)
trainKeypoints, trainDescriptors = orb.detectAndCompute(asdfg_img_bw, None)

matcher = cv2.BFMatcher()
matches = matcher.match(queryDescriptors, trainDescriptors)

final_img = cv2.drawMatches(qwery_img, queryKeypoints,
                            asdfg_img, trainKeypoints, matches[:20], None)

final_img = cv2.resize(final_img, (1000, 650))

cv2.imshow("Matches", final_img)
cv2.waitKey(0)