from ultralytics import YOLO
from picamera2 import Picamera2
import cv2
import time

#load  YOLO model
model = YOLO("yolov8n.pt")

#open webcam
picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"size": (640,480)}))
picam2.start()

phone_start = None

while True:
 	frame = picam2.capture_array()
	frame = cv2.cvtColor(frame,cv2.COLOR_RGB2BGR)
	results = model(frame)
	phone_detected = False
	annotated_frame = results[0].plot()
	for box in results[0].boxes:
		cls = int(box.cls[0])
		label = model.names[cls]
		if label == "cell phone":
			phone_detected + true
	if phone_detected:
		if phone_start is None:
			phone_start = time.time()
		elapsed = time.time() - phone_start
		if elapsed > 5:
			cv2.putText(annotated_frame,"LOCK IN", (50,100),cv2.FONT_HERSHEP_SIMPLEX,2,(0,0,255),5)
	else:
		phone_start = None
	cv2.imshow("StudyPet",annotated_frame)
	if cv2.waitKey(1) & 0xFF == ord('q'):
		break
cv2.destroyAllWindows()
