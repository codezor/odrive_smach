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