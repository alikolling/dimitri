#!/usr/bin/env python3

import cv2
import rospy
import numpy as np
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import time


class RecordVideo:
    def __init__(self):
        self.bridge = CvBridge()
        img_sub = rospy.Subscriber('/dimitri/camera1/image_raw', Image, self.get_image)
        rospy.spin()

    def get_image(self, data):
        cv_image = self.bridge.imgmsg_to_cv2(data, 'bgr8')
        cv2.imshow('Frame', cv_image)
        cv2.waitKey(1)


if __name__ == '__main__':
    rospy.init_node('recordingVideo', anonymous=False, disable_signals=False)
    try:
        RecordVideo()
    except rospy.ROSInterruptException as e:
        print('Error on recording video...')
        print(e)
