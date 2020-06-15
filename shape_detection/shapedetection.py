import cv2
img=cv2.imread("shapes2.png")

gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

ret,wbimg=cv2.threshold(gray,250,255,cv2.THRESH_BINARY_INV)
#cv2.imshow("wbimage",wbimg)
_,contours,_=cv2.findContours(wbimg,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)

for contour in contours:
    contourx=cv2.approxPolyDP(contour,0.01*cv2.arcLength(contour,True),True)
    if cv2.contourArea(contourx)>500:
        cv2.drawContours(img, [contourx], 0, (255, 0, 0), 2)
        length=len(contourx)
        shape=""
        cv2.putText(img,str("length="+ str(length)),(contourx[0][0][0],contourx[0][0][1]+30),cv2.FONT_HERSHEY_SIMPLEX,0.5,(200,100,100),2)
        if length==3:
            shape="triangle"
        elif length==4:
            shape="rectangle"
        elif length==5:
            shape="pentagone"
        elif length==6:
            shape="hexagone"
        elif length==7:
            shape="heptagone"
        elif length==8:
            shape="octagone"
        elif length==9:
            shape="nonagone"
        elif length==10:
            shape="decagone"
        elif length>10:
            shape="elipse"
        cv2.putText(img, shape, (contourx[0][0][0], contourx[0][0][1] + 50), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                    (0, 200, 255), 2)
cv2.imshow("win",img)
cv2.waitKey()
cv2.destroyAllWindows()
