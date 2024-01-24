import cv2
import numpy as np
# foto2 = cv2.imread("./goruntu/kanal.png")#klasörden görüntü okuma
# cv2.imshow("Kırmızı",foto2)
foto = cv2.imread("baboon.bmp")
# cv2.imshow("el",foto)
B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]
# # cv2.imshow("el1",B)
# # cv2.imshow("el2",G)
cv2.imshow("baboon",R)
cv2.waitKey()
print(foto.shape) # yükseklik, genişlik ve kanal sayısı
print(R.shape)
x=4 #sütun no
y = 3 #satır no
kanal = 0
yogunluk_b= foto[y, x, kanal]
print("yoğunluk:",yogunluk_b)
yogunluk_r = R[y,x]
print("yoğunluk_gray:",yogunluk_r)
print("merhaba")
maksimum_yogunluk =np.max(B)
minimum_yogunluk =np.min(B)
print("Maksimum yoğunluk: ",maksimum_yogunluk)
print("Minimum yoğunluk: ",minimum_yogunluk)
print(foto[y,x])#tam koordinatın R G B değerleri döner
# görüntünün belirli piksllerini elde etme ve ekranda gösterme
parca2 = R[0:500, 0:400]
print(parca2)
cv2.imshow("parca",parca2)
cv2.waitKey()