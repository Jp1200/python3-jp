import numpy as np
import cv2

res = "1080p"
boundaries = [
    ([17, 15, 100], [50, 56, 200]),
    ([86, 31, 4], [220, 88, 50]),
    ([25, 146, 190], [62, 174, 250]),
    ([103, 86, 65], [145, 133, 128]),
]


def get_dim(cap, res="1080p"):
    width, height = STD_RES["detect"]
    if res in STD_RES:
        width, height = STD_RES[res]
    change_res(cap, width, height)
    return width, height


STD_RES = {"480p": (640, 480), "720p": (1280, 720),
           "1080p": (1920, 1080), "detect": (416, 416)}
# Define Net
net = cv2.dnn.readNet('./config/yolov3.weights', './config/yolov3.cfg')
classes = []
with open('./config/coco.names', 'r') as f:
    classes = f.read().splitlines()
print(classes)
# DEFINE VIDEO CAPTURE METHOD
cap = cv2.VideoCapture(0)
#cap = cv2.VideoCapture("22.mp4")
if (cap.isOpened() == False):
    print("Error opening video stream or file")


while True:
    ret, frame = cap.read()

    height, width, _ = frame.shape
    blob = cv2.dnn.blobFromImage(
        frame, 1/255, (416, 416), (0, 0, 0), swapRB=True, crop=False)

    net.setInput(blob)
    output_layers_names = net.getUnconnectedOutLayersNames()
    layerOutputs = net.forward(output_layers_names)

    boxes = []
    confidences = []
    class_ids = []
    for output in layerOutputs:
        for detection in output:
            scores = detection[5:]
            class_id = np.argmax(scores)
            confidence = scores[class_id]
            if confidence > 0.5:
                center_x = int(detection[0]*width)
                center_y = int(detection[1]*height)
                w = int(detection[2]*width)
                h = int(detection[3]*height)

                x = int(center_x - w/2)
                y = int(center_y - h/2)

                boxes.append([x, y, w, h])
                confidences.append((float(confidence)))
                class_ids.append(class_id)

    indexes = cv2.dnn.NMSBoxes(boxes, confidences, 0.5, 0.4)

    font = cv2.FONT_HERSHEY_SIMPLEX
    colors = np.random.uniform(0, 255, size=(len(boxes), 3))
    if len(indexes) > 0:
        for i in indexes.flatten():
            x, y, w, h = boxes[i]
            label = str(classes[class_ids[i]])
            confidence = str(round(confidences[i], 2))
            color = colors[i]
            cv2.rectangle(frame, (x, y), (x+w, y+h), color, 2)
            cv2.putText(frame, label + "I" + confidence,
                        (x, y+20), font, 2, (255, 255, 255), 2)

    cv2.imshow("webcam", frame)
    if cv2.waitKey(20) & 0xFF == ord("q"):
        print("Program Closed! Saving...")
        break
cap.release()
cv2.destroyAllWindows()
