import roslib
import rospy
import smach
import smach_ros
import tf2_ros
import StateSpace_BasicMachine
class Return(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_return'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Return")
        return 'outcome_return'

    # E E E E E E E E E E E E
    # END OF SM_SUB_DIGGING
    # E E E E E E E E E E E E

    # S S S S S S S S S S S S
    # START OF SM_SUB_DUMPING
    # S S S S S S S S S S S S
