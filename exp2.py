import cv2 
import numpy as np 
image1 = cv2.imread('cam.jpg') 
image2 = cv2.imread('nature.jpg') 
# Show input images
cv2.imshow('Image1',image1)
cv2.imshow('Image2',image2)
# bitwise AND operation 
dest_and = cv2.bitwise_and(nature, cam, mask = None) 
cv2.imshow('Bitwise AND', dest_and) 
# bitwise OR operation 
dest_or = cv2.bitwise_or(nature, cam, mask = None) 
cv2.imshow('Bitwise OR', dest_or) 
# bitwise XOR operation 
dest_xor = cv2.bitwise_or(nature, cam, mask = None) 
cv2.imshow('Bitwise XOR', dest_xor) 
# bitwise NOT operation 
dest_not = cv2.bitwise_not(cam, mask = None) 
cv2.imshow('Bitwise NOT', dest_not) 









