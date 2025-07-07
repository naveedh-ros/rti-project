# Robot Talent Initiative (RTI) Setup Guide

This document will guide you through installing and configuring all necessary dependencies, cloning the Robot Talent Initiative (RTI) repository, building the workspace, and running the RTI project — on Ubuntu 22.04 with ROS 2 Humble.

---

## Prerequisites

- **Operating System**: Ubuntu 22.04 LTS
- **Git**: To clone the repository


1. Run `sudo apt install ros-humble-desktop` Follow this [link](https://docs.ros.org/en/humble/Installation/Ubuntu-Install-Debs.html) for more information and make sure you source ROS2. (Best if you add the setup file to .bashrc, if not make sure to source the ROS2 setup.bash everytime you open a new terminal)

2. Run `git clone --recursive https://github.com/naveedh-ros/rti-project/` to clone the project repository

3. Run `cd rti-project`

4. Run `bash docs/gazebo.sh` to install Gazebo 11

5. Run `sudo apt install ros-humble-gazebo-ros2-control` for gazebo_ros packages

6. Use `colcon build --symlink-install` to build all packages in this project

7. After you build, ensure you are sourcing the packages in this project by running `source ros2_ws/install/setup.bash` (You can also add this to .bashrc, or source everytime you open a new terminal)

8. Follow instructions in each package to run them.
