#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def move():
	pub = rospy.Publisher('/mobile_base/commands/velocity', Twist, queue_size=1)
	rospy.init_node('movement', anonymous=True)
	move = Twist()
	move.angular.z = 0.5
	rate = rospy.Rate(10)
	while not rospy.is_shutdown():
		pub.publish(move)
		rate.sleep()


if __name__ == '__main__':
	try:
		move()
	except rospy.ROSInterruptException:
		pass