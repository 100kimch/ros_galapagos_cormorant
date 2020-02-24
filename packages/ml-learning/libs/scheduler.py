#!/usr/bin/env python3

# NOTE: Scheduler for GALAPAGOS_CORMORANT
# author: Kim Jihyeong(kjhricky@gmail.com)
# written in 2020 Feb 23

import sys
import os
import rospy
from std_msgs.msg import String

class Scheduler():
    def __init__(self):
        """ initializer """
        self.path = os.path.split(sys.path[0])[0]
        sys.path.append(self.path + '/runners/')
        sys.path.append(self.path + '/libs/')

        # Check debug mode
        if sys.argv[2] == 'True':
            self.node = rospy.init_node('GC_' + sys.argv[1],
                anonymous=False, log_level=rospy.DEBUG)
            self.is_debug = True
        else:
            self.node = rospy.init_node('GC_' + sys.argv[1],
                anonymous=False)
            self.is_debug = False

    def load_module(self, module_name):
        if module_name in sys.modules:
            return sys.modules[module_name]
        return __import__(module_name, fromlist=[module_name])
        
SCHEDULER = Scheduler()