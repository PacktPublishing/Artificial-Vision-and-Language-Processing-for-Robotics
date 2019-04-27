#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class Observer:

	bridge = CvBridge()
	counter = 0

	def callback(self, data):
		if self.counter == 20:
			cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
			cv2.imshow('Image',cv_image)
			cv2.waitKey(1000)
			cv2.destroyAllWindows()
			self.counter = 0
		else:
			self.counter += 1

	def observe(self):
		laser_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.callback)
		rospy.init_node('observer', anonymous=True)
		rospy.spin()


if __name__ == '__main__':
	obs = Observer()
	obs.observe()