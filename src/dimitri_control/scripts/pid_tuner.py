#!/usr/bin/env python
import numpy as np
import random
from itertools import count
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import rospy
from std_msgs.msg import Float64

plt.style.use('fivethirtyeight')

class PIDTuner:
    def __init__(self):
        self.pub = rospy.Publisher('/dimitri/joint1_position_controller/command', Float64, queue_size=10)
        self.rate = rospy.Rate(60)

    def publisher(self):
        self.desiredv = np.sin(rospy.get_time()/60)*10
        while not rospy.is_shutdown():
            self.pub.publish(self.desiredv)
            self.rate.sleep()
    

        
        


if __name__ == '__main__':


    rospy.init_node('pid_tuner', anonymous=False, disable_signals=False)

    a = PIDTuner()
 
    try:
        a.publisher()
        
    except rospy.ROSInterruptException as e:
        print('Error on initializing servos...')
        print(e)
