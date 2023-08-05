import cv2

# Create a VideoCapture object to open the camera

cap = cv2.VideoCapture(0)

# Check if the camera is opened successfully
if not cap.isOpened():
    print("Failed to open camera")
    exit(),

# Read and display frames from the camera until 'q' is pressed
while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # If frame reading was unsuccessful, break the loop
    if not ret:
        break

    # Display the frame in a window named "Camera"
    cv2.imshow("Camera", frame)

    # Wait for 'q' key to be pressed to exit
    if cv2.waitKey(1) == ord('q'):
        break

# Release the VideoCapture object and close any open windows
cap.release()
cv2.destroyAllWindows()