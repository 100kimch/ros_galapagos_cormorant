#!/usr/bin/env python3
""" a module to launch modules """

import rospy
import sys
# sys.path.remove('/opt/ros/kinetic/lib/python2.7/dist-packages')
# sys.path.append('/opt/ros/kinetic/lib/python3.5/dist-packages')

print()
print("========= GALAPAGOS CORMORANT =========")
print("  Ver 0.0.1")
print("  Konkuk University")
print("  Electronics Engineering")
print("  Author: Kim Ji Hyeong")
print("          (kjhricky@gmail.com)")
print("=======================================")

if sys.argv[1] == "full":
    print(" Image learning: FULL")

print("=======================================")
print()

from constants import PATH_GALAPAGOS_STATE
from time import sleep  # * Variables

RUN_TYPE = 'run_' + sys.argv[1]

# * Main Codes
if __name__ == '__main__':
    try:
        rospy.loginfo("[LAUNCH] executing: %s" % RUN_TYPE)

        if RUN_TYPE in sys.modules:
            sys.modules[RUN_TYPE]
        else:
            __import__(RUN_TYPE, fromlist=[RUN_TYPE])


                # module_path = "mypackage.%s" % module
        module_path = module

        if RUN_TYPE in sys.modules:
            return sys.modules[module_path]

        __import__(module_path, fromlist=[module])
        SCHEDULER.load_module(RUN_TYPE)

        rospy.loginfo("[LAUNCH] Galapagos package started.")
        rospy.spin()

        # if sys.argv[1] == "viewer":
        #     rospy.spin()
        # else:
        #     while not rospy.is_shutdown():
        #         TURTLE.move()
        #         rospy.Rate(30).sleep()

    except KeyboardInterrupt:
        print("\r", end='')

    for i in [1]:
        print("Turning off in %d s...\r" % i, end='')
        sleep(1)

    rospy.loginfo("[LAUNCH] Package ended.")
