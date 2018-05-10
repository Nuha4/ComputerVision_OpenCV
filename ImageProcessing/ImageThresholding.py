import numpy as np
import cv2

img  = cv2.imread('image.jpg', 0)
thresholdValue = 200

(T_value, binary_threshold) = cv2.threshold(img, thresholdValue, 255, cv2.THRESH_BINARY)
#pixels<200 then make all pixels into Black = 0, pixels>200 then white = 1

#(T_value, binaryThreshold) = cv2.threshold(img, thresholdValue, 255, cv2.THRESH_BINARY_INV)
#pixels<200 then White = 0, pixels>200 then Black = 1

cv2.imshow('binary', binary_threshold)
cv2.waitKey(0)
cv2.destroyAllWindows()
