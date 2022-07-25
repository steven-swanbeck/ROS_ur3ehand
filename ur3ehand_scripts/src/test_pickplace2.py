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
# rospy.init_node('talker', anonymous=True)
rate = rospy.Rate(100)
poweron_command = "z %s"
grasp_command = "g %s"
reset_command = "r %s"
poweroff_command = "x %s"

# scene = moveit_commander.PlanningSceneInterface()
# box_pose = geometry_msgs.msg.PoseStamped()
# box_pose.header.frame_id = "world"
# box_pose.pose.orientation.w = 1.0
# box_pose.pose.position.z = -0.25
# box_name = "box"
# scene.add_box(box_name, box_pose, size=(2.0, 2.0, 0.5))

# assuming start position
manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
manipulator_group.set_named_target("up")
plan1 = manipulator_group.go()

manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
manipulator_group.set_named_target("pick")
plan1 = manipulator_group.go()

joint_goal = manipulator_group.get_current_joint_values()
joint_goal[0] = 2.2023980034384634
joint_goal[1] = -0.9120257774970887
joint_goal[2] = 1.7928126293556301
joint_goal[3] = -0.8807893124936923
joint_goal[4] = 0.6325328321346937
joint_goal[5] = 0.785398
# joint_goal[5] = -0.0001313144910217047
manipulator_group.go(joint_goal, wait=True)
manipulator_group.stop()

pub.publish(poweron_command)
rospy.sleep(1)

joint_goal = manipulator_group.get_current_joint_values()
joint_goal[0] = 2.532851104178941
joint_goal[1] = -0.1217214011730563
joint_goal[2] = 0.1286146930351096
joint_goal[3] = -0.0068683874986455095
joint_goal[4] = 0.9630710945579968
joint_goal[5] = 0.785398
# joint_goal[5] = -5.2414672313052374e-05
manipulator_group.go(joint_goal, wait=True)
manipulator_group.stop()

# Puiblish the grasp message to the arduino topic
pub.publish(grasp_command)
rospy.sleep(3)

joint_goal = manipulator_group.get_current_joint_values()
joint_goal[0] = 2.532851104178941
joint_goal[1] = -0.4363323125
joint_goal[2] = 0.1286146930351096
joint_goal[3] = -0.0068683874986455095
joint_goal[4] = 0.9630710945579968
joint_goal[5] = 0.785398
# joint_goal[5] = -5.2414672313052374e-05
manipulator_group.go(joint_goal, wait=True)
manipulator_group.stop()

joint_goal = manipulator_group.get_current_joint_values()
joint_goal[0] = 3.5648646705055835
joint_goal[1] = -0.8688864461762213
joint_goal[2] = 0.6075403037006841
joint_goal[3] = 0.2603143573852755
joint_goal[4] = 1.0638734942376717
joint_goal[5] = 0.749343
# joint_goal[5] = -0.036054985257424975
manipulator_group.go(joint_goal, wait=True)
manipulator_group.stop()

joint_goal = manipulator_group.get_current_joint_values()
joint_goal[0] = 3.545752726111179
joint_goal[1] = -0.6462491491559118
joint_goal[2] = 1.2908826905166841
joint_goal[3] = -0.6455245065997017
joint_goal[4] = 1.0445855221928007
joint_goal[5] = 0.749343
# joint_goal[5] = -0.03594657134456268
manipulator_group.go(joint_goal, wait=True)
manipulator_group.stop()

pub.publish(reset_command)
rospy.sleep(3)

joint_goal = manipulator_group.get_current_joint_values()
joint_goal[0] = 2.9608131806195233
joint_goal[1] = -1.1833748842942986
joint_goal[2] = 2.513991797608773
joint_goal[3] = -1.3327621076986882
joint_goal[4] = 0.4595316744097665
joint_goal[5] = 0.749343
# joint_goal[5] = -0.03459987525798038
manipulator_group.go(joint_goal, wait=True)
manipulator_group.stop()

pub.publish(poweroff_command)
rospy.sleep(1)

manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
manipulator_group.set_named_target("pick")
plan1 = manipulator_group.go()

manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
manipulator_group.set_named_target("up")
plan1 = manipulator_group.go()

# pose_target = geometry_msgs.msg.Pose()
# pose_target.orientation.w = 0.5
# pose_target.orientation.x = 0.5
# pose_target.orientation.y = -0.5
# pose_target.orientation.z = 0.5
# pose_target.position.x = -0.42273
# pose_target.position.y = 0.18643
# pose_target.position.z = 0.09787
# manipulator_group.set_pose_target(pose_target)
# plan1 = manipulator_group.go()

# pose_target.position.x = -0.5
# manipulator_group.set_pose_target(pose_target)
# plan1 = manipulator_group.go()

# pose_target.position.z = 0.3
# manipulator_group.set_pose_target(pose_target)
# plan1 = manipulator_group.go()

rospy.sleep(5)
moveit_commander.roscpp_shutdown()
