#!/usr/bin/env python3

import sys
import rospy
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError
from time import sleep

#!/usr/bin/env python3
from image_analyzer import IMAGE_ANALYZER as IA

from constants import PATH_CAM
import cv2
import rospy
import numpy as np

class Crawler:
    def __init__(self):
        rospy.logdebug("[CRW] crawler initialized")
        self.bridge = CvBridge()
        self.image_sub = rospy.Subscriber(PATH_CAM, Image, self.crawl_img, queue_size=1)

    def crawl_img(self, image):
        rospy.logdebug("[CRW] image received")
        
        try:
            cv_image = self.bridge.imgmsg_to_cv2(image, "bgr8")
        except CvBridgeError as e:
            rospy.logerr(e)

        cv2.imshow('test', cv_image)
        cv2.waitKey(1)




# file = open("/root/test.txt", 'a')
# file.write("Hello World!")
# file.close()

CRAWLER = Crawler()


key = ''
while key != 'q':
    key = sys.stdin.readline().strip()
    print('key: {:s}'.format(key))

rospy.signal_shutdown('ending')

# print("Testing input:")
# test_str = sys.stdin.readline()
# print("input: ", test_str)
