#!usr/bin/env python
import sys, os
sys.path.append(os.path.join(os.getcwd(),'python/'))
import darknet as dn

dn.set_gpu(0)
net = dn.load_net("cfg/yolov3.cfg", "yolov3.weights", 0)
meta = dn.load_meta("cfg/coco.data")


object_name_index = 0
dog_images = 0
number_of_images = 0

for file in os.listdir("dataset/"):

	filename = "dataset/" + file
	r = dn.detect(net, meta, filename)

	for obj in r:
		if obj[object_name_index] == "dog":
			dog_images += 1
			break
	number_of_images += 1


print("There are " + str(dog_images) + "/" + str(number_of_images) + " images containing dogs")