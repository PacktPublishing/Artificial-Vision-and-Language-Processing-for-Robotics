#!/usr/bin/env python
import rospy
from sensor_msgs.msg import Image
import cv2
from cv_bridge import CvBridge

class ObtainImage:

	bridge = CvBridge()

	def callback(self, data):
		cv_image = self.bridge.imgmsg_to_cv2(data, "bgr8")
		cv2.imshow('Image',cv_image)
		cv2.waitKey(0)
		rospy.signal_shutdown("Finishing")

	def obtain(self):
		laser_sub = rospy.Subscriber('/camera/rgb/image_raw', Image, self.callback)
		rospy.init_node('image_obtainer', anonymous=True)
		rospy.spin()


if __name__ == '__main__':
	obt = ObtainImage()
	obt.obtain()