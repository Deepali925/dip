# Import cv2 module 
import cv2 

# Reads the image 
img = cv2.imread('dog.jpg') 

# Convert to YCrCb color space 
imgYC = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb) 
# Shows the image 
cv2.imshow('YCrCbimage', imgYC) 
cv2.waitKey(0)		 
cv2.destroyAllWindows()

# convert to HSV color space 
imgHSV= cv2.cvtColor(img, cv2.COLOR_BGR2HSV) 
# Shows the image 
cv2.imshow('HSV image', imgHSV) 
cv2.waitKey(0)		 
cv2.destroyAllWindows()

# Converts to LAB color space 
imgLAB = cv2.cvtColor(img, cv2.COLOR_BGR2LAB) 
  
# Shows the image 
cv2.imshow('Image LAB', imgLAB)  
  
cv2.waitKey(0)          
cv2.destroyAllWindows()

