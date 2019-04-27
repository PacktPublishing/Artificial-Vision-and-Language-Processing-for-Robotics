#!/usr/bin/env python
import rospy
import cv2
import sys
import os
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image
from std_msgs.msg import String

sys.path.append(os.path.join(os.getcwd(), '/home/alvaro/Escritorio/tfg/darknet/python/'))

import darknet as dn



class Activity():

	def __init__(self):
		rospy.init_node('Activity', anonymous=True)
		self.bridge = CvBridge()
		self.image_sub = rospy.Subscriber("camera/rgb/image_raw", Image, self.imageCallback)
		self.pub = rospy.Publisher('yolo_topic', String, queue_size=10)
		self.imageToProcess = None
		cfgPath =  "/home/alvaro/Escritorio/tfg/darknet/cfg/yolov3.cfg"
		weightsPath = "/home/alvaro/Escritorio/tfg/darknet/yolov3.weights"
		dataPath = "/home/alvaro/Escritorio/tfg/darknet/cfg/coco2.data"
		self.net = dn.load_net(cfgPath, weightsPath, 0)
		self.meta = dn.load_meta(dataPath)
		self.fileName = 'predict.jpg'
		self.rate = rospy.Rate(10)


	def imageCallback(self, data):
		self.imageToProcess = self.bridge.imgmsg_to_cv2(data, "bgr8")


	def run(self):

		print("The robot is recognizing objects")

		while not rospy.core.is_shutdown():

			if(self.imageToProcess is not None):
				cv2.imwrite(self.fileName, self.imageToProcess)
				r = dn.detect(self.net, self.meta, self.fileName)

				objects = ""

				for obj in r:
					objects += obj[0] + " "

				self.pub.publish(objects)
				self.rate.sleep()






if __name__ == '__main__':
	# Set Darknet params
	dn.set_gpu(0)
	node = Activity()
	try:
		node.run()
	except rospy.ROSInterruptException:
		pass