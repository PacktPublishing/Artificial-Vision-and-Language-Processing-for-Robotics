#!/usr/bin/env python
import rospy
from std_msgs.msg import Int32

class Finder:

    searched_number = 150
    generated_numbers = 0

    def callback(self, data):
        if data.data == self.searched_number:
            print(str(data.data) + ": YES")
            self.generated_numbers += 1
            print("The searched number has been found after " + str(self.generated_numbers) + " tries")
            rospy.signal_shutdown("Number found")
        elif self.generated_numbers >= 1000:
            print("It wasn't possible to find the searched number")
            rospy.signal_shutdown("Number not found")
        else:
            print(str(data.data) + ": NO")
            self.generated_numbers += 1


    def finder(self):
        rospy.init_node('finder', anonymous=True)
        rospy.Subscriber('numbers_topic', Int32, self.callback)
        rospy.spin()


if __name__ == '__main__':
    find = Finder()
    find.finder()