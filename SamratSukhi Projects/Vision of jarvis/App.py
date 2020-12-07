import  cv2,time
import numpy as np
import pandas as pa
#cv2.namedWindow('Vision Of Jarvis')
xxx=160  #x/4 x=device_width
yyy=120  #y/4 y=device_height

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
img = np.zeros((480,640,3), np.uint8)


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
    
    #lower_range=np.array([l_h,l_s,l_v])
    lower_range=np.array([163,143,57])
    upper_range=np.array([179,255,255])
    #upper_range=np.array([u_h,u_s,u_v])

    mask=cv2.inRange(hsv,lower_range,upper_range)
    #print(mask.size)
    
    contours, hierarchy= cv2.findContours(mask,cv2.RETR_TREE,cv2.CHAIN_APPROX_NONE)
    
    cv2.drawContours(frame,contours,-1,(0,255,0),3)
   
    result=cv2.bitwise_and(frame,frame,mask=mask)
    M = cv2.moments(mask)
    if M["m00"]!=0:
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])
    else:
        M["m00"]=np.nextafter(0, 1)
        cX = int(M["m10"] / M["m00"])
        cY = int(M["m01"] / M["m00"])

    print(cX,cY,M["m00"])
    #cv2.circle(result,(cX,cY), 10, (0,0,255), -1)
    cv2.circle(result,(cX,cY), 7, (255,0,0), -1)
    img=cv2.circle(img,(cX+10,cY+10),15,(0,255,0),-1)
    cv2.imshow('VoJ',img)

    #cv2.rectangle(result,(510,0),(510,480),(0,0,255),3)
    #cv2.imshow("mask",mask)
   
    #cv2.imshow("hii",frame)
   
    cv2.imshow("result",result)
    
    key=cv2.waitKey(1)
    if key==ord(' '):
        break
    key=cv2.waitKey(1)
    if key==ord('r'):
        img.delete()

video.release()
cv2.destroyAllWindows()