import numpy as np
import cv2

pic = np.zeros((500, 500, 3), dtype='uint8')
color =  (255, 255, 0)
cv2.circle(pic, (250,250) , 150, color)
cv2.imshow('dark', pic)

cv2.waitKey(0)
cv2.destroyAllWindows()