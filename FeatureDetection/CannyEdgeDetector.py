import numpy as np
import cv2

img  = cv2.imread('flower.jpg')
thresholdValue1 = 50
thresholdValue2 = 100

canny = cv2.Canny(img, thresholdValue1, thresholdValue2)
cv2.imshow('canny', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()