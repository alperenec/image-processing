import cv2
import numpy as np

def apply_threshold(image_path, threshold):
    image = cv2.imread(image_path)

    _, thresholded_image = cv2.threshold(image, threshold, 255, cv2.THRESH_BINARY)

    return thresholded_image

image_path = 'pirincfotosu.jpg'
threshold_value = 200
thresholded_image = apply_threshold(image_path, threshold_value)

