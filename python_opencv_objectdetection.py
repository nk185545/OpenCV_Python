import cv2
import numpy as np

def nothing(x):
    pass


cv2.namedWindow('Tracking')

cv2.createTrackbar('LH','Tracking',0, 255 ,nothing)
cv2.createTrackbar('LS','Tracking',0, 255 ,nothing)
cv2.createTrackbar('LV','Tracking',0, 255 ,nothing)
cv2.createTrackbar('UH','Tracking',255, 255 ,nothing)
cv2.createTrackbar('US','Tracking',255, 255 ,nothing)
cv2.createTrackbar('UV','Tracking',255, 255 ,nothing)



cap =cv2.VideoCapture(0)

while(1):
    #frame = cv2.imread('amarties.png')
    _ ,frame = cap.read()
    hsv = cv2.cvtColor(frame , cv2.COLOR_BGR2HSV)

    lh = cv2.getTrackbarPos('LH','Tracking')
    ls = cv2.getTrackbarPos('LS','Tracking')
    lv = cv2.getTrackbarPos('LV','Tracking')
    uh = cv2.getTrackbarPos('UH','Tracking')
    us = cv2.getTrackbarPos('US','Tracking')
    uv= cv2.getTrackbarPos('UV','Tracking')

    l_b = np.array([lh, ls, lv])
    u_b = np.array([uh,us,uv])

    mask = cv2.inRange(hsv ,l_b ,u_b)

    res = cv2.bitwise_and(frame , frame, mask=mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)

    k = cv2.waitKey(1) & 0xFF
    if k==27:
        break
cap.release()
cv2.destroyAllWindows()