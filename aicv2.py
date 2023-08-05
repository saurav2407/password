# Import the necessary packages
import cv2 
import face_recognizer
import matplotlib.pyplot as plt


# Load the known image
known_image = face_recognizer("d:\jarvis\jarvis all\dist\WhatsApp Image 2023-05-16 at 21.27.40.jpg")
known_faces = face_recognizer(face_image = known_image,
											num_jitters=50,
											model='large')[0]
# Lanch the live camera
cam = cv2.VideoCapture(0)
#Check cameram
if not cam.isOpened():
	print("Camera not working")
	exit()
	
# when camera is opened
while True:
	
	# campture the image frame-by-frame
	ret, frame = cam.read()
	
	# check frame is reading or not
	if not ret:
		print("Can't receive the frame")
		break

	# Face detection in the frame
	face_locations = face_recognizer.face_locations(frame)

	for face_location in face_locations:
		top, right, bottom, left = face_location
		# Draw a rectangle with blue line borders of thickness of 2 px
		frame = cv2.rectangle(frame, (right,top), (left,bottom), color = (0,0, 255), thickness=2)
	# Check the each faces location in each frame
	try:
		# Frame encoding
		Live_face_encoding = face_recognizer.face_encodings(face_image = frame,
															num_jitters=23,
															model='large')[0]

		# Match with the known faces
		results = face_recognizer.compare_faces([known_faces], Live_face_encoding)

		if results:
			img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
			img = cv2.putText(img, 'PawanKrgunjan', (30, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
					(255,0,0), 2, cv2.LINE_AA)
			print('Pawan Kumar Gunjan Enter....')
			plt.imshow(img)
			plt.show()
			break
	except:
		img = cv2.putText(frame, 'Not PawanKrgunjan', (30, 55), cv2.FONT_HERSHEY_SIMPLEX, 1,
				(255,0,0), 2, cv2.LINE_AA)
		# Display the resulting frame
		cv2.imshow('frame', img)
		# End the streaming
		if cv2.waitKey(1) == ord('q'):
			break
	

# Release the capture
cam.release()
cv2.destroyAllWindows()
