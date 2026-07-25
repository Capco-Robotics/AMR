// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:srv/SetLiftTarget.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__BUILDER_HPP_
#define AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/srv/detail/set_lift_target__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_SetLiftTarget_Request_target_position
{
public:
  Init_SetLiftTarget_Request_target_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::SetLiftTarget_Request target_position(::amr_msgs::srv::SetLiftTarget_Request::_target_position_type arg)
  {
    msg_.target_position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::SetLiftTarget_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::SetLiftTarget_Request>()
{
  return amr_msgs::srv::builder::Init_SetLiftTarget_Request_target_position();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_SetLiftTarget_Response_accepted
{
public:
  Init_SetLiftTarget_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::SetLiftTarget_Response accepted(::amr_msgs::srv::SetLiftTarget_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::SetLiftTarget_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::SetLiftTarget_Response>()
{
  return amr_msgs::srv::builder::Init_SetLiftTarget_Response_accepted();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__BUILDER_HPP_
