// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/LiftState.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__LIFT_STATE__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__LIFT_STATE__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/lift_state__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_LiftState_limit_lower
{
public:
  explicit Init_LiftState_limit_lower(::amr_msgs::msg::LiftState & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::LiftState limit_lower(::amr_msgs::msg::LiftState::_limit_lower_type arg)
  {
    msg_.limit_lower = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::LiftState msg_;
};

class Init_LiftState_limit_upper
{
public:
  explicit Init_LiftState_limit_upper(::amr_msgs::msg::LiftState & msg)
  : msg_(msg)
  {}
  Init_LiftState_limit_lower limit_upper(::amr_msgs::msg::LiftState::_limit_upper_type arg)
  {
    msg_.limit_upper = std::move(arg);
    return Init_LiftState_limit_lower(msg_);
  }

private:
  ::amr_msgs::msg::LiftState msg_;
};

class Init_LiftState_position
{
public:
  explicit Init_LiftState_position(::amr_msgs::msg::LiftState & msg)
  : msg_(msg)
  {}
  Init_LiftState_limit_upper position(::amr_msgs::msg::LiftState::_position_type arg)
  {
    msg_.position = std::move(arg);
    return Init_LiftState_limit_upper(msg_);
  }

private:
  ::amr_msgs::msg::LiftState msg_;
};

class Init_LiftState_header
{
public:
  Init_LiftState_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LiftState_position header(::amr_msgs::msg::LiftState::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_LiftState_position(msg_);
  }

private:
  ::amr_msgs::msg::LiftState msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::LiftState>()
{
  return amr_msgs::msg::builder::Init_LiftState_header();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__LIFT_STATE__BUILDER_HPP_
