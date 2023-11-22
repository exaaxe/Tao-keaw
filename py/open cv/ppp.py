<<<<<<< HEAD
import cv2
import numpy as np
import urllib
url = r'http://www.mywebsite.com/abc.jpg'
req = urllib.request.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr,-1)
=======
import cv2
import numpy as np
import urllib
url = r'http://www.mywebsite.com/abc.jpg'
req = urllib.request.urlopen(url)
arr = np.asarray(bytearray(req.read()), dtype=np.uint8)
img = cv2.imdecode(arr,-1)
>>>>>>> 80ee62ea7d1f9be315d76ce9ef7232b7c5380a0d
cv2.imshow('abc',img)