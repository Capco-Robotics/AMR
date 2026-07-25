// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/EncoderTicks.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__ENCODER_TICKS__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__ENCODER_TICKS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/encoder_ticks__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_EncoderTicks_dt_ms
{
public:
  explicit Init_EncoderTicks_dt_ms(::amr_msgs::msg::EncoderTicks & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::EncoderTicks dt_ms(::amr_msgs::msg::EncoderTicks::_dt_ms_type arg)
  {
    msg_.dt_ms = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::EncoderTicks msg_;
};

class Init_EncoderTicks_right_ticks
{
public:
  explicit Init_EncoderTicks_right_ticks(::amr_msgs::msg::EncoderTicks & msg)
  : msg_(msg)
  {}
  Init_EncoderTicks_dt_ms right_ticks(::amr_msgs::msg::EncoderTicks::_right_ticks_type arg)
  {
    msg_.right_ticks = std::move(arg);
    return Init_EncoderTicks_dt_ms(msg_);
  }

private:
  ::amr_msgs::msg::EncoderTicks msg_;
};

class Init_EncoderTicks_left_ticks
{
public:
  explicit Init_EncoderTicks_left_ticks(::amr_msgs::msg::EncoderTicks & msg)
  : msg_(msg)
  {}
  Init_EncoderTicks_right_ticks left_ticks(::amr_msgs::msg::EncoderTicks::_left_ticks_type arg)
  {
    msg_.left_ticks = std::move(arg);
    return Init_EncoderTicks_right_ticks(msg_);
  }

private:
  ::amr_msgs::msg::EncoderTicks msg_;
};

class Init_EncoderTicks_header
{
public:
  Init_EncoderTicks_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_EncoderTicks_left_ticks header(::amr_msgs::msg::EncoderTicks::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_EncoderTicks_left_ticks(msg_);
  }

private:
  ::amr_msgs::msg::EncoderTicks msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::EncoderTicks>()
{
  return amr_msgs::msg::builder::Init_EncoderTicks_header();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__ENCODER_TICKS__BUILDER_HPP_
