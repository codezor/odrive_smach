#!/usr/bin/env python
import roslib
import rospy
import smach
import smach_ros
import tf2_ros

import odrive_smach
import actionlib
import Return
import odrive_smach.msg

class BL_ON(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_ON")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())
            
        return 'outcome_next'

class Robot_Lower(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Robot_Lower")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

class Dump_Move(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Move")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

class BL_Lower(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_Lower")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

class Dump_Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Stop")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

class Timeout(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Timeout")

        return 'outcome_next'

class Whole_Raise(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_Raise")

        client = actionlib.SimpleActionClient("/name0/position",odrive_smach.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_smach.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=Return.fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

def digger_main():
    rospy.init_node('smach_example_state_machine')

    # Create a SMACH state machine
    sm_digger = smach.StateMachine(outcomes = ['end_digging'],
                                input_keys = ['aVar'],
                                output_keys = ['aVar'])
    sm_digger.userdata.sm_counter = 0
    sm_digger.userdata.e_stop = False

    # Open the container
    with sm_digger:
        smach.StateMachine.add('BL_On', BL_ON(), 
                                   transitions = {'outcome_next':'Robot_Lower'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
        smach.StateMachine.add('Robot_Lower', Robot_Lower(), 
                                   transitions = {'outcome_next':'Dump_Move'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
        smach.StateMachine.add('Dump_Move', Dump_Move(), 
                                   transitions = {'outcome_next':'BL_Lower'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})                                                       
        smach.StateMachine.add('BL_Lower', BL_Lower(), 
                                   transitions = {'outcome_next':'Timeout'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})    
        smach.StateMachine.add('Timeout', Timeout(), 
                                   transitions = {'outcome_next':'Dump_Stop'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
        smach.StateMachine.add('Dump_Stop', Dump_Stop(), 
                                   transitions = {'outcome_next':'Whole_Raise'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
        smach.StateMachine.add('Whole_Raise', Whole_Raise(), 
                                   transitions = {'outcome_next':'Return'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})                                                       
        smach.StateMachine.add('Return', Return.Return(), 
                                   transitions = {'outcome_return':'end_digging'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})   
	return sm_digger

if __name__ == '__main__':
    digger_main()                                                  
