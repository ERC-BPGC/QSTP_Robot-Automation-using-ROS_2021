#!/usr/bin/env python
import rospy
from nav_msgs.msg import Odometry
from geometry_msgs.msg import PoseStamped, Pose, Quaternion, Point
from std_msgs.msg import Header, Bool

import numpy as np

class Thief:
    def __init__(self):
        
        self.pose_pub = rospy.Publisher("/thief_pose", PoseStamped, queue_size=10)
        self.odom_pub = rospy.Subscriber("/odom", Odometry, self.__odom_callback)

        self.pose_change_timer = rospy.Timer(rospy.Duration(60), self.__teleport)

        self.recent_position = Point(0, 0, 0)
        self.count = 0

        self.x_new = 0
        self.y_new = 0

    def __odom_callback(self, msg):
        self.recent_position = msg.pose.pose.position
        # Publish the pose now
        pose = PoseStamped()
        pose.header = Header(frame_id="odom", stamp=rospy.Time.now())
        pose.pose.position = Point(self.x_new, self.y_new, 0)
        pose.pose.orientation = Quaternion(0, 0, 0, 1)

        self.pose_pub.publish(pose)

    def __teleport(self, timer):
        # This method publishes the a new pose every one minute
        # The new pose generated is generally on a circle with radius 5 to 7 meters away from the turtlebot centered at the robots current pose

        if self.count < 5:
            # publish the new pose only five times
            x, y = self.recent_position.x, self.recent_position.y
            
            theta = np.random.uniform(0, 2*np.pi)
            r = np.random.uniform(5, 7)

            self.x_new = x + r * np.cos(theta)
            self.y_new = y + r * np.sin(theta)

            rospy.loginfo("HaHa, I changed my place now!!")
            self.count = self.count + 1

    

if __name__ == "__main__":
    rospy.init_node("thief_node")

    thief = Thief()

    rospy.loginfo("Catch the Thief")
    
    rospy.spin()



        
