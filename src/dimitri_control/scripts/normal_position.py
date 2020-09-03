#!/usr/bin/env python3

import rospy
from std_msgs.msg import Float64


class InitialPosition:
    def __init__(self):
        pub = [rospy.Publisher('/dimitri/joint'+str(i)+'_position_controller/command', Float64, queue_size=10)
               for i in range(1, 19)]
        rate = rospy.Rate(60)

        while not rospy.is_shutdown():
            for p in pub:
                p.publish(0.0)
            rate.sleep()


if __name__ == '__main__':
    rospy.init_node('initialPosition', anonymous=False, disable_signals=False)
    try:
        InitialPosition()
    except rospy.ROSInterruptException as e:
        print('Error on initializing servos...')
        print(e)