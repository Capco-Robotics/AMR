cmake_minimum_required(VERSION 3.8)
project(amr_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/EncoderTicks.msg"
  "msg/WheelSetpoints.msg"
  "msg/LiftCommand.msg"
  "msg/LiftState.msg"
  "msg/SignalCommand.msg"
  "msg/PicoStatus.msg"
  DEPENDENCIES std_msgs
)

ament_package()
