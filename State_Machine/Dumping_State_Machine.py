#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
import tf2_ros

import odrive_smach
import actionlib
import Return

class Rangefinder_Check(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Rangefinder_Check")
        return 'outcome_next'

class BL_Move(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_Move")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

class BL_Reset(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_reset")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

class Dump_Lower(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Lower")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

class Dump_Rotate(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Rotate")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'


def dumper_main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm_dumper = smach.StateMachine(outcomes = ['end_dumping'])
    sm_dumper.userdata.sm_counter = 0
    sm_dumper.userdata.e_stop = False

    # Open the container
    with sm_dumper:
        smach.StateMachine.add('Rangerfinder_Check', Rangefinder_Check(), 
                                   transitions = {'outcome_next':'BL_Move'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
        smach.StateMachine.add('BL_Move', BL_Move(), 
                                   transitions = {'outcome_next':'Dump_Rotate'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
        smach.StateMachine.add('Dump_Rotate', Dump_Rotate(), 
                                   transitions = {'outcome_next':'Dump_Lower'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})                                                       
        smach.StateMachine.add('Dump_Lower', Dump_Lower(), 
                                   transitions = {'outcome_next':'BL_Reset'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})   
        smach.StateMachine.add('BL_Reset', BL_Reset(), 
                                   transitions = {'outcome_next':'Return'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})                                                      
        smach.StateMachine.add('Return', Return.Return(), 
                                   transitions = {'outcome_return':'end_dumping'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})   

	return sm_dumper

if __name__ == '__main__':
    dumper_main()                                                  
