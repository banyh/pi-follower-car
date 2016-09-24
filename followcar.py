import cv2
from camera import Camera
from motor import *

state = 0
left_threshold = 0.3
right_threshold = 0.7

car = Motor()
cam = Camera()
cv2.namedWindow('result')

while True:
    image, (x, y), radius = cam.findSkin()
    cv2.imshow("result", image)
    cv2.waitKey(1)

    if x is None or radius is None:
        # car.go(STOP)
        # action = 'STOP'
        action = 'RIGHT_FORWARD'
        car.go(RIGHT_FORWARD, 70)
        state = 1
    else:
        if state == 1:
            print '>>> FOUND'
            car.go(LEFT_FORWARD, 70)
            time.sleep(0.5)
            car.go(STOP)
            time.sleep(0.5)
            state = 0
        if radius < 0.5:
            if x >= left_threshold and x <= right_threshold:
                action = 'FORWARD'
                car.go(FORWARD)
            elif x < left_threshold:
                action = 'LEFT_FORWARD'
                car.go(LEFT_FORWARD, (left_threshold - x) * 30 + 80)
            elif x > right_threshold:
                action = 'RIGHT_FORWARD'
                car.go(RIGHT_FORWARD, (x - right_threshold) * 30 + 80)
        #elif radius > 0.30:
        #    if x >= left_threshold and x <= right_threshold:
        #        action = 'BACKWARD'
        #        car.go(BACKWARD)
        #    elif x < left_threshold:
        #        action = 'RIGHT_BACKWARD'
        #        car.go(RIGHT_BACKWARD, (left_threshold - x) * 30 + 80)
        #    elif x > right_threshold:
        #        action = 'LEFT_BACKWARD'
        #        car.go(LEFT_BACKWARD, (x - right_threshold) * 30 + 80)
        else:
            car.go(STOP)
            action = 'STOP'
    print '{}, ({:.2}, {:.2}), r={:.2}'.format(action, x, y, radius)

cv2.destroyAllWindows()
