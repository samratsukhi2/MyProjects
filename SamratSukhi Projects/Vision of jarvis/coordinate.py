import  cv2,time
import numpy as np
import pandas as pa

def nothing(x):
    pass

video=cv2.VideoCapture(0)

cv2.namedWindow("frame1")
cv2.createTrackbar("L - H","frame1",0,179,nothing)
cv2.createTrackbar("L - S","frame1",0,255,nothing)
cv2.createTrackbar("L - V","frame1",0,255,nothing)
cv2.createTrackbar("U - H","frame1",179,179,nothing)
cv2.createTrackbar("U - S","frame1",255,255,nothing)
cv2.createTrackbar("U - V","frame1",255,255,nothing)


while True:
    check, frame = video.read()
    frame=cv2.flip(frame,1)
    blurred_frame=cv2.GaussianBlur(frame,(5,5),0)
    hsv=cv2.cvtColor(blurred_frame,cv2.COLOR_BGR2HSV)

    l_h=cv2.getTrackbarPos("L - H","frame1")
    l_s=cv2.getTrackbarPos("L - S","frame1")
    l_v=cv2.getTrackbarPos("L - V","frame1")
    u_h=cv2.getTrackbarPos("U - H","frame1")
    u_s=cv2.getTrackbarPos("U - S","frame1")
    u_v=cv2.getTrackbarPos("U - V","frame1")
    
    lower_range=np.array([l_h,l_s,l_v])
    #lower_range=np.array([154,122,0])
    upper_range=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,lower_range,upper_range)
    #print(mask.size)
    
    contours, hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
   
    result=cv2.bitwise_and(frame,frame,mask=mask)
    M = cv2.moments(mask)
    cX = int(M["m10"] / M["m00"])
    cY = int(M["m01"] / M["m00"])
    print(cX,cY)
    cv2.circle(result,(cX,cY), 10, (0,0,255), -1)
# put text and highlight the center
#cv2.imshow("mask",mask)
   
    #cv2.imshow("hii",frame)
   
    cv2.imshow("result",result)
    
    key=cv2.waitKey(1)
    if key==ord('q'):
        break

video.release()
cv2.destroyAllWindows()