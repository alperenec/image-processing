import cv2
from skimage.util import random_noise
import numpy as np
while True:

    img = cv2.imread('morphologic_imp_shapes2.jpg',0)
    # cv2.imshow("Giris",img)
    ret,esik_image=cv2.threshold(img,60,255,cv2.THRESH_BINARY)
    # ret,esik_image=cv2.threshold(img,50,255,cv2.THRESH_BINARY)
    noise_img = random_noise(esik_image, mode="s&p",amount=0.1)#küçük değerler elde edilir
    noise_img = np.array(255*noise_img, dtype = 'uint8')#pikseller 255'e genişletilir
    cv2.imshow("Gurultulu giris goruntusu", noise_img)
    kernel = np.ones((3,3),dtype=np.uint8)
    kernel2 = np.ones((3,3),dtype=np.uint8)
    opening = cv2.morphologyEx(noise_img,cv2.MORPH_OPEN,kernel)
    closing = cv2.morphologyEx(noise_img,cv2.MORPH_CLOSE,kernel2)
    a = cv2.erode(closing,kernel,iterations=1)
    cv2.imshow("Acma sonucu",opening)
    cv2.imshow("Kapama sonucu",closing)
    cv2.imshow("erozyon sonucu",a)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break