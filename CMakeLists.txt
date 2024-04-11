cmake_minimum_required(VERSION 3.5)
project(capra_thermal_cam)

# Default to C++14
if(NOT CMAKE_CXX_STANDARD)
  set(CMAKE_CXX_STANDARD 14)
endif()

# Find dependencies
find_package(ament_cmake REQUIRED)
find_package(usb_cam REQUIRED)
find_package(rclcpp REQUIRED)
find_package(sensor_msgs REQUIRED)

# Include directories
include_directories(include)

# Declare a C++ executable
add_executable(${PROJECT_NAME}_node src/capra_thermal_cam_node.cpp)

# Specify libraries to link a library or executable target against
ament_target_dependencies(${PROJECT_NAME}_node
  rclcpp
  sensor_msgs
  usb_cam
)

# Install targets
install(TARGETS
  ${PROJECT_NAME}_node
  DESTINATION lib/${PROJECT_NAME}
)

# Macro for ament package
ament_package()
