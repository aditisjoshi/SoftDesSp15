""" Experiment with face detection and image filtering using OpenCV """

import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    face_cascade = cv2.CascadeClassifier('/usr/share/opencv/haarcascades/haarcascade_frontalface_alt.xml')

    kernel = np.ones((21,21),'uint8')   

    ret, frame = cap.read()
    faces = face_cascade.detectMultiScale(frame, scaleFactor=1.2, minSize=(20,20))

    for (x,y,w,h) in faces:
        frame[y:y+h,x:x+w,:] = cv2.dilate(frame[y:y+h,x:x+w,:], kernel)
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255))

        cv2.line(frame, (x+w-w/4-x/13,y+h/3), (x+w-w/4+x/13,y+h/3), (0,0,0), thickness=5)
        cv2.line(frame, (x+w/4+x/13,y+h/3), (x+w/4-x/13,y+h/3), (0,0,0), thickness=5)
        cv2.line(frame, (x+w/4-x/13,y+h/3+y/3), (x+w-w/4+x/13,y+h/3+y/3), (0,0,0), thickness=5)
    
    cv2.imshow('frame',frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()