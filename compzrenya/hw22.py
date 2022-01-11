import numpy as np
import cv2


img = cv2.imread('Images/photo.jpg')


dft = np.fft.fft2(img, axes=(0,1))

dft_shift = np.fft.fftshift(dft)

mag = np.abs(dft_shift)
spec = np.log(mag) / 20

radius = 32
mask = np.zeros_like(img)
cy = mask.shape[0] // 2
cx = mask.shape[1] // 2
cv2.circle(mask, (cx,cy), radius, (255,255,255), -1)[0]
mask = 255 - mask

mask2 = cv2.GaussianBlur(mask, (19,19), 0)

dft_shift_masked = np.multiply(dft_shift,mask) / 255
dft_shift_masked2 = np.multiply(dft_shift,mask2) / 255

back_ishift = np.fft.ifftshift(dft_shift)
back_ishift_masked = np.fft.ifftshift(dft_shift_masked)
back_ishift_masked2 = np.fft.ifftshift(dft_shift_masked2)

img_back = np.fft.ifft2(back_ishift, axes=(0,1))
img_filtered = np.fft.ifft2(back_ishift_masked, axes=(0,1))
img_filtered2 = np.fft.ifft2(back_ishift_masked2, axes=(0,1))

img_back = np.abs(img_back).clip(0,255).astype(np.uint8)
img_filtered = np.abs(3*img_filtered).clip(0,255).astype(np.uint8)
img_filtered2 = np.abs(3*img_filtered2).clip(0,255).astype(np.uint8)


cv2.imshow("ORIGINAL", img)
cv2.imshow("SPECTRUM", spec)
cv2.imshow("MASK", mask)
cv2.imshow("MASK2", mask2)
cv2.imshow("ORIGINAL DFT/IFT ROUND TRIP", img_back)
cv2.imshow("FILTERED DFT/IFT ROUND TRIP", img_filtered)
cv2.imshow("FILTERED2 DFT/IFT ROUND TRIP", img_filtered2)
cv2.waitKey(0)
cv2.destroyAllWindows()

# write result to disk
cv2.imwrite("friends_dft_numpy_mask_highpass.png", mask)
cv2.imwrite("friends_dft_numpy_mask_highpass_blurred.png", mask2)
cv2.imwrite("friends_dft_numpy_roundtrip.png", img_back)
cv2.imwrite("friends_dft_numpy_highpass_filtered1.png", img_filtered)
cv2.imwrite("friends_dft_numpy_highpass_filtered2.png", img_filtered2)