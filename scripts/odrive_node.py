#!/usr/bin/env python
import rospy
from odrive_ros.odrive_interface import ODrive_ROS
import pprint
import sys
if __name__=="__main__":
	rospy.init_node("%s"%(sys.argv[1]))
	odrive_node = ODrive_ROS("%s"%(sys.argv[1]))
	rate = rospy.Rate(1)
	while not rospy.is_shutdown():
		#print("%s"%(sys.argv[1]))
		odrive_node.update()
		rate.sleep()
