#!/usr/bin/env python

import roslib
import rospy
import smach
import smach_ros
import tf2_ros
from std_msgs.msg import Bool
from move_base_msgs.msg import *
from geometry_msgs.msg import Twist
import rospy
import actionlib
import odrive_smach.msg
import time

class Initialize(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['Run','Preempt'])
    def execute(self, userdata):
        #First Server
        client0 = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        
        #Second Server
        client1 = actionlib.SimpleActionClient("/name1/position",odrive_smach.msg.SetpointAction)

        #Third Server
        client2 = actionlib.SimpleActionClient("/name2/position",odrive_smach.msg.SetpointAction)

        #Fourth Server
        client3 = actionlib.SimpleActionClient("/name3/position",odrive_smach.msg.SetpointAction)

        #Fifth Server
        client4 = actionlib.SimpleActionClient("/name4/position",odrive_smach.msg.SetpointAction)
        
        #Sixth Server
        client5 = actionlib.SimpleActionClient("/name5/position",odrive_smach.msg.SetpointAction)

        #Seventh Server
        client6 = actionlib.SimpleActionClient("/name6/position",odrive_smach.msg.SetpointAction)

        #Eighth Server
        client7 = actionlib.SimpleActionClient("/name7/position",odrive_smach.msg.SetpointAction)

        #Ninth Server
        client8 = actionlib.SimpleActionClient("/name8/position",odrive_smach.msg.SetpointAction)

        #Tenth Server
        client9 = actionlib.SimpleActionClient("/name9/position",odrive_smach.msg.SetpointAction)

        #Let Servers Startup
        client0.wait_for_server()
        client1.wait_for_server()
        client2.wait_for_server()
        client3.wait_for_server()
        client4.wait_for_server()
        client5.wait_for_server()
        client6.wait_for_server()
        client7.wait_for_server()
        client8.wait_for_server()
        client9.wait_for_server()
        return 'Run'

class Drive(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['Mine','Dump','Preempt'])
    def execute(self, userdata):
        return 'Mine'

class Mine(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['Drive','Preempt'])
    def execute(self, userdata):
        return 'Drive'

class Dump(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['Drive','Preempt'])
    def execute(self, userdata):
        return 'Drive'

class Manual_Preemption(smach.State):
    def __init__(self):
        smach.State.__init__(self,
                             outcomes=['Drive','Mine','Dump'])
    def execute(self, userdata):
        return 'Drive'

def main():
    rospy.init_node('smach_example_state_machine')
    sm = smach.StateMachine(outcomes=['outcome4'])
    with sm:
        smach.StateMachine.add('Initialize', Initialize(),
                                transitions={'Run':'Drive',
                                             'Preempt':'Manual_Preemption'})
        smach.StateMachine.add('Drive', Drive(),
                                transitions={'Mine':'Mine',
                                             'Dump':'Dump',
                                             'Preempt':'Manual_Preemption'})
        smach.StateMachine.add('Mine', Mine(),
                                transitions={'Drive':'Drive',
                                             'Preempt':'Manual_Preemption'})
        smach.StateMachine.add('Dump', Dump(),
                                transitions={'Drive':'Drive',
                                             'Preempt':'Manual_Preemption'})
        smach.StateMachine.add('Manual_Preemption', Manual_Preemption(),
                                transitions={'Drive':'Drive',
                                             'Mine':'Mine',
                                             'Dump':'Dump'})
	outcome = sm.execute()

if __name__ == '__main__':
    main()
