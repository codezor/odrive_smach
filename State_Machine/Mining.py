import roslib
import rospy
import smach
import smach_ros
import tf2_ros
import StateSpace_BasicMachine

import random

class Mining(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_drive', 'outcome_manual', 'outcome_dig'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        #MINE STUFF

        userdata.x_out = random.randint(0, 2)
        rospy.loginfo(userdata.x_in)

        return 'outcome_dig'

        '''
        if(userdata.x_in == 0):
            return 'outcome_manual'
        else:
            return 'outcome_drive'
        '''