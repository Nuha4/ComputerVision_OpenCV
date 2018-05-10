import numpy as np
import cv2

img  = cv2.imread('flower.jpg')

dimpixel = 7
color = 100
space = 100
filter = cv2.bilateralFilter(img, dimpixel, color, space)
cv2.imshow('filter', filter)

cv2.waitKey(0)
cv2.destroyAllWindows()