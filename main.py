import cv2
import numpy as np
from os import listdir
from os.path import isfile, join
import os

# write image names in list
path = 'original'
files = [f for f in listdir(path) if isfile(join(path, f))]
# loop through all images
for i in range(0, len(files)):
    path = 'original'
    # import image
    image = cv2.imread(os.path.join(path, files[i]))
    # create copy of original image
    output = image.copy()
    # convert color image to grayscale image
    img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Find circles
    circles = cv2.HoughCircles(img, cv2.HOUGH_GRADIENT, 1.3, 100)
    # If some circle is found
    if circles is not None:
        # Get the (x, y, r) as integers
        circles = np.round(circles[0, :]).astype("int")
        # draw the circle and the center
        for (x, y, r) in circles:
            cv2.circle(output, (x, y), r, (0, 255, 0), 2)
            cv2.circle(output, (x, y), 2, (0, 255, 0), -1)
        # save the output image
        path = 'detected'
        cv2.imwrite(os.path.join(path, str(files[i])), output)
    else:
        print("There where no circles found in image: " + files[i] +  " :(")
