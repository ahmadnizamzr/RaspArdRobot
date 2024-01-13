import cv2
import time


vid = cv2.VideoCapture('/dev/video0')

while(True):
    ret, frame = vid.read()

    cv2.imshow('frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv2.destroyAllWindows()
