

import rospy
from std_msgs.msg import String

def mentee():
    rospy.init_node('mentee', anonymous = true)
    rospy.Subscriber('Answer', String, callback)
    rospy.spin()
   
def callback(data):
    rospy.loginfo('No,I''am so hungry')

if __name__ == '__main__':
    mentee()
