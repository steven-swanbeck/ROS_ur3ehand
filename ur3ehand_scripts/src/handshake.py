#!/usr/bin/env python

import sys
import rospy
import moveit_commander
import geometry_msgs
from std_msgs.msg import String

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('python_pickplace_jointspacecontroller', anonymous=True)
robot = moveit_commander.RobotCommander()

pub = rospy.Publisher('arduino', String, queue_size=10)
rate = rospy.Rate(100)
poweron_command = "z %s"
grasp_command = "g %s"
reset_command = "r %s"
poweroff_command = "x %s"

handshake_command = "h %s"
fist_command = "f %s"
pinkieout_command = "m %s"
pinkieclosed_command = "n %s"
snap_command = "s %s"
fingergun_command = "j %s"
peace_command = "p %s"
# rps_command = "k %s"
rps_command = "p %s"

# assuming start position
manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
manipulator_group.set_named_target("up")
plan1 = manipulator_group.go()

# turn to wave
joint_goal1 = manipulator_group.get_current_joint_values()
joint_goal1[0] = 0.5000457037320826
joint_goal1[1] = -1.5699301308502909
joint_goal1[2] = -3.84951266925782e-05
joint_goal1[3] = 9.69088695012033e-05
joint_goal1[4] = 1.5698764966321643
joint_goal1[5] = -0.7799225543141831
manipulator_group.go(joint_goal1, wait=True)
manipulator_group.stop()

# wave one direction
joint_goal1 = manipulator_group.get_current_joint_values()
joint_goal1[4] = 1.2
manipulator_group.go(joint_goal1, wait=True)
manipulator_group.stop()

# wave other direction
joint_goal1 = manipulator_group.get_current_joint_values()
joint_goal1[4] = 1.94
manipulator_group.go(joint_goal1, wait=True)
manipulator_group.stop()

# return to middle position
joint_goal1 = manipulator_group.get_current_joint_values()
joint_goal1[4] = 1.57
manipulator_group.go(joint_goal1, wait=True)
manipulator_group.stop()

# base handshake config
joint_goal2 = manipulator_group.get_current_joint_values()
joint_goal2[0] = 0.5000457037320826
joint_goal2[1] = -0.7850922423802317
joint_goal2[2] = 0.7849461150598712
joint_goal2[3] = 0.393
joint_goal2[4] = 1.5698764966321643
joint_goal2[5] = 1.2
# joint_goal4[5] = 0.7799225543141831
# joint_goal4[5] = 0
manipulator_group.go(joint_goal2, wait=True)
manipulator_group.stop()

# grasp hand
pub.publish(poweron_command)
rospy.sleep(0.2)
pub.publish(handshake_command)
rospy.sleep(2)
pub.publish(poweroff_command)

# shake down handshake config
joint_goal2 = manipulator_group.get_current_joint_values()
joint_goal2[2] = 0.9
joint_goal2[3] = 0.1
manipulator_group.go(joint_goal2, wait=True)
manipulator_group.stop()

# shake up handshake config
joint_goal2 = manipulator_group.get_current_joint_values()
joint_goal2[2] = 0.67
joint_goal2[3] = 0.686
manipulator_group.go(joint_goal2, wait=True)
manipulator_group.stop()

# repeat twice
joint_goal2 = manipulator_group.get_current_joint_values()
joint_goal2[2] = 0.9
joint_goal2[3] = 0.1
manipulator_group.go(joint_goal2, wait=True)
manipulator_group.stop()

# reassume middle configuration
joint_goal2 = manipulator_group.get_current_joint_values()
joint_goal2[0] = 0.5000457037320826
joint_goal2[1] = -0.7850922423802317
joint_goal2[2] = 0.7849461150598712
joint_goal2[3] = 0.393
joint_goal2[4] = 1.5698764966321643
joint_goal2[5] = 1.2
manipulator_group.go(joint_goal2, wait=True)
manipulator_group.stop()

# open hand
pub.publish(poweron_command)
rospy.sleep(0.2)
pub.publish(reset_command)
rospy.sleep(2)
pub.publish(poweroff_command)
# rospy.sleep(1)

# dap starting config
joint_goal3 = manipulator_group.get_current_joint_values()
joint_goal3[0] = 0.5000457037320826
joint_goal3[1] = -0.7850922423802317
joint_goal3[2] = 0.7849461150598712
joint_goal3[3] = 0.0
joint_goal3[4] = 1.5698764966321643
joint_goal3[5] = 0.7799225543141831
manipulator_group.go(joint_goal3, wait=True)
manipulator_group.stop()

# one side config
joint_goal3 = manipulator_group.get_current_joint_values()
joint_goal3[0] = 0.4
joint_goal3[1] = -0.7850922423802317
joint_goal3[2] = 0.7849461150598712
joint_goal3[3] = 0.0
joint_goal3[4] = 1.87
joint_goal3[5] = 0.7799225543141831
manipulator_group.go(joint_goal3, wait=True)
manipulator_group.stop()

