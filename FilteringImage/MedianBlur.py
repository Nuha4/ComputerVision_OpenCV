import numpy as np
import cv2

img  = cv2.imread('kingFisher.jpg')
kernal = 3
#Noise Remove
median = cv2.medianBlur(img, kernal)
cv2.imshow('median', median)

cv2.waitKey(0)
cv2.destroyAllWindows()