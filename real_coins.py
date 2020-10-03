import cv2 as cv
import numpy as np
import sys

# Reads the given image
img = cv.imread('given_data/real_original.jpg')

# Tests whether the image read operation worked
if img is None:
    sys.exit("Could not read the image.")

# Displays the images and waits until the user presses a key to close it
cv.imshow("Display window", img)
k = cv.waitKey(0)

# Convert into grayscale
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Display window", img_gray)
k = cv.waitKey(0)
