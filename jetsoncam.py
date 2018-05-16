
import numpy as np
import cv2

cap = cv2.VideoCapture("nvcamerasrc ! video/x-raw(memory:NVMM), width=(int)300, height=(int)300,format=(string)I420, framerate=(fraction)30/1 ! nvvidconv flip-method=0 ! video/x-raw, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink")

while(True):
  # Capture frame-by-frame
  ret, frame = cap.read()

  # Our operations on the frame come here
  grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
  grey_3_channel = cv2.cvtColor(grey, cv2.COLOR_GRAY2BGR)

  numpy_horizontal = np.hstack((frame, grey_3_channel))
  numpy_horizontal_concat = np.concatenate((frame, grey_3_channel), axis=1)	

  # Display the resulting frame
  cv2.imshow('Numpy Horizontal Concat', numpy_horizontal_concat)

  if cv2.waitKey(1) & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()


