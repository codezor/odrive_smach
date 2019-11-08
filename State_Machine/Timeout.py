import roslib
import rospy
import smach
import smach_ros
import tf2_ros
import StateSpace_BasicMachine
class Timeout(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Timeout")

        return 'outcome_next'