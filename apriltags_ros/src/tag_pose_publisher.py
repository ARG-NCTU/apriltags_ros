#!/usr/bin/env python

import rospy
from apriltags_ros.msg import AprilTagDetectionArray
from geometry_msgs.msg import PoseStamped

def callback(data):
    for detection in data.detections:
        if detection.id == 1:
            tag_pose = PoseStamped()
            tag_pose.header = detection.pose.header
            tag_pose.pose = detection.pose.pose
            tag_pose_publisher.publish(tag_pose)

if __name__ == '__main__':
    rospy.init_node('tag_pose_publisher', anonymous=True)
    tag_pose_publisher = rospy.Publisher('/tag_pose', PoseStamped, queue_size=10)
    rospy.Subscriber('/tag_detections', AprilTagDetectionArray, callback)
    rospy.spin()

