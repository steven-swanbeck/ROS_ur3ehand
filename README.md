# ROS Packages for Motion Planning and Execution for UR3e Manipulator with Custom Soft Gripper

## Acknowledgment
This repository was created for the Smart Robotics Lab at the University of Nevada, Reno.
It is the companion repository to https://github.com/steven-swanbeck/gripperROSIntegration.
---

## Purpose
ROS packages to allow control of Universal Robots UR3e manipulator with University of Nevada, Reno Smart Robotics Lab's TSA-Driven Soft Robotic Hand. Packages can be used for motion planning and execution with the real robot or in simulation using Gazebo.

## Contents
1. **ur3ehand_description**
    * The ur3ehand_description package contains files used to construct and load virtual models of the UR3e with the attached end-effector to be used for simulation, visualization, and motion-planning.
    * The ur3e_with_hand.urdf model can be altered to change the collision and visual geometry of the end-effector and adjust joint limits to fit the user's needs.
---
2. **ur3ehand_moveit_config**
    * The ur3ehand_moveit_config package provides tools for motion planning and simulated execution for the combined UR3e-end-effector system. 
---
3. **ur3ehand_scripts**
    * The ur3ehand_scripts package contains Python and C++ scripts used for controlling the gripper and manipulator.
    * Many of them are meant to serve as examples, showing how one *could* program specific joint-space or Cartesian goals to the system and execute them. **They do not necessarily reflect the optimal method of performing these actions.**
    * Some of the scripts include examples of how to publish to the arduino topic to interface with this repository's [companion repository](https://github.com/steven-swanbeck/gripperROSIntegration).
---

## Requirements and Building
These packages are built and tested on a system running ROS noetic on Ubuntu 20.04.  
Building

## Dependencies/Further Setup
Use of these packages in a non-simulated environment requires the use of the official [Universal Robots ROS Drivers](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver). Slight modifications may be necessary to get these drivers to load the proper configuration files. Please contact the author at stevenswanbeck@nevada.unr.edu if help is needed to do this.

## Arduino Integration with Soft Gripper
For full details of the ROS integration of the Arduino-based gripper with these packages, view this repository's [companion repository](https://github.com/steven-swanbeck/ur3ehand).
