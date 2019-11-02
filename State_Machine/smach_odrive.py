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
import odrive_ros.msg
import time

def fdbk_cb(msg):
    print(msg)
    return

class Startup(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes=['begin'])
    def execute(self,userdata):
        rospy.loginfo('Executing state Startup')
        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        print('server is up')
        return 'begin'

class Positive_rotation(smach.State):
    def __init__(self):
        smach.State.__init__(self,outcomes=['done'])
    def execute(self,userdata):
        rospy.loginfo('Executing state Positive Rotation')
        client = actionlib.SimpleActionClient('/name0/position',odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        rotation = odrive_ros.msg.SetpointGoal(setpoint = 10)
        client.send_goal(rotation,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())
        return 'done'

class Negative_rotation(smach.State):
    def __init__(self):
        smach.State.__init__(self,outcomes=['done'])
    def execute(self,userdata):
        rospy.loginfo('Executing state Negative Rotation')
        client = actionlib.SimpleActionClient('/name0/position',odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        rotation = odrive_ros.msg.SetpointGoal(setpoint = -10)
        client.send_goal(rotation,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())
        return 'done'


rospy.init_node('smach_odrive')
print('init node')
sm_odrive = smach.StateMachine(outcomes=['end'])

with sm_odrive:
    smach.StateMachine.add('Startup',Startup(),
        transitions={'begin':'Positive_rotation'})
    print('add Startup')
    #rotation = odrive_ros.msg.SetpointGoal(setpoint = 10)
    #smach.StateMachine.add('Positive_rotation', smach_ros.SimpleActionState('/name0/position',
    #    odrive_ros.msg.SetpointAction,
    #    goal=rotation),
    #    transitions={'succeeded':'Negative_rotation',
    #                 'preempted':'Positive_rotation',
    #                 'aborted':'end'})
    smach.StateMachine.add('Positive_rotation',Positive_rotation(),
        transitions={'done':'Negative_rotation'})
    print('add Positive_rotation')
    #rotation = odrive_ros.msg.SetpointGoal(setpoint = -10)
    #smach.StateMachine.add('Negative_rotation', smach_ros.SimpleActionState('/name0/position',
    #    odrive_ros.msg.SetpointAction,
    #    goal=rotation),
    #    transitions={'succeeded':'Positive_rotation',
    #                 'preempted':'Negative_rotation',
    #                 'aborted':'end'})
    smach.StateMachine.add('Negative_rotation',Negative_rotation(),
        transitions={'done':'Positive_rotation'})
    print('add Negative_rotation')

outcome = sm_odrive.execute()
    