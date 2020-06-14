import cv2
cap=cv2.VideoCapture(0)
faced=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
while True:
    ret,frame=cap.read()
    facec=faced.detectMultiScale(frame)
    for (x,y,a,b) in facec:
        cv2.rectangle(frame,(x,y),(x+a,y+b),(255,0,0),2)
    cv2.imshow('w',frame)
    if cv2.waitKey(1)==ord('q'):
        break
cap.release()
cv2.destroyAllWindows()