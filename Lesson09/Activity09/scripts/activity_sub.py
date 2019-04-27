#!/usr/bin/env python
import rospy
from std_msgs.msg import String


class ActivitySub():

	yolo_data = ""
	
	def __init__(self):
		rospy.init_node('ThiefDetector', anonymous=True)
		rospy.Subscriber("yolo_topic", String, self.callback)

	
	def callback(self, data):
		self.yolo_data = data

	def run(self):

		while True:
			if "person" in str(self.yolo_data):
				print("ALERT: THIEF DETECTED")
				break


if __name__ == '__main__':
	node = ActivitySub()
	try:
		node.run()
	except rospy.ROSInterruptException:
		pass