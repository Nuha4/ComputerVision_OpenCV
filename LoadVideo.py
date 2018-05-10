import cv2

cap = cv2.VideoCapture('sample.mp4')

while(cap.isOpened()):
    ret, frame = cap.read()
    cv2.imshow('vid', frame)
    if cv2.waitKey(1) & 0xFF == ('q'):
        break

cap.release()
cv2.destroyAllWindows()