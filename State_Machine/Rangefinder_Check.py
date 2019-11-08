import roslib
import rospy
import smach
import smach_ros
import tf2_ros
import StateSpace_BasicMachine
class Rangefinder_Check(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Rangefinder_Check")
        return 'outcome_next'