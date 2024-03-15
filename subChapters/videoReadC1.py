import cv2


def videread(video):
    cap = cv2.VideoCapture(video)

    while True:
        success, img = cap.read()
        cv2.imshow("video", img)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
