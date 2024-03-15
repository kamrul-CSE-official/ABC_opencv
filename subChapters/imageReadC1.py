import cv2

def imageRead(image):
    img = cv2.imread(image)
    cv2.imshow("Output", img)
    cv2.waitKey(0)
