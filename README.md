# ROS Packages for Motion Planning and Execution for UR3e Manipulator with Custom Soft Gripper

## Purpose
ROS packages to allow control of Universal Robots UR3e manipulator with University of Nevada, Reno Smart Robotics Lab's TSA-Driven Soft Robotic Hand. Packages can be used for motion planning and execution with the real robot or in simulation using Gazebo.

## Contents
* ur3ehand_description
* ur3ehand_moveit_config
* ur3ehand_scripts

## ur3ehand_description
The ur3ehand_description package contains files used to construct and load virtual models of the UR3e with the attached end-effector to be used for simulation, visualization, and motion-planning. The ur3e_with_hand.urdf model can be altered to change the collision and visual geometry of the end-effector and adjust joint limits to fit the user's needs.

## ur3ehand_moveit_config
The ur3ehand_moveit_config package provides 
