from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import cv2


class Camera(object):
    def __init__(self):
        self.camera = PiCamera(resolution=(320, 240), framerate=30)
        self.camera.hflip = True
        self.camera.vflip = True
        self.rawCapture = PiRGBArray(self.camera, size=(320, 240))
        time.sleep(0.1)
        self.frames = self.camera.capture_continuous(self.rawCapture, format="bgr", use_video_port=True)

    def __del__(self):
        self.camera.close()

    def getImage(self):
        image = self.frames.next().array
        self.rawCapture.truncate(0)
        return image

    def findSkin(self):
        image = self.getImage()
        hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
        mask = cv2.inRange(hsv, (121, 0, 0), (179, 255, 255))
        mask = cv2.erode(mask, None, iterations=2)
        mask = cv2.GaussianBlur(mask, (9, 9), 0)
        contours, _ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
        # cv2.drawContours(image, contours, -1, (255, 0, 0), 3)

        width = float(self.camera.resolution[0])
        height = float(self.camera.resolution[1])
        center = None, None
        radius = None
        if len(contours) > 0:
            c = max(contours, key=cv2.contourArea)
            ((x, y), radius) = cv2.minEnclosingCircle(c)
            M = cv2.moments(c)
            try:
                center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))
                cv2.circle(image, (int(x), int(y)), int(radius), (0, 255, 0), 5)
                cv2.circle(image, center, 5, (0, 255, 0), -1)
                center = (center[0] / width, center[1] / height)  # between 0~1
                radius = radius / width
            except:
                pass
        return image, center, radius
