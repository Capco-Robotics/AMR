// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:srv/GetRobotState.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__BUILDER_HPP_
#define AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/srv/detail/get_robot_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace srv
{


}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::GetRobotState_Request>()
{
  return ::amr_msgs::srv::GetRobotState_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_GetRobotState_Response_active_faults
{
public:
  explicit Init_GetRobotState_Response_active_faults(::amr_msgs::srv::GetRobotState_Response & msg)
  : msg_(msg)
  {}
  ::amr_msgs::srv::GetRobotState_Response active_faults(::amr_msgs::srv::GetRobotState_Response::_active_faults_type arg)
  {
    msg_.active_faults = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::GetRobotState_Response msg_;
};

class Init_GetRobotState_Response_state
{
public:
  Init_GetRobotState_Response_state()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetRobotState_Response_active_faults state(::amr_msgs::srv::GetRobotState_Response::_state_type arg)
  {
    msg_.state = std::move(arg);
    return Init_GetRobotState_Response_active_faults(msg_);
  }

private:
  ::amr_msgs::srv::GetRobotState_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::GetRobotState_Response>()
{
  return amr_msgs::srv::builder::Init_GetRobotState_Response_state();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__BUILDER_HPP_
