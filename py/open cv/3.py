<<<<<<< HEAD
import cv2
img = cv2.imread("image/boy.jpg")
imgresize = cv2.resize(img,(400,400))

#show image
cv2.imshow("where is where where",imgresize)
cv2.waitKey(5000) #ms
=======
import cv2
img = cv2.imread("image/boy.jpg")
imgresize = cv2.resize(img,(400,400))

#show image
cv2.imshow("where is where where",imgresize)
cv2.waitKey(5000) #ms
>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
cv2.destroyAllWindows()