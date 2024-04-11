cmake_minimum_required(VERSION 3.5)
project(capra_thermal_cam)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find ROS 2 dependencies
find_package(ament_cmake REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)
# If usb_cam has a ROS 2 version, include it here, otherwise, you'll need to port it or find an alternative
# find_package(usb_cam REQUIRED)

# Include directories
include_directories(include)

# Declare a C++ executable
add_executable(${PROJECT_NAME}_node src/capra_thermal_cam_node.cpp)

# Specify libraries to link a library or executable target against
ament_target_dependencies(${PROJECT_NAME}_node
  rclcpp
  sensor_msgs
  # usb_cam, if available for ROS 2
)

# Install the executable
install(TARGETS
  ${PROJECT_NAME}_node
  DESTINATION lib/${PROJECT_NAME}
)

ament_package()
