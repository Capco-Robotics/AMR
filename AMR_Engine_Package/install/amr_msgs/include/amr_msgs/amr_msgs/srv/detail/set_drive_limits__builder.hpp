// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:srv/SetDriveLimits.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__BUILDER_HPP_
#define AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/srv/detail/set_drive_limits__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_SetDriveLimits_Request_max_angular_rps
{
public:
  explicit Init_SetDriveLimits_Request_max_angular_rps(::amr_msgs::srv::SetDriveLimits_Request & msg)
  : msg_(msg)
  {}
  ::amr_msgs::srv::SetDriveLimits_Request max_angular_rps(::amr_msgs::srv::SetDriveLimits_Request::_max_angular_rps_type arg)
  {
    msg_.max_angular_rps = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::SetDriveLimits_Request msg_;
};

class Init_SetDriveLimits_Request_max_linear_mps
{
public:
  Init_SetDriveLimits_Request_max_linear_mps()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SetDriveLimits_Request_max_angular_rps max_linear_mps(::amr_msgs::srv::SetDriveLimits_Request::_max_linear_mps_type arg)
  {
    msg_.max_linear_mps = std::move(arg);
    return Init_SetDriveLimits_Request_max_angular_rps(msg_);
  }

private:
  ::amr_msgs::srv::SetDriveLimits_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::SetDriveLimits_Request>()
{
  return amr_msgs::srv::builder::Init_SetDriveLimits_Request_max_linear_mps();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_SetDriveLimits_Response_accepted
{
public:
  Init_SetDriveLimits_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::SetDriveLimits_Response accepted(::amr_msgs::srv::SetDriveLimits_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::SetDriveLimits_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::SetDriveLimits_Response>()
{
  return amr_msgs::srv::builder::Init_SetDriveLimits_Response_accepted();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__BUILDER_HPP_
