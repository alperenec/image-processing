import cv2
from skimage.util import random_noise
import numpy as np
while True:
    img = cv2.imread('morphologic_imp_shapes2.jpg', 0)
    cv2.imshow("Giris",img)
    ret,esik_image=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    kernel = np.ones((2,2),dtype=np.uint8)
    erode_result = cv2.erode(esik_image,kernel,iterations=2)
    dilate_result = cv2.dilate(esik_image,kernel,iterations=1)
    cv2.imshow("Esiklenen giris goruntusu", esik_image)
    cv2.imshow("Erozyon",erode_result)
    cv2.imshow("Genisleme",dilate_result)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break