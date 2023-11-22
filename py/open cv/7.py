<<<<<<< HEAD
#open vdo by open cv

import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง
    if check == True :
        cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break
    

cap.release()
=======
#open vdo by open cv

import cv2

cap = cv2.VideoCapture("image/Video.mp4")

while (cap.isOpened()):
    check , frame = cap.read() #รับภาพจากกล้อง
    if check == True :
        cv2.imshow("output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else :
        break
    

cap.release()
>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
cv2.destroyAllWindows()