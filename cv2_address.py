

import cv2
cap = cv2.VideoCapture(f'http://192.168.29.33:8080/')

if not cap.isOpened():
    print("Failed to open camera")
    exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    cv2.imshow("Camera", frame)

    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()