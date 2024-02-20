#!/usr/bin/env python3
from tkinter import*
import rospy
from geometry_msgs.msg import Twist
from std_msgs.msg import String


# Parameter for Defult Scale
#
#
#text = rospy.get_param("/REMOTE/text")



frame = Tk()
frame.title("REMOTE")
frame.geometry("300x300")



# Initial ROS node and determine Publish or Subscribe action
#
#
#
if __name__ == "__main__":
    pub = rospy.Publisher("turtle1/cmd_vel",Twist,queue_size=10)  
    pub1 = rospy.Publisher("chatter",String,queue_size=10)
    rospy.init_node("REMOTE")
	


def fw():
    print("Forward")
    cmd = Twist()
    cmd.linear.x = 1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
def bw():
    print("Backward")
    cmd = Twist()
    cmd.linear.x = -1.0
    cmd.angular.z=0.0
    pub.publish(cmd)
def lt():
    print("Turn Left")
    cmd = Twist()
    cmd.linear.y = 0.0
    cmd.angular.z= 1.0

    pub.publish(cmd)
def rt():
    print("Turn Right")
    cmd = Twist()
    cmd.linear.y = 0.0
    cmd.angular.z= -1.0
    pub.publish(cmd)

def onp():
    print("PenOn")

def offp():
    print("PenOff")
    



#LinearVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
#LinearVel.set(1) # 1 is defult value for scale
#LinearVel.pack()

#AngularVel = Scale(frame, from_=0, to=2, orient=HORIZONTAL)
#AngularVel.set(1) # 1 is defult value for scale
#AngularVel.pack()



B1 = Button(text = "Forward", command=fw)
B1.place(x=73, y=50)

B2 = Button(text = "Backward", command=bw)
B2.place(x=73, y=150)

B3 = Button(text = "Turn Left", command=lt)
B3.place(x=20, y=100)

B4 = Button(text = "Turn Right", command=rt)
B4.place(x=128, y=100)

B4 = Button(text = "PenOn", command=onp)
B4.place(x=20,y=220)

B4 = Button(text = "PenOff", command=offp)
B4.place(x=128, y=220)

frame.mainloop()    