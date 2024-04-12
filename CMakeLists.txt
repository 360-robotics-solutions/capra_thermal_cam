cmake_minimum_required(VERSION 3.5)
project(capra_thermal_cam)

# Uncomment to set C++ standard explicitly
# add_compile_options(-std=c++14)

# Find required packages
find_package(ament_cmake REQUIRED)
find_package(usb_cam REQUIRED)

# Uncomment this if the package has a setup.py. This macro ensures
# modules and global scripts declared therein get installed
# ament_python_install_package()

# catkin_package is replaced by ament_package in ROS 2
ament_package()

# Include directories
include_directories(
  include
  ${usb_cam_INCLUDE_DIRS}
)

# Linking against libraries is managed differently in ROS 2
# Here is an example of declaring a library in ROS 2
# add_library(${PROJECT_NAME}_lib
#   src/${PROJECT_NAME}/example.cpp
# )
# ament_target_dependencies(${PROJECT_NAME}_lib
#   usb_cam
# )

# Executable names should be unique across packages
# add_executable(${PROJECT_NAME}_node src/example_node.cpp)

# Setup target dependencies of executables
# add_dependencies(${PROJECT_NAME}_node ${${PROJECT_NAME}_EXPORTED_TARGETS} ${usb_cam_EXPORTED_TARGETS})

# Specify libraries to link executable against
# target_link_libraries(${PROJECT_NAME}_node
#   ${PROJECT_NAME}_lib
#   ${usb_cam_LIBRARIES}
# )

# Installation of executables and libraries
# install(TARGETS ${PROJECT_NAME}_node ${PROJECT_NAME}_lib
#   DESTINATION lib/${PROJECT_NAME}
# )

# Install launch files, configs, and other resources
# install(DIRECTORY launch config
#   DESTINATION share/${PROJECT_NAME}
# )

