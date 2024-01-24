import cv2
import matplotlib.pyplot as plt

def gri_histogram(resim):

  genişlik, yükseklik = resim.shape

  histogram = [0] * 256

  for i in range(genişlik):
    for j in range(yükseklik):
      histogram[resim[i, j]] += 1
  return histogram

def main():
  resim = cv2.imread("baboon.bmp", cv2.IMREAD_GRAYSCALE)
  cv2.imshow("resim", resim)
  cv2.waitKey()

  histogram = gri_histogram(resim)

  plt.plot(histogram)
  plt.show()

if __name__ == "__main__":
  main()