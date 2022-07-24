import sys
import rospy
import moveit_commander
import geometry_msgs

moveit_commander.roscpp_initialize(sys.argv)
rospy.init_node('move_group_python_interface_tutorial', anonymous=True)
robot = moveit_commander.RobotCommander()

scene = moveit_commander.PlanningSceneInterface()
box_pose = geometry_msgs.msg.PoseStamped()
box_pose.header.frame_id = "world"
box_pose.pose.orientation.w = 1.0
box_pose.pose.position.z = -0.25
box_name = "box"
scene.add_box(box_name, box_pose, size=(2.0, 2.0, 0.5))

# assuming start position
manipulator_group = moveit_commander.MoveGroupCommander("manipulator")
manipulator_group.set_named_target("pick")
plan1 = manipulator_group.go()

pose_target = geometry_msgs.msg.Pose()
pose_target.orientation.w = 0.5
pose_target.orientation.x = 0.5
pose_target.orientation.y = -0.5
pose_target.orientation.z = 0.5
pose_target.position.x = -0.42273
pose_target.position.y = 0.18643
pose_target.position.z = 0.09787
manipulator_group.set_pose_target(pose_target)
plan1 = manipulator_group.go()

pose_target.position.x = -0.5
manipulator_group.set_pose_target(pose_target)
plan1 = manipulator_group.go()

pose_target.position.z = 0.3
manipulator_group.set_pose_target(pose_target)
plan1 = manipulator_group.go()


rospy.sleep(5)
moveit_commander.roscpp_shutdown()

# def wait_for_state_update(self, box_is_known=False, box_is_attached=False, timeout=4):
#         start = rospy.get_time()
#         seconds = rospy.get_time()
#         while (seconds - start < timeout) and not rospy.is_shutdown():
#             # Test if the box is in attached objects
#             attached_objects = scene.get_attached_objects([box_name])
#             is_attached = len(attached_objects.keys()) > 0

#             # Test if the box is in the scene.
#             # Note that attaching the box will remove it from known_objects
#             is_known = box_name in scene.get_known_object_names()

#             # Test if we are in the expected state
#             if (box_is_attached == is_attached) and (box_is_known == is_known):
#                 return True

#             # Sleep so that we give other threads time on the processor
#             rospy.sleep(0.1)
#             seconds = rospy.get_time()

#         # If we exited the while loop without returning then we timed out
#         return False