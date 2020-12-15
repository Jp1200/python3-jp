import numpy as np
import cv2

cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()
    cv2.imshow("webcam", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        print("Program Closed! Saving...")
        break
cap.release()
cv2.destroyAllWindows()
