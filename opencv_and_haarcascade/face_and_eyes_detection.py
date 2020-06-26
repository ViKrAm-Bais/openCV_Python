import cv2
import numpy as np
face_cascade=cv2.CascadeClassifier("harcascade/haarcascade_frontalface_default.xml")
eye_cascade=cv2.CascadeClassifier("harcascade/haarcascade_eye.xml")
cap=cv2.VideoCapture(0)
while True:
    ret,frame=cap.read()
    if ret:
        frame = cv2.flip(frame, 1)
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray,1.3,5)
        for (x, y, a, b) in faces:
            cv2.rectangle(frame, (x, y), (x + a, y + b), (255, 0, 0), 2)
            (cx,cy),radius=cv2.minEnclosingCircle(np.array([[int(x),int(y)],[int(x+a),int(y+b)]],dtype=np.int32))
            eyes=eye_cascade.detectMultiScale(gray)
            cv2.circle(frame,(int(cx),int(cy)),int(radius),(0,0,255),2)
            for (h,k,l,m) in eyes:
                cv2.rectangle(frame,(h,k),(h+l,k+m),(0,255,0),2)
        cv2.imshow("window", frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

