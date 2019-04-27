#!/usr/bin/env python
import rospy
from std_msgs.msg import String

def publisher():
    pub = rospy.Publisher('publisher_topic', String, queue_size=1)
    rospy.init_node('publisher', anonymous=True)
    pub.publish("Sending message")

if __name__ == "__main__":
    publisher()