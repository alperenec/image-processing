import cv2
import numpy as np

foto = cv2.imread("baboon.bmp")

# görüntünün belirli piksllerini elde etme ve ekranda gösterme
kesit = foto[0:1000, 400:1500]

cv2.imshow("baboon", foto)
cv2.imshow("parca", kesit)

cv2.waitKey(0)
cv2.destroyAllWindows()
