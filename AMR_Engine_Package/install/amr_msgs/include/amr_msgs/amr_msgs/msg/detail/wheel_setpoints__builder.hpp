// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/WheelSetpoints.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__WHEEL_SETPOINTS__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__WHEEL_SETPOINTS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/wheel_setpoints__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_WheelSetpoints_right_speed
{
public:
  explicit Init_WheelSetpoints_right_speed(::amr_msgs::msg::WheelSetpoints & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::WheelSetpoints right_speed(::amr_msgs::msg::WheelSetpoints::_right_speed_type arg)
  {
    msg_.right_speed = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::WheelSetpoints msg_;
};

class Init_WheelSetpoints_left_speed
{
public:
  explicit Init_WheelSetpoints_left_speed(::amr_msgs::msg::WheelSetpoints & msg)
  : msg_(msg)
  {}
  Init_WheelSetpoints_right_speed left_speed(::amr_msgs::msg::WheelSetpoints::_left_speed_type arg)
  {
    msg_.left_speed = std::move(arg);
    return Init_WheelSetpoints_right_speed(msg_);
  }

private:
  ::amr_msgs::msg::WheelSetpoints msg_;
};

class Init_WheelSetpoints_header
{
public:
  Init_WheelSetpoints_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_WheelSetpoints_left_speed header(::amr_msgs::msg::WheelSetpoints::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_WheelSetpoints_left_speed(msg_);
  }

private:
  ::amr_msgs::msg::WheelSetpoints msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::WheelSetpoints>()
{
  return amr_msgs::msg::builder::Init_WheelSetpoints_header();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__WHEEL_SETPOINTS__BUILDER_HPP_
