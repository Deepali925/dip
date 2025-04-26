import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread('dog.jpg')
# Displaying the original image
plt.imshow(img)
cv2.waitKey(0)          
cv2.destroyAllWindows()

# Averaging the image
blrimg = cv2.blur(img, (3,3))
# Displaying the blurred image
plt.imshow(blrimg)
cv2.waitKey(0)          
cv2.destroyAllWindows()

# Guassian Blur
guassimg = cv2.GaussianBlur(img, (5,5), cv2.BORDER_DEFAULT)
# Displaying the blurred image
plt.imshow(guassimg)
cv2.waitKey(0)          
cv2.destroyAllWindows()

# Median blurr
medimg = cv2.medianBlur(img, 5)
# Displaying the blurred image
plt.imshow(medimg)
cv2.waitKey(0)          
cv2.destroyAllWindows()

