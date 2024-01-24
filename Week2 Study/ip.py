import cv2
import numpy as np
from matplotlib import pyplot as plt

# foto2 = cv2.imread("./goruntu/kanal.png")#klasörden görüntü okuma
# cv2.imshow("Kırmızı",foto2)

foto = cv2.imread("baboon.bmp")
cv2.imshow("el",foto)


B = foto[:,:,0]
G = foto[:,:,1]
R = foto[:,:,2]
# cv2.waitKey()

cv2.imshow("Mavi",B)
cv2.imshow("Yesil",G)
cv2.imshow("Kirmizi",R)
cv2.waitKey()

foto_gri = cv2.imread("baboon.bmp",0)
cv2.imshow("baboon_gri",foto_gri)
cv2.waitKey()

# cv2.waitKey()

import matplotlib.image as mpimg
imgGray = 0.2989 * R + 0.5870 * G + 0.1140 * B
plt.imshow(imgGray, cmap='gray')
plt.show()