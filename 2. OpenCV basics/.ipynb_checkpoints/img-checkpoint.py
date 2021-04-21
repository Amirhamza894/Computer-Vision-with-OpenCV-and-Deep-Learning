import cv2

img = cv2.imread('C:\\Users\\Sorcim\\Computer Vision with OpenCV and Deep Learning\\DATA\\lion.jpg')


while True:
    cv2.imshow('img',  img)
    
    #if we've waited at least 1 ms AND we've pressed the Esc
    if cv2.waitKey(1) & 0xFF == 27:
        break
        
cv2.distroyAllWindows()