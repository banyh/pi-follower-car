import cv2
import numpy as np
import sys
from camera import Camera

cam = Camera()

# Creating a window for later use
cv2.namedWindow('result')

while True:
    frame, _, _ = cam.findSkin()
    cv2.imshow("result", frame)
    cv2.waitKey(1)

cv2.destroyAllWindows()
