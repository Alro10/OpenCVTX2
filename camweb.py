
import numpy as np
import cv2

# webcam /dev/video1
cap = cv2.VideoCapture("/dev/video1")

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


