import cv2 
# loading the image 
img = cv2.imread("cam.jpg") 
# fetching the dimensions 
h=img.shape[0]
w=img.shape[1]
pixels=h*w
print('Height =',h)
print('Width =',h)
print('Total Number of pixels=',pixels,'Pixels')
#Arithmetic operations : addition, subtraction 
import cv2 
import numpy as np 
image1 = cv2.imread('input1.jpg') 
image2 = cv2.imread('input2.jpg') 
# Show input images
cv2.imshow('Image1',image1)
cv2.imshow('Image2',image2)
# ADD images 
ImgSum = cv2.add(image1, image2) 
cv2.imshow('Image',ImgSum) 
# subtract images 
subtracted = cv2.subtract(image1, image2) 
# TO show the output 
cv2.imshow('image', subtracted) 

