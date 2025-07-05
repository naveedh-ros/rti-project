cmake_minimum_required(VERSION 3.8)
project(multibot_interfaces)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(std_msgs REQUIRED)
find_package(nav2_msgs REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(rclpy REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/RobotGoal.msg"
  "srv/GetRobotPose.srv"
  "srv/Task.srv"
  DEPENDENCIES geometry_msgs std_msgs
)

install(DIRECTORY
  msg
  srv
  DESTINATION share/${PROJECT_NAME}/
)

ament_package()

