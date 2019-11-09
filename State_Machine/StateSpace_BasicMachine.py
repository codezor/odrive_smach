#!/usr/bin/env python
#--------------------

import roslib
import rospy
import smach
import smach_ros
import tf2_ros
#from std_msgs.msg import Bool
#from move_base_msgs.msg import

import odrive_ros
import actionlib

import 2020_Digging_State_Machine
import 2020_

import random # Just to Infinite Move


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
        client0 = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        
        #Second Server
        client1 = actionlib.SimpleActionClient("/name1/position",odrive_ros.msg.SetpointAction)

        #Third Server
        client2 = actionlib.SimpleActionClient("/name2/position",odrive_ros.msg.SetpointAction)

        #Fourth Server
        client3 = actionlib.SimpleActionClient("/name3/position",odrive_ros.msg.SetpointAction)

        #Fifth Server
        client4 = actionlib.SimpleActionClient("/name4/position",odrive_ros.msg.SetpointAction)
        
        #Sixth Server
        client5 = actionlib.SimpleActionClient("/name5/position",odrive_ros.msg.SetpointAction)

        #Seventh Server
        client6 = actionlib.SimpleActionClient("/name6/position",odrive_ros.msg.SetpointAction)

        #Eighth Server
        client7 = actionlib.SimpleActionClient("/name7/position",odrive_ros.msg.SetpointAction)

        #Ninth Server
        client8 = actionlib.SimpleActionClient("/name8/position",odrive_ros.msg.SetpointAction)

        #Tenth Server
        client9 = actionlib.SimpleActionClient("/name9/position",odrive_ros.msg.SetpointAction)

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
        smach.StateMachine.add('Start_Digging', 2020_Digging_State_Machine.sm_digger,
                               transitions={'end_digging':'Dump'},
                               remapping = {'aVar':'aVariable',
                                            'aVar':'aVariable'})

        # Create Dump Sub Container
        smach.StateMachine.add('Start_Dumping', 2020_Dumping_State_Machine.sm_dumper,
                               transitions={'end_dumping':'Drive'},
                               remapping = {'aVari':'aVariable',
                                            'aVari':'aVariable'})

    sis = smach_ros.IntrospectionServer('state_machine', sm, '/SM_ROOT')
    sis.start()
    
    # Execute SMACH plan
    sm_main.execute()

    rospy.spin()
    sis.stop()


if __name__ == '__main__':
    main()