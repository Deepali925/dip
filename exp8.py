import cv2
import numpy as np
# read a image using imread
img = cv2.imread('nature.jpg', 0)
cv2.imshow('image',img)
# creating a Histograms Equalization of a image using cv2.equalizeHist()
equ = cv2.equalizeHist(img)
# stacking images side-by-side
res = np.hstack((img, equ))
# show image input vs output
cv2.imshow('image', res)
cv2.waitKey(0)
cv2.destroyAllWindows()

