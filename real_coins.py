import cv2 as cv
import numpy as np
import sys

# Reads the given image
img = cv.imread('given_data/real_original.jpg')

# Tests whether the image read operation worked
if img is None:
    sys.exit('Could not read the image.')

# Displays the images and waits until the user presses a key to close it
cv.imshow('Original image', img)
k = cv.waitKey(0)

# Convert into grayscale and display it
img_gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale image', img_gray)
k = cv.waitKey(0)

# Blur image and display it
# 2D Convolution
# kernel = np.ones((20,20), np.float32)/20**2
# img_blurred_conv = cv.filter2D(img_gray, -1, kernel)
# cv.imshow('Blurred image - 2D Convolution', img_blurred)
# k = cv.waitKey(0)

# Averaging
img_blurred = cv.blur(img_gray, (20,20))
cv.imshow('Blurred image - Averaging 20x20', img_blurred)
k = cv.waitKey(0)

# Circle detection
output = img
circles = cv.HoughCircles(img_blurred, cv.HOUGH_GRADIENT, 7, 120,
                            param1=45,
                            param2=300)

print('Number of coins detected =', len(circles[0]))

# ensure at least some circles were found
if circles is not None:
	# convert the (x, y) coordinates and radius of the circles to integers
	circles = np.round(circles[0, :]).astype('int')
	# loop over the (x, y) coordinates and radius of the circles
	for (x, y, r) in circles:
		# draw the circle in the output image, then draw a rectangle
		# corresponding to the center of the circle
		cv.circle(output, (x, y), r, (0, 255, 0), 4)
		cv.rectangle(output, (x - 5, y - 5), (x + 5, y + 5), (0, 0, 255), -1)
    # show the output image
	cv.imshow('output', output)
	cv.waitKey(0)

cv.imwrite('image_result/real_result.jpg', output)
