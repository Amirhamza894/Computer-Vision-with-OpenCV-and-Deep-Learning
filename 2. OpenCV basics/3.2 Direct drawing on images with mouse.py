import cv2
import numpy as np



################
### Function ###
################

def draw_circle(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:
        cv2.circle(img, (x,y), radius=100, color=(0,200,0), thickness=-1)
cv2.namedWindow(winname='my Drawing')

cv2.setMouseCallback('my Drawing', draw_circle)

#####################################
##### SHOWING IMAGE WITH OPENCV #####
#####################################

img = np.zeros(shape=(512,512,3), np.int8)

while True:
    cv2.imshow('my Drawing', img)
    
    if cv2.waitKey(20) & 0xFF = 27:
        break
        
cv2.distroyAllWindows()