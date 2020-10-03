import cv2 as cv
import numpy as np
import sys

# Reads the given image
img = cv.imread('given_data/real_original.jpg')

# Tests whether the image read operation worked
if img is None:
    sys.exit("Could not read the image.")

# Displays the images and waits until the user presses a key to close it
cv.imshow("Original image", img)
k = cv.waitKey(0)

# Convert into grayscale and display it
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Grayscale image", img_gray)
k = cv.waitKey(0)

# Blur image and display it
# 2D Convolution
# kernel = np.ones((20,20), np.float32)/20**2
# img_blurred_conv = cv.filter2D(img_gray, -1, kernel)
# cv.imshow("Blurred image - 2D Convolution", img_blurred)
# k = cv.waitKey(0)

# Averaging
img_blurred = cv.blur(img_gray, (20,20))
cv.imshow("Blurred image - Averaging 20x20", img_blurred)
k = cv.waitKey(0)
