# görüntü inverting, positive/negative transforms
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('hand.jpg',0)
inverted = np.invert(image)
cv2.imshow("original",image)
cv2.imshow("inverted",inverted)
cv2.waitKey()
negimage = 255 - image
cv2.imshow("negimage",negimage)
cv2.waitKey()

# [h,w] = image.shape
# new_image = np.zeros([h,w], dtype=np.uint8)
# for i in range(h):
# for j in range(w):
# new_image[i,j] = 255 - image[i,j]
#
# # print(image[0,0])
# cv2.imshow("Manuel_inverted",new_image)
# cv2.waitKey()
