#histogram eşitleme
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
# görüntüyü yeniden boyutlandırma yapacaksak
# image2 = cv2.resize(image, (500, 600))
img = cv2.imread('hand.jpg',0)
equ = cv2.equalizeHist(img)
# iki görüntüyü tek pencerede gösterme
res = np.hstack((img, equ))
# show image input vs output
cv2.imshow("image", res)
cv2.waitKey(0)
cv2.destroyAllWindows()