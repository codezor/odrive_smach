import roslib
import rospy
import smach
import smach_ros
import tf2_ros
import StateSpace_BasicMachine
class Driving(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_mine', 'outcome_dump', 'outcome_manual'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    # Drive chooses to mine, dump, or go to manual (and execute its function)
    def execute(self, userdata):
        #DRIVE STUFF
        
        userdata.x_out = random.randint(0, 2)

        rospy.loginfo(userdata.x_in)

        if(userdata.x_in == 0):
            return 'outcome_manual'

        elif(userdata.x_in == 1):
            return 'outcome_mine'

        else:
            return 'outcome_dump'