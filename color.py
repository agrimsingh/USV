import cv2
import numpy as np

#capturing video through webcam
cap=cv2.VideoCapture(0)

while(1):
	_, img = cap.read()

        #converting frame to BGR to HSV

	hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

       #defining the range of red color
	red_lower=np.array([136,87,111],np.uint8)
	red_upper=np.array([180,255,255],np.uint8)

       #defining the range of Blue color
        blue_lower=np.array([99,115,150],np.uint8)
        blue_upper=np.array([130,255,255],np.uint8)
        #defining the Range of yellow color
        yellow_lower=np.array([20,100,100],np.uint8)
        yellow_upper=np.array([30,255,255],np.uint8)

       #finding the range of red, blue, yellow color int the image
	red=cv2.inRange(hsv, red_lower, red_upper)
	blue=cv2.inRange(hsv,blue_lower,blue_upper)
        yellow=cv2.inRange(hsv,yellow_lower,yellow_upper)
	
	kernal = np.ones((5 ,5), "uint8")
	red=cv2.dilate(red, kernal)
	res=cv2.bitwise_and(img, img, mask = red)
	
	blue=cv2.dilate(blue,kernal)
	res1=cv2.bitwise_and(img, img, mask = blue)

	yellow=cv2.dilate(yellow,kernal)
        res2=cv2.bitwise_and(img, img, mask = yellow) 

	#tracking Red
	(_,contours,hierarchy)=cv2.findContours(red,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
	
	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
                if(area>300):
			x,y,w,h = cv2.boundingRect(contour) 
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),2)
			cv2.putText(img,"Red color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,255))
			print "Red in frame"

        #tracking Blue
	(_,contours,hierarchy)=cv2.findContours(blue,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
			cv2.putText(img,"Blue color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (255,0,0))
			print "Blue in frame"

	#tracking Yellow
        (_,contours,hierarchy)=cv2.findContours(yellow,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)

	for pic, contour in enumerate(contours):
		area = cv2.contourArea(contour)
		if(area>300):
			x,y,w,h = cv2.boundingRect(contour)
			img = cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,255),2)
			cv2.putText(img,"Yellow color",(x,y),cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0,255,255))
			print "Yellow in frame"


        #cv2.imshow("Redcolour",red)
	cv2.imshow("let's",img)
        #cv2.imshow("red",res)  
	if cv2.waitKey(10) & 0xFF == ord('q'):
		cap.release()
		cv2.destroyAllWindows()
		break  
