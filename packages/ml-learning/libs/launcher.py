#!/usr/bin/env python3
""" a module to launch modules """

import rospy
import sys
import os

# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# sys.path.append('/opt/ros/melodic/lib/python3.5/dist-packages')

print()
print("========= GALAPAGOS CORMORANT =========")
print("  Ver 0.0.1")
print("  Konkuk University")
print("  Electronics Engineering")
print("  Author: Kim Ji Hyeong")
print("          (kjhricky@gmail.com)")
print("=======================================")

if sys.argv[1] == "full":
    print("  Image learning: FULL")

if sys.argv[2] == "True":
    print("  DEBUG MODE enabled.")
    
print("=======================================")
print()

# from constants import PATH_GALAPAGOS_STATE
from time import sleep  # * Variables
from scheduler import SCHEDULER

RUN_TYPE = 'run_' + sys.argv[1]


# * Main Codes
if __name__ == '__main__':
    try:
        rospy.loginfo("[LAUNCH] executing: %s" % RUN_TYPE)

        SCHEDULER.load_module(RUN_TYPE)

        rospy.loginfo("[LAUNCH] Galapagos package is spinning.")
        rospy.spin()

    except KeyboardInterrupt:
        print("\r", end='')


    for i in [1]:
        print("Turning off in %d s...\r" % i, end='')
        sleep(1)

    rospy.loginfo("[LAUNCH] Package ended.")
