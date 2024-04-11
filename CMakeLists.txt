cmake_minimum_required(VERSION 3.5)
project(capra_thermal_cam)

if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)  # If you use sensor messages
find_package(usb_cam REQUIRED)  # If you use sensor messages
# Include ROS 2 equivalent of usb_cam if available

ament_package()
