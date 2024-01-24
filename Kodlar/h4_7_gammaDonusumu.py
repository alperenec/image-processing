#Gamma dönüşümü
import cv2
import matplotlib.pyplot as plt
import numpy as np
import math
img = cv2.imread('hand.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hue, sat, val = cv2.split(hsv)
# cv2.imshow("val bandi", hsv)
mid = 0.5
mean = np.mean(val)
gamma = math.log(mid*255)/math.log(mean)
print(gamma)
# gamma düzeltmesi value bandında
val_gamma = np.power(val, gamma).clip(0,255).astype(np.uint8)
# iyileştirilen value bandı ile görüntünün diğer bantlarını birleştirme
hsv_gamma = cv2.merge([hue, sat, val_gamma])
img_gamma2 = cv2.cvtColor(hsv_gamma, cv2.COLOR_HSV2BGR)
cv2.imshow('orijinal', img)
cv2.imshow('SONUC', img_gamma2)
cv2.waitKey(0)