import cv2 as cv
import numpy as np
import sys

# Reads the given image
img = cv.imread('given_data/dolar_original.png')

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

# Inverse binary threshold conversion and display
ret, img_bin = cv.threshold(img_gray,35,255,cv.THRESH_BINARY_INV)
cv.imshow("Binary Threshold", img_bin)
k = cv.waitKey(0)

# Apply morphological filter
# Different types of morphological filters were tested
# Define a 5x5 matrix of ones as the filter kernel
kernel = np.ones((5,5), np.uint8)
# img_eroded = cv.erode(img_bin, kernel, iterations=1)
# img_dilated = cv.dilate(img_bin, kernel, iterations=1)
# img_open = cv.morphologyEx(img_bin, cv.MORPH_OPEN, kernel)
img_close = cv.morphologyEx(img_bin, cv.MORPH_CLOSE, kernel, iterations=3)
# cv.imshow("Eroded img", img_eroded)
# cv.imshow("Dilated img", img_dilated)
# cv.imshow("Openned img", img_open)
cv.imshow("Morphological filter img - Type Closed", img_close)
k = cv.waitKey(0)

# Setup SimpleBlobDetector ans it's parameters.
params = cv.SimpleBlobDetector_Params()

# Filter the blob by area.
params.filterByArea = True
params.minArea = 1000
params.maxArea = 100000

# Initialize SimpleBlobDetector with the above defined parameters
detector = cv.SimpleBlobDetector_create(params)

# Apply the detector to the filtered image and print the amount of detected
# coins
keypoints = detector.detect(img_close)
print('Number of coins detected =', len(keypoints))

# Draw detected blobs as red circles.
# cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS ensures the size of the circle
# corresponds to the size of blob
img_filtered_with_keypoints = cv.drawKeypoints(img_close, keypoints, np.array([]),
                                        (0,0,255),
                                        cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Show keypoints drawn over the filtered image
cv.imshow("Keypoints over filtered img", img_filtered_with_keypoints)
cv.waitKey(0)

# ensure at least some circles were found
output = img # used to draw over the original image
if keypoints is not None:
    centers = []
    radii = []
    for i in keypoints:
        # extracts the center and radii from the keypoints and stores them in lists
        centers.append(i.pt)
        radii.append(i.size/2)
    # convert the (x, y) coordinates and radius of the circles to integers
    centers = np.round(centers[:]).astype("int")
    radii = np.round(radii[:]).astype("int")
    # loop over the (x, y) coordinates and radius of the circles
    for i,j in enumerate(centers):
        # draw the circle in the output image, then draw a rectangle
        # corresponding to the center of the circle
        cv.circle(output, tuple(j), radii[i], (0, 255, 0), 2)
        cv.rectangle(output, (j[0] - 5, j[1] - 5), (j[0] + 5, j[1] + 5), (255, 0, 0), -1)


# show the output image
cv.imshow("output", output)
cv.waitKey(0)

# Save otput to image_result directory
cv.imwrite('image_result/dolar_result.png', output)
