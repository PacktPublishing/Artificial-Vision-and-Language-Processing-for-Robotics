#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def callback(data):
    if(data != None):
        print("Message received")
        rospy.signal_shutdown("Message received")

def subscriber():
    rospy.init_node('subscriber', anonymous=True)
    rospy.Subscriber('publisher_topic', String, callback)
    rospy.spin()
    

if __name__ == '__main__':
    subscriber()
