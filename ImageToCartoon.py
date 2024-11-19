import cv2
import numpy as np
webcam=cv2.VideoCapture(0)
webcam.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
webcam.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)



imageFrame=cv2.imread("1731083177863.jpg")
imageFrame = cv2.resize(imageFrame, (0, 0), fx = 0.1, fy = 0.1)
#imageFrame=webcam.read();
gray=cv2.cvtColor(imageFrame,cv2.COLOR_BGR2GRAY)
gray=cv2.medianBlur(gray,5)
edges=cv2.adaptiveThreshold(gray,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,9,9)
color=cv2.bilateralFilter(imageFrame,9,250,250)
cartoon=cv2.bitwise_and(color,color,mask=edges)
cv2.imshow("Image",imageFrame)
cv2.imshow("edges",edges)
cv2.imshow("Cartoon",cartoon)
cv2.waitkey(0)
