#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CompressedImage
from time import sleep
# from constants import PATH_RASPICAM, PATH_USBCAM, PATH_LIDAR, IS_DEBUG_MODE

# rospy.Subscriber(PATH_RASPICAM, CompressedImage,
#                  _processor.process_fishcam, queue_size=1)
# rospy.Subscriber(PATH_USBCAM, CompressedImage,
#                  _processor.process_frontcam, queue_size=1)
# rospy.Subscriber(PATH_LIDAR, LaserScan, _processor.process_lidar, queue_size=1)

while (1):
    print('testing...')
    sleep(1)
