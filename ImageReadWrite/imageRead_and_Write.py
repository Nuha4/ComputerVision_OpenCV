import cv2

img  = cv2.imread('image.jpg')
cv2.imshow('Original', img)
cv2.waitKey()
cv2.destroyAllWindows()

#Read Image in Grayscale
img  = cv2.imread('image.jpg', 0)
cv2.imshow('Original', img)
cv2.waitKey()
cv2.destroyAllWindows()


#Save image in different format
img  = cv2.imread('image.jpg')
img  = cv2.imwrite('image.png', img)
cv2.imshow('Original', img)
cv2.waitKey()
cv2.destroyAllWindows()