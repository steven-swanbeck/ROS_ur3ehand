#include <ros/ros.h>
#include <moveit/planning_scene_interface/planning_scene_interface.h>
#include <moveit/move_group_interface/move_group_interface.h>
#include <tf2_geometry_msgs/tf2_geometry_msgs.h>

const double tau = 2 * M_PI;

void openGripper() {}
void closeGripper() {}

//void initPose(moveit::planning_interface::MoveGroupInterface& move_group)
//{
  

void pick(moveit::planning_interface::MoveGroupInterface& move_group) {
    std::vector<moveit_msgs::Grasp> grasps;
    grasps.resize(1);

    grasps[0].grasp_pose.header.frame_id = "world";
    tf2::Quaternion orientation;
    grasps[0].grasp_pose.pose.orientation.w = 0.5;
    grasps[0].grasp_pose.pose.orientation.x = 0.5;
    grasps[0].grasp_pose.pose.orientation.y = -0.5;
    grasps[0].grasp_pose.pose.orientation.z = 0.5;
    grasps[0].grasp_pose.pose.position.x = -0.42273;
    grasps[0].grasp_pose.pose.position.y = 0.18643;
    grasps[0].grasp_pose.pose.position.z = 0.09787;

    // Pre-grasp approach
    grasps[0].pre_grasp_approach.direction.header.frame_id = "world";
    grasps[0].pre_grasp_approach.direction.vector.x = -1.0;
    grasps[0].pre_grasp_approach.min_distance = 0.095;
    grasps[0].pre_grasp_approach.desired_distance = 0.115;

    // Post-grasp retreat
    grasps[0].post_grasp_retreat.direction.header.frame_id = "world";
    grasps[0].post_grasp_retreat.direction.vector.z = 1.0;
    grasps[0].post_grasp_retreat.min_distance = 0.1;
    grasps[0].post_grasp_retreat.desired_distance = 0.25;

    // Opening Gripper
    openGripper();

    // Closing Gripper
    closeGripper(); 

    // Set suport surface as table
    move_group.setSupportSurfaceName("table1");

    // Call to pick up object
    move_group.pick("object", grasps);
}

void place(moveit::planning_interface::MoveGroupInterface& group) {
    std::vector<moveit_msgs::PlaceLocation> place_location;
    place_location.resize(1);

    place_location[0].place_pose.header.frame_id = "world";
    tf2::Quaternion orientation;
    orientation.setRPY(0, 0, tau / 4);  // A quarter turn about the z-axis
    place_location[0].place_pose.pose.orientation = tf2::toMsg(orientation);
    place_location[0].place_pose.pose.position.x = 0.05843;
    place_location[0].place_pose.pose.position.y = -0.28461;
    place_location[0].place_pose.pose.position.z = 0.14755;

    // Pre-place approach
    place_location[0].post_place_retreat.direction.header.frame_id = "world";
    place_location[0].pre_place_approach.direction.vector.z = -1.0;
    place_location[0].pre_place_approach.min_distance = 0.095;
    place_location[0].pre_place_approach.desired_distance = 0.115;

    //Post-grasp retreat
    place_location[0].post_place_retreat.direction.header.frame_id = "world";
    place_location[0].post_place_retreat.direction.vector.y = -1.0;
    place_location[0].post_place_retreat.min_distance = 0.1;
    place_location[0].post_place_retreat.desired_distance = 0.25;

    openGripper();
    
    group.setSupportSurfaceName("table1");
    group.place("object", place_location);
}

void addCollisionObjects(moveit::planning_interface::PlanningSceneInterface& planning_scene_interface) {
    std::vector<moveit_msgs::CollisionObject> collision_objects;
    collision_objects.resize(2);

    collision_objects[0].id = "table1";
    collision_objects[0].header.frame_id = "world";

    collision_objects[0].primitives.resize(1);
    collision_objects[0].primitives[0].type = collision_objects[0].primitives[0].BOX;
    collision_objects[0].primitives[0].dimensions.resize(3);
    collision_objects[0].primitives[0].dimensions[0] = 2.0;
    collision_objects[0].primitives[0].dimensions[1] = 2.0;
    collision_objects[0].primitives[0].dimensions[2] = 0.5;

    collision_objects[0].primitive_poses.resize(1);
    collision_objects[0].primitive_poses[0].position.x = 0;
    collision_objects[0].primitive_poses[0].position.y = 0;
    collision_objects[0].primitive_poses[0].position.z = -0.25;
    collision_objects[0].primitive_poses[0].orientation.w = 1.0;

    collision_objects[0].operation = collision_objects[0].ADD;

    // Object to pp
    collision_objects[1].header.frame_id = "world";
    collision_objects[1].id = "object"; 

    collision_objects[1].primitives.resize(1);
    collision_objects[1].primitives[0].type = collision_objects[1].primitives[0].BOX;
    collision_objects[1].primitives[0].dimensions.resize(3);
    collision_objects[1].primitives[0].dimensions[0] = 0.02;
    collision_objects[1].primitives[0].dimensions[1] = 0.02;
    collision_objects[1].primitives[0].dimensions[2] = 0.2;

    collision_objects[1].primitive_poses.resize(1);
    collision_objects[1].primitive_poses[0].position.x = -0.7;
    collision_objects[1].primitive_poses[0].position.y = 0.35;
    collision_objects[1].primitive_poses[0].position.z = 0.1;
    collision_objects[1].primitive_poses[0].orientation.w = 1.0;

    collision_objects[1].operation = collision_objects[1].ADD;

    planning_scene_interface.applyCollisionObjects(collision_objects);
}

int main(int argc, char** argv) {
    ros::init(argc, argv, "test_pickplace");
    ros::NodeHandle nh;
    ros::AsyncSpinner spinner(1);
    spinner.start();

    ros::WallDuration(1.0).sleep();
    moveit::planning_interface::PlanningSceneInterface planning_scene_interface;
    moveit::planning_interface::MoveGroupInterface group("manipulator");
    group.setPlanningTime(45.0);

    addCollisionObjects(planning_scene_interface);

    ros::WallDuration(1.0).sleep();

    pick(group);

    ros::WallDuration(1.0).sleep();

    place(group);

    ros::waitForShutdown();
    return 0;
}