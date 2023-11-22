<<<<<<< HEAD
import cv2 

img = cv2.imread("image/cat.jpg",0)

imgresize = cv2.resize(img,(400,400))

cv2.imwrite("outPut.jpg",imgresize)
cv2.waitKey(0)
=======
import cv2 

img = cv2.imread("image/cat.jpg",0)

imgresize = cv2.resize(img,(400,400))

cv2.imwrite("outPut.jpg",imgresize)
cv2.waitKey(0)
>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
cv2.destroyAllWindows