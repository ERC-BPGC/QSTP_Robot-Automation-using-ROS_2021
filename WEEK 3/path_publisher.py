#!/usr/bin/env python3
import rospy
from nav_msgs.msg import Path
from geometry_msgs.msg import Point, Pose, PoseStamped, Quaternion
from std_msgs.msg import Header
import sys

PATH1 = [(0, 0,), (3, 0)] # Simple Straight Line
PATH2 = [(0, 0), (3, 0), (3, 3), (0, 3), (0, 0)] # Simple Square
PATH3 = [(0, 0), (1, 3), (2, -3), (3, 5), (0, -2)] # Random Path

def return_path_message(PATH):
    path = Path()
    path.header = Header(frame_id="odom", stamp=rospy.Time.now())
    for pt in PATH:
        pose = PoseStamped()
        pose.header = path.header
        pose.pose.position = Point(pt[0], pt[1], 0)
        pose.pose.orientation = Quaternion(0, 0, 0, 1)

        path.poses.append(pose)
    return path

if __name__ == "__main__":
    rospy.init_node("path_publisher")
    rospy.loginfo("Path Publisher Started. Check out Paths in topics path1, path2, path3")
    rate = rospy.Rate(10)

    # start three publishers for paths
    path_pub1 = rospy.Publisher("/path1", Path, queue_size=10)
    path_pub2 = rospy.Publisher("/path2", Path, queue_size=10)
    path_pub3 = rospy.Publisher("/path3", Path, queue_size=10)

    path1 = return_path_message(PATH1)
    path2 = return_path_message(PATH2)
    path3 = return_path_message(PATH3)

    while not rospy.is_shutdown():
        path_pub1.publish(path1)
        path_pub2.publish(path2)
        path_pub3.publish(path3)

        rate.sleep()



