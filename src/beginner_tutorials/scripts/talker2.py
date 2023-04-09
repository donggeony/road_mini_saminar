import rospy
from std_msgs.msg import String

def mentor():
    pub = rospy.Publisher('food',String, 10)
    rospy.init_node('mentor', anoymous=True)
    rate = rospy.Rate(10)
    while not rospy.is_shutdown():
    	Question ='Did you eat lunch?'
    	rospy.loginfo(Question)
    	pub.publish(Question)
    	rate.sleep()
    	

if __name__ == '__main__':
    try:
        mentor()
    except rospy.ROSInterruptException:
        pass
