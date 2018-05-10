import numpy as np
import cv2

img  = cv2.imread('image.jpg')
cols = img.shape[1]
rows = img.shape[0]
center = (cols/2, rows/2)
angle = 90

M = cv2.getRotationMatrix2D(center, angle, 1)
rotate = cv2.warpAffine(img, M , (cols, rows))
cv2.imshow('rotate', rotate)

cv2.waitKey(0)
cv2.destroyAllWindows()