import cv2
from app.vision.hand_tracker import HandTracker

cap = cv2.VideoCapture(0)
tracker = HandTracker()

while True:
    success, frame = cap.read()
    if not success:
        break

    frame = tracker.detect(frame)

    cv2.imshow("Hand Tracking", frame)

    if cv2.waitKey(1) & 0xFF == 27:  # ESC to exit
        break

cap.release()
cv2.destroyAllWindows()