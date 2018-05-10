import numpy as np
import cv2

img  = cv2.imread('image.jpg')
cols = img.shape[1]
rows = img.shape[0]

M = np.float32([[1,0,150], [0,1,70]])
#shift 150px to the right(along with x axis) and 70px to the down(along with y axis)
#M = np.float32([[1,0,-150], [0,1,-70]])
#shift 150px to the left and 70px to the up
shifted = cv2.warpAffine(img, M , (cols, rows))
cv2.imshow('shifted', shifted)

cv2.waitKey(0)
cv2.destroyAllWindows()