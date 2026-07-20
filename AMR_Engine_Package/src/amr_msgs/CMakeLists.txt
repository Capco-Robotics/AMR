cmake_minimum_required(VERSION 3.8)
project(amr_msgs)

find_package(ament_cmake REQUIRED)
find_package(rosidl_default_generators REQUIRED)
find_package(std_msgs REQUIRED)
find_package(action_msgs REQUIRED)
find_package(unique_identifier_msgs REQUIRED)

rosidl_generate_interfaces(${PROJECT_NAME}
  "msg/EncoderTicks.msg"
  "msg/WheelSetpoints.msg"
  "msg/LiftCommand.msg"
  "msg/FaultCodes.msg"
  "msg/LiftState.msg"
  "msg/SignalCommand.msg"
  "msg/PicoStatus.msg"
  "srv/ResetOdometry.srv"
  "srv/GetRobotState.srv"
  "srv/AcknowledgeFault.srv"
  "srv/SetLiftTarget.srv"
  "srv/GetPicoStatus.srv"
  "srv/SetDriveLimits.srv"
  "srv/TriggerEstop.srv"
  "action/NavigateToGoal.action"
  "action/MoveLift.action"
  DEPENDENCIES std_msgs action_msgs unique_identifier_msgs
)

ament_package()
