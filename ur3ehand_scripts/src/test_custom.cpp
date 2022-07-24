#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit/move_group_interface/move_group_interface.h>
#include <moveit_msgs/DisplayRobotState.h>
#include <moveit_msgs/DisplayTrajectory.h>
#include <moveit_msgs/AttachedCollisionObject.h>
#include <moveit_msgs/CollisionObject.h>

int main(int argc, char **argv)
{
  ros::init(argc, argv, "move_group_interface_tutorial");
  ros::NodeHandle node_handle;  
  ros::AsyncSpinner spinner(1);
  spinner.start();

  /* This sleep is ONLY to allow Rviz to come up */
  sleep(2.0);
  
  // The :move_group_interface:`MoveGroup` class can be easily 
  // setup using just the name
  // of the group you would like to control and plan for.
  moveit::planning_interface::MoveGroupInterface group("manipulator");

  // We will use the :planning_scene_interface:`PlanningSceneInterface`
  // class to deal directly with the world.
  moveit::planning_interface::PlanningSceneInterface planning_scene_interface;  

  // (Optional) Create a publisher for visualizing plans in Rviz.
  ros::Publisher display_publisher = node_handle.advertise<moveit_msgs::DisplayTrajectory>("/move_group/display_planned_path", 1, true);
  moveit_msgs::DisplayTrajectory display_trajectory;

  // Getting Basic Information
  // ^^^^^^^^^^^^^^^^^^^^^^^^^
  //	
  // We can print the name of the reference frame for this robot.
  ROS_INFO("Reference frame: %s", group.getPlanningFrame().c_str());
  
  // We can also print the name of the end-effector link for this group.
  ROS_INFO("Reference frame: %s", group.getEndEffectorLink().c_str());

  // Planning to a Pose goal
  // ^^^^^^^^^^^^^^^^^^^^^^^
  // We can plan a motion for this group to a desired pose for the 
  // end-effector.
  geometry_msgs::Pose target_pose1;
  target_pose1.orientation.w = 0.46464582895130785;
  target_pose1.orientation.x = 0.5329403552989955;
  target_pose1.orientation.y = -0.5334136949145868;
  target_pose1.orientation.z = 0.46427218461749403;

  target_pose1.position.x = -0.22281733126293418;
  target_pose1.position.y = 0.3864684395327212;
  target_pose1.position.z = 0.0878207898712599;
  group.setPoseTarget(target_pose1);


  // Now, we call the planner to compute the plan
  // and visualize it.
  // Note that we are just planning, not asking move_group 
  // to actually move the robot.
	moveit::planning_interface::MoveGroupInterface::Plan my_plan;
	moveit::planning_interface::MoveItErrorCode success = group.plan(my_plan); 
  ROS_INFO("Visualizing plan 1 (pose goal) %s",success.val ? "":"FAILED");    

  // Sleep to give Rviz time to visualize the plan. 
	group.move();	
	// END_TUTORIAL

  ros::shutdown();  

 return 0;
}
