#!/usr/bin/env python3

import rospy
from sensor_msgs.msg import CameraInfo,CompressedImage

class camera_info_test():
    def __init__(self):
        rospy.Subscriber('/unity/camera_under/compressed', CompressedImage, self.camera_info, queue_size=10)
        self.camera_info_pub = rospy.Publisher('/unity/camera_info', CameraInfo, queue_size=10)
        self.camera_info_msg = CameraInfo()
        self.camera_info_msg.height = 480
        self.camera_info_msg.width = 640
        self.camera_info_msg.distortion_model = "plumb_bob"
        self.camera_info_msg.K = [416.66667, 0.0, 320.0, 0.0, 418.3333, 240.0, 0.0, 0.0, 1.0]
        self.camera_info_msg.R = [1.0, 0.0, 0.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0]
        self.camera_info_msg.P = [416.66667, 0.0, 320.0, 0.0, 0.0, 418.3333, 240.0, 0.0, 0.0, 0.0, 1.0, 0.0]
        
    def camera_info(self, msg):
        self.camera_info_msg.header = msg.header
        self.camera_info_pub.publish(self.camera_info_msg)

if __name__=='__main__':
    rospy.init_node("camera_info_test", anonymous=False)
    test = camera_info_test()

    rospy.spin()
