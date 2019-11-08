#!/usr/bin/env python
#--------------------

import roslib
import rospy
import smach
import smach_ros
import tf2_ros
#from std_msgs.msg import Bool
#from move_base_msgs.msg import

import random # Just to Infinite Move
import Drive
import Mining
import Dump
import BL_ON
import BL_Lower
import Dump_Move
import Robot_Lower
import Timeout
import Dump_Stop
import BL_Raise
import Return
import Rangefinder_Check
import BL_Move
import Dump_Rotate
import Dump_Lower
import BL_Reset

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
'''
# line 69 to 91 copied to Drive.py
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
'''
'''
# line 94 to 115 copied to Mining.py file
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

        ############################ tripple quote here
        if(userdata.x_in == 0):
           return 'outcome_manual'
        else:
            return 'outcome_drive'
        ############################## tripple quote end here
'''

'''
# line 119 to 137 copied in Dump.py
class Dump(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_drive', 'outcome_manual', 'outcome_dump'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        #DUMP STUFF

        userdata.x_out = random.randint(0, 2)
        rospy.loginfo(userdata.x_in)

        return 'outcome_dump'
        ############################## tripple qyote here
        if(userdata.x_in == 0):
            return 'outcome_manual'
        else:
            return 'outcome_drive'
        ############################# tripple quote end here
'''

'''
# line 142 to 159 copied to Manual_Control.py file
class Manual_Control(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_mine', 'outcome_dump', 'outcome_drive'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        #MANUAL STUFF

        userdata.x_out = random.randint(0, 2)
        rospy.loginfo(userdata.x_in)

        if(userdata.x_in == 0):
            return 'outcome_mine'
        elif(userdata.x_in == 1):
            return 'outcome_dump'
        else:
            return 'outcome_drive'
'''
    # S S S S S S S S S S S S
    # START OF SM_SUB_DIGGING
    # S S S S S S S S S S S S
'''
# line 166 to 182 copied to Bl_ON.py file
class BL_ON(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_ON")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())
            
        return 'outcome_next'
'''
'''
# line 186 to 202 copied to BL_Lower.py file
class BL_Lower(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_Lower")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''
'''
# line 209 to 225 copied to Dump_Move.py file
class Dump_Move(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Move")

                client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''

'''
# line 230 to 246 copied to Robot_Lower.py file
class Robot_Lower(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Robot_Lower")

                client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''

'''
# line 253 to 262 copied to Timeout.py file
class Timeout(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
'             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Timeout")

        return 'outcome_next'
'''

'''
# line 268 to 284 copied to Dump_Move.py file
class Dump_Stop(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Stop")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''

'''
# line 290 to 306 copied to BL_Raise.py file
class BL_Raise(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_Raise")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''

'''
# line 312 to 328 copied to Return.py file
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
'''

'''
# line 334 to 342 copied to Rangefinder_Check.py file
class Rangefinder_Check(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Rangefinder_Check")
        return 'outcome_next'
'''

'''
# line to 348 to 364 copied to BL_Move.py file
class BL_Move(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_Move")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''

'''
# line 371 to 387 copied to Dump_Rotate.py file
class Dump_Rotate(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Rotate")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''

'''
# line 393 to 409 copied to Dump_Lower.py file
class Dump_Lower(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: Dump_Lower")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'
'''       

'''
# line 415 to 435 copied to BL_Reset.py file
class BL_Reset(smach.State):
    def __init__(self):
        smach.State.__init__(self, outcomes = ['outcome_next'],
                                input_keys = ['x_in'],
                                output_keys = ['x_out'])
             
    def execute(self, userdata):
        rospy.loginfo("Running --> Sub Digging: BL_reset")

        client = actionlib.SimpleActionClient("/name0/position",odrive_ros.msg.SetpointAction)
        client.wait_for_server()
        goal = odrive_ros.msg.SetpointGoal(setpoint=10)
        client.send_goal(goal,feedback_cb=fdbk_cb)
        client.wait_for_result()
        print(client.get_result())

        return 'outcome_next'

    # E E E E E E E E E E E E
    # END OF SM_SUB_DIGGING
    # E E E E E E E E E E E E
'''


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
        smach.StateMachine.add('Mine', Mining(), 
                                transitions = {'outcome_drive':'Drive',
                                               'outcome_manual':'Manual',
                                               'outcome_dig':'Start_Digging'},
                                remapping = {'x_in':'aVariable',
                                             'x_out':'aVariable'})
        smach.StateMachine.add('Dump', Dump(), 
                                transitions = {'outcome_drive':'Drive',
                                               'outcome_manual':'Manual',
                                               'outcome_dump':'Start_Dumping'},
                                remapping = {'x_in':'aVariable',
                                             'x_out':'aVariable'})                                                       
        smach.StateMachine.add('Manual', Manual_Control(), 
                                transitions = {'outcome_drive':'Drive',
                                               'outcome_mine':'Mine',
                                               'outcome_dump':'Dump'},
                                remapping = {'x_in':'aVariable',
                                             'x_out':'aVariable'})    

                # Create Sub Container
        sm_sub_dig = smach.StateMachine(outcomes = ['end_digging'],
                                input_keys = ['aVar'],
                                output_keys = ['aVar'])

        # Sub State where Loop will occur
        with sm_sub_dig:
            smach.StateMachine.add('BL_On', BL_ON(), 
                                   transitions = {'outcome_next':'BL_Lower'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
            smach.StateMachine.add('BL_Lower', BL_Lower(), 
                                   transitions = {'outcome_next':'Dump_Move'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
            smach.StateMachine.add('Dump_Move', Dump_Move(), 
                                   transitions = {'outcome_next':'Robot_Lower'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})                                                       
            smach.StateMachine.add('Robot_Lower', Robot_Lower(), 
                                   transitions = {'outcome_next':'Timeout'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})    
            smach.StateMachine.add('Timeout', Timeout(), 
                                   transitions = {'outcome_next':'Dump_Stop'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
            smach.StateMachine.add('Dump_Stop', Dump_Stop(), 
                                   transitions = {'outcome_next':'BL_Raise'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})
            smach.StateMachine.add('BL_Raise', BL_Raise(), 
                                   transitions = {'outcome_next':'Return'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})                                                       
            smach.StateMachine.add('Return', Return(), 
                                   transitions = {'outcome_return':'end_digging'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})   
        # Start up the Loop in a Sub State                                        
        smach.StateMachine.add('Start_Digging', sm_sub_dig,
                               transitions={'end_digging':'Dump'},
                               remapping = {'aVar':'aVariable',
                                            'aVar':'aVariable'})

        # Create Sub Container
        sm_sub_dump = smach.StateMachine(outcomes = ['end_dumping'],
                                input_keys = ['aVar'],
                                output_keys = ['aVar'])

        # Sub State where Loop will occur
        with sm_sub_dump:
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
            smach.StateMachine.add('Return', Return(), 
                                   transitions = {'outcome_return':'end_dumping'},
                                   remapping = {'x_in':'aVar',
                                                'x_out':'aVar'})   
        # Start up the Loop in a Sub State                                        
        smach.StateMachine.add('Start_Dumping', sm_sub_dump,
                               transitions={'end_dumping':'Drive'},
                               remapping = {'aVar':'aVariable',
                                            'aVar':'aVariable'})

    # Execute SMACH plan
    sm_main.execute()


if __name__ == '__main__':
    main()