# other side config
joint_goal3 = manipulator_group.get_current_joint_values()
joint_goal3[0] = 0.6
joint_goal3[4] = 1.27
manipulator_group.go(joint_goal3, wait=True)
manipulator_group.stop()

# return to center
pub.publish(poweron_command)
rospy.sleep(0.2)
pub.publish(fist_command)
joint_goal3 = manipulator_group.get_current_joint_values()
joint_goal3[0] = 0.5000457037320826
joint_goal3[1] = -0.7850922423802317
joint_goal3[2] = 0.7849461150598712
joint_goal3[3] = 0.0
joint_goal3[4] = 1.5698764966321643
joint_goal3[5] = 0.7799225543141831
manipulator_group.go(joint_goal3, wait=True)
manipulator_group.stop()
rospy.sleep(1)

# go down
pub.publish(poweroff_command)

joint_goal3 = manipulator_group.get_current_joint_values()
joint_goal3[2] = 1
joint_goal3[3] = 0.4
manipulator_group.go(joint_goal3, wait=True)
manipulator_group.stop()

# go back up
joint_goal3 = manipulator_group.get_current_joint_values()
joint_goal3[2] = 0.57
joint_goal3[3] = -0.4
manipulator_group.go(joint_goal3, wait=True)
manipulator_group.stop()

# return to center
joint_goal3 = manipulator_group.get_current_joint_values()
joint_goal3[0] = 0.5000457037320826
joint_goal3[1] = -0.7850922423802317
joint_goal3[2] = 0.7849461150598712
joint_goal3[3] = 0.0
joint_goal3[4] = 1.5698764966321643
joint_goal3[5] = 0.7799225543141831
manipulator_group.go(joint_goal3, wait=True)
manipulator_group.stop()

# challenge to rock, paper, scissors
pub.publish(poweron_command)
rospy.sleep(0.2)
pub.publish(reset_command)
rospy.sleep(2)
pub.publish(fist_command)
rospy.sleep(2)
pub.publish(reset_command)
rospy.sleep(2)
pub.publish(peace_command)
rospy.sleep(2)
pub.publish(fist_command)
rospy.sleep(2)
pub.publish(poweroff_command)
# rospy.sleep(1)

# rock, paper, scissors
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[0] = 0.5000457037320826
joint_goal4[1] = -0.7850922423802317
joint_goal4[2] = 0.5
joint_goal4[3] = 0.0
joint_goal4[4] = 1.5698764966321643
joint_goal4[5] = 0.7799225543141831
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()

# go back and forth three times
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[2] = 0.785
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[2] = 0.5
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[2] = 0.785
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[2] = 0.5
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[2] = 0.785
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[2] = 0.5
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()
joint_goal4 = manipulator_group.get_current_joint_values()
joint_goal4[2] = 0.785
pub.publish(poweron_command)
rospy.sleep(0.2)
pub.publish(rps_command)
manipulator_group.go(joint_goal4, wait=True)
manipulator_group.stop()

pub.publish(poweroff_command)
rospy.sleep(3)

# high-five
pub.publish(poweron_command)
rospy.sleep(0.2)
pub.publish(reset_command)

joint_goal8 = manipulator_group.get_current_joint_values()
joint_goal8[0] = 0.5000457037320826
joint_goal8[1] = -0.7850922423802317
joint_goal8[2] = 0.7849461150598712
joint_goal8[3] = 0.0
joint_goal8[4] = 1.5698764966321643
joint_goal8[5] = -0.7799225543141831
rospy.sleep(2)
pub.publish(poweroff_command)

joint_goal8[1] = -1.57
joint_goal8[2] = -0.785
manipulator_group.go(joint_goal8, wait=True)
manipulator_group.stop()
rospy.sleep(1)

joint_goal8 = manipulator_group.get_current_joint_values()
joint_goal8[1] = -0.785
joint_goal8[2] = 0
joint_goal8[3] = -0.785
manipulator_group.go(joint_goal8, wait=True)
manipulator_group.stop()
rospy.sleep(2)

# peace
joint_goal1 = manipulator_group.get_current_joint_values()
joint_goal1[0] = 0.5000457037320826
joint_goal1[1] = -1.5699301308502909
joint_goal1[2] = -3.84951266925782e-05
joint_goal1[3] = 9.69088695012033e-05
joint_goal1[4] = 1.5698764966321643
joint_goal1[5] = -0.7799225543141831
manipulator_group.go(joint_goal1, wait=True)
manipulator_group.stop()

pub.publish(poweron_command)
rospy.sleep(0.2)
pub.publish(peace_command)
rospy.sleep(3)

# reset hand
pub.publish(reset_command)

# reset to up config
manipulator_group.set_named_target("up")
plan1 = manipulator_group.go()
pub.publish(poweroff_command)

rospy.sleep(5)
moveit_commander.roscpp_shutdown()