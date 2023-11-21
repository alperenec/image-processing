import cv2
import numpy as np

# kamerayı açar
cap = cv2.VideoCapture(0)


while True:
    ret, frame = cap.read()

    #BGR'den HSV'ye dönüştüren kod
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    #kırmızı için aralıl
    alt_deger_red = np.array([0, 115, 115])
    upper_red = np.array([10, 255, 255])

    # Mavi için aralık
    alt_deger_blue = np.array([75, 100, 100])
    upper_blue = np.array([125, 255, 255])

    #yeşil için aralık
    alt_deger_green = np.array([50, 100, 100])
    upper_green = np.array([100, 255, 255])

    # Kırmızı tonunda pikselleri beyaz, mavi ve yeşil tonunda pikselleri siyah yapan kod
    mask_red = cv2.inRange(hsv, alt_deger_red, upper_red)
    mask_black = cv2.inRange(hsv, alt_deger_blue, upper_blue) | cv2.inRange(hsv, alt_deger_green, upper_green)

    result = cv2.bitwise_and(frame, frame, mask=mask_red)

    #Mavi ve yeşil ton görüntü siyah olsun
    result[mask_black > 0] = [0, 0, 0]

    #HSV'den BGR'ye tekrar dönüştür
    result_bgr = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

    cv2.imshow('Original', frame)
    cv2.imshow('Result', result_bgr)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.imwrite("webcam_fotografi.jpg", frame)
cv2.imwrite("webcam_fotografi2.jpg", result_bgr)

cv2.destroyAllWindows()