<<<<<<< HEAD
#change color vdo
import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
        cv2.imshow("output",gray)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break
    

cap.release()
=======
#change color vdo
import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read()
    if check == True :
        gray = cv2.cvtColor(frame,cv2.COLOR_BAYER_BG2GRAY)
        cv2.imshow("output",gray)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break
    

cap.release()
>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
cv2.destroyAllWindows()