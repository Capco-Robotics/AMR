// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/SignalCommand.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__SIGNAL_COMMAND__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__SIGNAL_COMMAND__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/signal_command__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_SignalCommand_pattern_id
{
public:
  explicit Init_SignalCommand_pattern_id(::amr_msgs::msg::SignalCommand & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::SignalCommand pattern_id(::amr_msgs::msg::SignalCommand::_pattern_id_type arg)
  {
    msg_.pattern_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::SignalCommand msg_;
};

class Init_SignalCommand_light_on
{
public:
  explicit Init_SignalCommand_light_on(::amr_msgs::msg::SignalCommand & msg)
  : msg_(msg)
  {}
  Init_SignalCommand_pattern_id light_on(::amr_msgs::msg::SignalCommand::_light_on_type arg)
  {
    msg_.light_on = std::move(arg);
    return Init_SignalCommand_pattern_id(msg_);
  }

private:
  ::amr_msgs::msg::SignalCommand msg_;
};

class Init_SignalCommand_siren_on
{
public:
  explicit Init_SignalCommand_siren_on(::amr_msgs::msg::SignalCommand & msg)
  : msg_(msg)
  {}
  Init_SignalCommand_light_on siren_on(::amr_msgs::msg::SignalCommand::_siren_on_type arg)
  {
    msg_.siren_on = std::move(arg);
    return Init_SignalCommand_light_on(msg_);
  }

private:
  ::amr_msgs::msg::SignalCommand msg_;
};

class Init_SignalCommand_header
{
public:
  Init_SignalCommand_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_SignalCommand_siren_on header(::amr_msgs::msg::SignalCommand::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_SignalCommand_siren_on(msg_);
  }

private:
  ::amr_msgs::msg::SignalCommand msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::SignalCommand>()
{
  return amr_msgs::msg::builder::Init_SignalCommand_header();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__SIGNAL_COMMAND__BUILDER_HPP_
