#!/usr/bin/env python
#--------------------

import roslib
import rospy
import smach
import smach_ros
import tf2_ros
#from std_msgs.msg import Bool
#from move_base_msgs.msg import

import odrive_smach
import actionlib
import odrive_smach.msg

import Digging_State_Machine
import Dumping_State_Machine
import Drive
import Mining
import Dump
import Manual_Control

import random # Just to Infinite Move


def fdbk_cb(msg):
    print(msg)
    return

class Starting(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_start'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
    
    # Should Execute Startup Sequence
    def execute(self, userdata):
        rospy.loginfo('Starting up the State Machine')
        rospy.loginfo(userdata.x_in)

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

        return 'outcome_start'


# main
def main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm_main = smach.StateMachine(outcomes = ['TisUseless'])
    sm_main.userdata.aVariable = 0

    sm_dumper=Dumping_State_Machine.dumper_main()
    sm_digger=Digging_State_Machine.digger_main()

    # Open the container
    with sm_main:
        # Add startup state to the Container
        smach.StateMachine.add('Startup', Starting(), 
                               transitions = {'outcome_start':'Drive'},
                               remapping = {'x_in':'aVariable',
                                            'x_out':'aVariable'})

        # Under here are the states that will continue to loop
        smach.StateMachine.add('Drive', Drive.Driving(), 
                                transitions = {'outcome_mine':'Mine',
                                               'outcome_dump':'Dump',
                                               'outcome_manual':'Manual'},
                                remapping = {'x_in':'aVariable',
                                             'x_out':'aVariable'})
        smach.StateMachine.add('Mine', Mining.Mining(),
                                transitions = {'outcome_drive':'Drive',
                                               'outcome_manual':'Manual',
                                               'outcome_dig':'Start_Digging'},
                                remapping = {'x_in':'aVariable',
                                             'x_out':'aVariable'})
        smach.StateMachine.add('Dump', Dump.Dump(),
                                transitions = {'outcome_drive':'Drive',
                                               'outcome_manual':'Manual',
                                               'outcome_dump':'Start_Dumping'},
                                remapping = {'x_in':'aVariable',
                                             'x_out':'aVariable'})                                                       
        smach.StateMachine.add('Manual', Manual_Control.Manual_Control(), 
                                transitions = {'outcome_drive':'Drive',
                                               'outcome_mine':'Mine',
                                               'outcome_dump':'Dump'},
                                remapping = {'x_in':'aVariable',
                                             'x_out':'aVariable'})    

        # Create Dig Sub Container
        smach.StateMachine.add('Start_Digging', sm_digger,
                               transitions={'end_digging':'Dump'},
                               remapping = {'aVar':'aVariable',
                                            'aVar':'aVariable'})

        # Create Dump Sub Container
        smach.StateMachine.add('Start_Dumping', sm_dumper,
                               transitions={'end_dumping':'Drive'},
                               remapping = {'aVari':'aVariable',
                                            'aVari':'aVariable'})

    sis = smach_ros.IntrospectionServer('state_machine', sm_main, '/SM_ROOT')
    sis.start()
    
    # Execute SMACH plan
    sm_main.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()
