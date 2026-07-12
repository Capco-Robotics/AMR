// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:srv/ResetOdometry.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__RESET_ODOMETRY__BUILDER_HPP_
#define AMR_MSGS__SRV__DETAIL__RESET_ODOMETRY__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/srv/detail/reset_odometry__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_ResetOdometry_Request_theta
{
public:
  explicit Init_ResetOdometry_Request_theta(::amr_msgs::srv::ResetOdometry_Request & msg)
  : msg_(msg)
  {}
  ::amr_msgs::srv::ResetOdometry_Request theta(::amr_msgs::srv::ResetOdometry_Request::_theta_type arg)
  {
    msg_.theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::ResetOdometry_Request msg_;
};

class Init_ResetOdometry_Request_y
{
public:
  explicit Init_ResetOdometry_Request_y(::amr_msgs::srv::ResetOdometry_Request & msg)
  : msg_(msg)
  {}
  Init_ResetOdometry_Request_theta y(::amr_msgs::srv::ResetOdometry_Request::_y_type arg)
  {
    msg_.y = std::move(arg);
    return Init_ResetOdometry_Request_theta(msg_);
  }

private:
  ::amr_msgs::srv::ResetOdometry_Request msg_;
};

class Init_ResetOdometry_Request_x
{
public:
  Init_ResetOdometry_Request_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_ResetOdometry_Request_y x(::amr_msgs::srv::ResetOdometry_Request::_x_type arg)
  {
    msg_.x = std::move(arg);
    return Init_ResetOdometry_Request_y(msg_);
  }

private:
  ::amr_msgs::srv::ResetOdometry_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::ResetOdometry_Request>()
{
  return amr_msgs::srv::builder::Init_ResetOdometry_Request_x();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_ResetOdometry_Response_success
{
public:
  Init_ResetOdometry_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::ResetOdometry_Response success(::amr_msgs::srv::ResetOdometry_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::ResetOdometry_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::ResetOdometry_Response>()
{
  return amr_msgs::srv::builder::Init_ResetOdometry_Response_success();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__RESET_ODOMETRY__BUILDER_HPP_
