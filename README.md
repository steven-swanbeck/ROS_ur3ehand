# ROS Packages for Motion Planning and Execution for UR3e Manipulator with Custom Soft Gripper

## Acknowledgment
This repository was created for the Smart Robotics Lab at the University of Nevada, Reno.
It is the companion repository to [gripperROSIntegration](https://github.com/steven-swanbeck/gripperROSIntegration).
---

## Purpose
ROS packages to allow control of Universal Robots UR3e manipulator with University of Nevada, Reno Smart Robotics Lab's TSA-Driven Soft Robotic Hand. Packages can be used for motion planning and execution with the real robot or in simulation using Gazebo.
![20220429_142555](https://user-images.githubusercontent.com/99771915/180668626-87d21a32-0e39-43e8-98b6-ef3fa3bb8e55.jpg)

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

## Requirements, Dependencies, and Building
These packages are built and tested on a system running ROS noetic on Ubuntu 20.04.  
Use of these packages in a non-simulated environment requires the use of the official [Universal Robots ROS Drivers](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver). Slight modifications may be necessary to get these drivers to load the proper configuration files. Please contact the author at stevenswanbeck@nevada.unr.edu if help is needed to do this.  
1. Create a Catkin workspace:
```console
mkdir -p catkin_ur3ehand/src && cd catkin_ur3ehand
```
2. Clone the contents of this repository:
```console
git clone https://github.com/steven-swanbeck/ROS_ur3ehand.git
```
3. Clone the UR Robots ROS Driver:
```console
git clone https://github.com/UniversalRobots/Universal_Robots_ROS_Driver.git src/Universal_Robots_ROS_Driver
```
4. Install all package dependencies:
```console
rosdep install --from-paths src --ignore-src -r -y
```
5. Make the workspace:
```console
catkin_make
```
6. Source the workspace:
```console
source devel/setup.bash
```
---

## Commonly Used Commands
1. To launch a simple demo of the robot configured in RViz, use:
```console
roslaunch ur3ehand_moveit_config demo.launch
```
![Screenshot from 2022-07-24 15-14-10](https://user-images.githubusercontent.com/99771915/180668069-c6ace6f6-42e7-4eed-b04a-3cbc2879fd0d.png)
---
2. To expand the capabilites of this demo to Gazebo to simulate the robot, instead run:
```console
roslaunch ur3ehand_moveit_config demo_gazebo.launch
```
![Screenshot from 2022-07-24 15-24-07](https://user-images.githubusercontent.com/99771915/180668176-ad85acdd-48ab-4c7c-9318-9e49778525ff.png)
---
3. To run MoveIt with the real robot and drivers, the PC and robot must be configured as described in [Universal Robots ROS Drivers](https://github.com/UniversalRobots/Universal_Robots_ROS_Driver). Once this is done, start with:
```console
roslaunch ur_robot_driver ur3e_bringup.launch <robot_ip> <port> <kinematics_config>
```
ex:
```console
roslaunch ur_robot_driver ur3e_bringup.launch robot_ip:=192.168.0.2 [reverse_port:=REVERSE_PORT] kinematics_config:=$(rospack find  ur_calibration)/my_ur3_calibration.yaml
```
Then use:
```console
roslaunch ur3ehand_moveit_config ur3ehand_moveit_planning_execution.launch limited:=true
```
Followed by:
```console
roslaunch ur3ehand_moveit_config moveit_rviz.launch config:=true
```
**Note: The fixed frame may have to be defined and the robot model may need to be loaded in after this node has been launched. Scene objects should also be loaded in if necessary to prevent environment collisions.**
***
Once the RViz is launched through any of these methods, movement scripts can be passed to the robot in the form:
```console
rosrun ur3ehand_scripts <executable>
```
ex:
```console
rosrun ur3ehand_scripts test_pickplace2.py
```
Running in simulation and with real system:
***
[Screencast from 07-24-2022 03:28:46 PM.webm](https://user-images.githubusercontent.com/99771915/180668403-3f5fb114-27e2-4fbe-a7f3-14e8b3f1ee51.webm) 
***
https://user-images.githubusercontent.com/99771915/180924977-beed9b2a-423b-4f19-8d4b-48126be9a99b.mp4
***
https://user-images.githubusercontent.com/99771915/182464740-69e11d78-788f-4822-9b3e-c8cb71fe61d9.mp4
***

## Arduino Integration with Soft Gripper
For full details of the ROS integration of the Arduino-based gripper with these packages, view this repository's [companion repository](https://github.com/steven-swanbeck/gripperROSIntegration).
***
## Helpful Links
https://ros-planning.github.io/moveit_tutorials/doc/getting_started/getting_started.html  
https://moveit.readthedocs.io/en/latest/doc/pr2_tutorials/planning/src/doc/move_group_interface_tutorial.html#moving-to-a-pose-goal  
<!--https://support.squarespace.com/hc/en-us/articles/206543587-Markdown-cheat-sheet-->
