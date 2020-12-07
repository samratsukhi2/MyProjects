import cv2
import numpy as np
from win32api import GetSystemMetrics
result = np.zeros((480,640,3), np.uint8)
cv2.namedWindow('VoJ')

cv2.line(result,(160,120),(160,480),(255,0,0),3)
cv2.line(result,(320,120),(320,480),(255,0,0),3)
cv2.line(result,(480,120),(480,480),(255,0,0),3)
cv2.line(result,(640,120),(640,480),(255,0,0),3)

cv2.line(result,(0,120),(640,120),(255,0,0),3)
cv2.line(result,(0,210),(640,210),(255,0,0),3)
cv2.line(result,(0,300),(640,300),(255,0,0),3)
cv2.line(result,(0,390),(640,390),(255,0,0),3)

while(1):
    cv2.imshow('VoJ',result)
    k = cv2.waitKey(1) & 0xFF
    if k == ord('m'):
        mode = not mode
    elif k == 27:
        break

cv2.destroyAllWindows()