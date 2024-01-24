# eşikleme
import cv2
import numpy as np
from matplotlib import pyplot as plt
image1 = cv2.imread('hand.jpg')
img = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
ret, thresh1 = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY)
ret, thresh2 = cv2.threshold(img, 140, 255, cv2.THRESH_BINARY_INV)
ret, thresh3 = cv2.threshold(img, 140, 255, cv2.THRESH_TRUNC)
ret, thresh4 = cv2.threshold(img, 140, 255, cv2.THRESH_TOZERO)
ret, thresh5 = cv2.threshold(img, 140, 255, cv2.THRESH_TOZERO_INV)

cv2.imshow('Binary Threshold', thresh1)
cv2.imshow('Binary Threshold Inverted', thresh2)
cv2.imshow('Truncated Threshold', thresh3)
cv2.imshow('Set to 0', thresh4)
cv2.imshow('Set to 0 Inverted', thresh5)
cv2.waitKey()
# #Belirli aralıklar arası manuel eşikleme
# myResult = cv2.inRange(img, 100, 130)
# cv2.imshow("esikleme",myResult) # cv2.waitKey()