import cv2
import numpy as np
from matplotlib import pyplot as plt
foto1 = cv2.imread("baboon.bmp",0)
import matplotlib.image as mpimg
# Michalson’in denklemi ile Contrast iyileştirme
CM = (np.max(foto1) - np.min(foto1))/(np.max(foto1) + np.min(foto1))
yeni = CM*foto1
plt.imshow(yeni, cmap='gray')
plt.show()
cv2.imshow("hand_original",foto1)
cv2.waitKey()
# İyileştirilen görüntü ile orijinalin histogram karşılaştırması
hist_gray = cv2.calcHist([foto1], [0],None,[256],[0,256])#gri görüntü histogram hesaplama
hist_gray_yeni = cv2.calcHist([yeni], [0],None,[256],[0,256])#gri görüntü histogram hesaplama
plt.figure(1)
plt.plot(hist_gray)
plt.figure(2)
plt.plot(hist_gray_yeni)
plt.show()
#np kütüphanesi ile histogram oluşturma (sonuçlar opencv ile aynı!!!)
# a=np.histogram(foto1,256,[0,256])#numpy fonksiyonu ile histogramı hesaplama (Hangi pikselden kaç tane var görünür (Debug da)
# print(a[0])#histogram değerleri
# print(np.sum(a[0]))#histogram değerlerinin toplamı (kümülatif ile örtüşmeli)
# plt.figure(1)
# plt.plot(a[0])
# plt.show()
# # Cumulative histogram
# plt.figure(3)
# plt.hist(foto1.ravel(), bins = 256, cumulative = True)
# plt.xlabel('Intensity Value')
# plt.ylabel('Count')
# plt.show()