
import cv2
from ascii import Converter
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    con = Converter(path=frame)
    con.run()
    cv2.imshow("webcam", frame)

    if cv2.waitKey(20) & 0xFF == ord("q"):
        print("Program Closed! Saving...")
        break
cap.release()
cv2.destroyAllWindows()
