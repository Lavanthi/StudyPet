from ultralytics import YOLO
from picamera2 import Picamera2
import cv2
import time
import numpy as np

# Load YOLO model
model = YOLO("yolov8n.pt")

# Start camera
picam2 = Picamera2()

picam2.configure(
    picam2.create_preview_configuration(
        main={"size": (640, 480)}
    )
)

picam2.start()

# Timer variables
phone_start = None
warning_mode = False
flash_state = False
last_flash = time.time()

while True:

    # WARNING SCREEN MODE
    if warning_mode:

        # Flash every 0.5 seconds
        if time.time() - last_flash > 0.5:
            flash_state = not flash_state
            last_flash = time.time()

        # Create flashing background
        if flash_state:
            screen = np.zeros((480, 640, 3), dtype=np.uint8)
            screen[:] = (180, 105, 255)   # pink
        else:
            screen = np.zeros((480, 640, 3), dtype=np.uint8)
            screen[:] = (255, 255, 255)   # white

        # Main warning text
        cv2.putText(
            screen,
            "LOCK IN",
            (140, 180),
            cv2.FONT_HERSHEY_SIMPLEX,
            2.5,
            (255, 255, 255),
            6
        )

        # Cute subtitle
        cv2.putText(
            screen,
            "put the phone away girl",
            (150, 250),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.8,
            (255, 255, 255),
            2
        )

        # Fake cute button
        cv2.rectangle(
            screen,
            (180, 320),
            (460, 390),
            (255, 255, 255),
            -1
        )

        cv2.putText(
            screen,
            "press SPACE to continue",
            (205, 365),
            cv2.FONT_HERSHEY_SIMPLEX,
            0.7,
            (180, 105, 255),
            2
        )

        # Show warning screen
        cv2.imshow("StudyPet", screen)

        key = cv2.waitKey(1)

        # SPACE key returns to camera
        if key == 32:
            warning_mode = False
            phone_start = None

        # Q quits app
        if key == ord('q'):
            break

        continue

    # NORMAL CAMERA MODE
    frame = picam2.capture_array()

    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)

    results = model(frame)

    annotated_frame = results[0].plot()

    phone_detected = False

    # Detect objects
    for box in results[0].boxes:

        cls = int(box.cls[0])
        label = model.names[cls]

        if label == "cell phone":
            phone_detected = True

    # Timer logic
    if phone_detected:

        if phone_start is None:
            phone_start = time.time()

        elapsed = time.time() - phone_start

        # Trigger warning screen
        if elapsed > 5:
            warning_mode = True

    else:
        phone_start = None

    # Show camera
    cv2.imshow("StudyPet", annotated_frame)

    key = cv2.waitKey(1)

    if key == ord('q'):
        break

cv2.destroyAllWindows()
