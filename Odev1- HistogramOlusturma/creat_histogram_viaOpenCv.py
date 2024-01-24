import cv2
import numpy as np
from matplotlib import pyplot as plt

renkli = cv2.imread("seaView.jpg")
cv2.imshow("manzaraya",renkli)
cv2.waitKey(0)


gri = cv2.imread("seaView.jpg",0)
cv2.imshow("seaView_original",gri)
cv2.waitKey()

# hist_color = cv2.calcHist([renkli], [2],None,[256],[0,256])#renkli görüntü histogram hesaplama(2.parametre kanallar)
hist_gray = cv2.calcHist([gri], [0],None,[256],[0,256])#gri görüntü histogram hesaplama
# plt.figure(1)
# plt.plot(hist_color)
# plt.show()
plt.figure(2)
plt.plot(hist_gray)
plt.show()

# B = renkli[:,:,0]
# hist_B = cv2.calcHist([B], [0],None,[256],[0,256])#gri görüntü histogram hesaplama
# print(np.sum(hist_B))
# plt.plot(hist_B)
# plt.show()
# #alternatif gösterim
# plt.figure(3)
# plt.hist(hist_gray.ravel(),256,[0,256])
# plt.show()