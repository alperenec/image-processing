#Gamma dönüşümü
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('baboon.bmp')
cv2.imshow("Orijinal", img)

# 4 gamma değerini uygulama.
for gamma in [0.1, 0.5, 1.16, 2.2]:
    # Gamma uygulama
    gamma_corrected = np.array(255 * (img / 255) ** gamma, dtype='uint8')

    # Düzeltilen görüntüleri kaydetme
    cv2.imwrite('gamma_transformed' + str(gamma) + '.jpg', gamma_corrected)

    # Ekrana gösterme
    cv2.imshow("Gamma Dönüşüm", gamma_corrected)
    cv2.waitKey(0)  # Bekleme işlemi

# Pencereyi kapatma
cv2.destroyAllWindows()

# Gamma fonksiyonunu çizdirme
gama = 1 / 5
a = np.linspace(0, 1, 50)
print("a = ", a)
g = a ** gama
plt.plot(a, g)
plt.show()