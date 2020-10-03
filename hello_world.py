import cv2 as cv
import numpy as np
import sys

# img = cv.imread(cv.samples.findFile("starry_night.jpg"))
img = cv.imread('given_data/real_original.jpg')
if img is None:
    sys.exit("Could not read the image.")

# Displays the images and waits until the user presses a key to close it. If the
# key pressed is 's', saves the image
cv.imshow("Display window", img)
k = cv.waitKey(0)
# if k == ord("s"):
#     cv.imwrite("starry_night.png", img)

px = img[100,100]
# print(px)

blue = img[100,100,0]
print(blue)

print('mudança trivial')
