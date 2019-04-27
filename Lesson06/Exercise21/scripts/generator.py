#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32
import random

def generate():
    pub = rospy.Publisher('numbers_topic', Int32, queue_size=10)
    rospy.init_node('generator', anonymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
        num = random.randint(1,101)
        pub.publish(num)
        rate.sleep()

if __name__ == '__main__':
    try:
        generate()
    except rospy.ROSInterruptException:
        pass
