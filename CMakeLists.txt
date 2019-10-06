cmake_minimum_required(VERSION 2.8.3)
project(riptide_robothoughts)

## Compile as C++11, supported in ROS Kinetic and newer
add_compile_options(-std=c++11)

## Find catkin macros and libraries
## if COMPONENTS list like find_package(catkin REQUIRED COMPONENTS xyz)
## is used, also find other catkin packages
find_package(catkin REQUIRED COMPONENTS
  roscpp
  roslint
  rospy
  riptide_msgs
  geometry_msgs
  sensor_msgs
  actionlib_msgs
  darknet_ros_msgs
)

catkin_package(
  CATKIN_DEPENDS
    actionlib_msgs)
