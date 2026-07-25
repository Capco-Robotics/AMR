// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/LiftCommand.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/lift_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_LiftCommand_target_position
{
public:
  explicit Init_LiftCommand_target_position(::amr_msgs::msg::LiftCommand & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::LiftCommand target_position(::amr_msgs::msg::LiftCommand::_target_position_type arg)
  {
    msg_.target_position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::LiftCommand msg_;
};

class Init_LiftCommand_header
{
public:
  Init_LiftCommand_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_LiftCommand_target_position header(::amr_msgs::msg::LiftCommand::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_LiftCommand_target_position(msg_);
  }

private:
  ::amr_msgs::msg::LiftCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::LiftCommand>()
{
  return amr_msgs::msg::builder::Init_LiftCommand_header();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__BUILDER_HPP_
