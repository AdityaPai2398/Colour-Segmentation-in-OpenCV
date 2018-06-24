##import numpy as np
##import cv2
##
##video=cv2.VideoCapture('take1.mp4')
##while(video.isOpened()):
##	print("Video is Opened")
##	ret, frame =video.read()
##	frame=cv2.cvtColor(frame,0)
##	image=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
##	lower=np.array([0,190,225])
##	upper=np.array([0,190,225])
##	image_mask=cv2.inRange(image,lower,upper)
##	image=cv2.bitwise_and(frame,frame,mask=image_mask)
##	cv2.imshow('Single Frame Display',frame)
##	if(cv2.waitKey(10) & 0xFF == ord('q')):
##		break
##video.release()
##	
import cv2
import numpy as np

cap = cv2.VideoCapture('take1.mpg')

while(1):

    # Take each frame
    _, frame = cap.read()

    # Convert BGR to HSV
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # define range of red color in HSV
    lower_red = np.array([168,50,50]) #example value
    upper_red = np.array([180,255,255])

    # Threshold the HSV image to get only red colors
    mask = cv2.inRange(hsv, lower_red, upper_red)

    # Bitwise-AND mask and original image
    res = cv2.bitwise_and(frame,frame, mask= mask)

    cv2.imshow('frame',frame)
    #cv2.imshow('mask',mask)
    cv2.imshow('res',res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cv2.destroyAllWindows()
