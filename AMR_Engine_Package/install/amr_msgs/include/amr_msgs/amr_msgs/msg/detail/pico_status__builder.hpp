// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:msg/PicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__PICO_STATUS__BUILDER_HPP_
#define AMR_MSGS__MSG__DETAIL__PICO_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/msg/detail/pico_status__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace msg
{

namespace builder
{

class Init_PicoStatus_free_mem_bytes
{
public:
  explicit Init_PicoStatus_free_mem_bytes(::amr_msgs::msg::PicoStatus & msg)
  : msg_(msg)
  {}
  ::amr_msgs::msg::PicoStatus free_mem_bytes(::amr_msgs::msg::PicoStatus::_free_mem_bytes_type arg)
  {
    msg_.free_mem_bytes = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::msg::PicoStatus msg_;
};

class Init_PicoStatus_watchdog_resets
{
public:
  explicit Init_PicoStatus_watchdog_resets(::amr_msgs::msg::PicoStatus & msg)
  : msg_(msg)
  {}
  Init_PicoStatus_free_mem_bytes watchdog_resets(::amr_msgs::msg::PicoStatus::_watchdog_resets_type arg)
  {
    msg_.watchdog_resets = std::move(arg);
    return Init_PicoStatus_free_mem_bytes(msg_);
  }

private:
  ::amr_msgs::msg::PicoStatus msg_;
};

class Init_PicoStatus_last_rpi_msg_age_ms
{
public:
  explicit Init_PicoStatus_last_rpi_msg_age_ms(::amr_msgs::msg::PicoStatus & msg)
  : msg_(msg)
  {}
  Init_PicoStatus_watchdog_resets last_rpi_msg_age_ms(::amr_msgs::msg::PicoStatus::_last_rpi_msg_age_ms_type arg)
  {
    msg_.last_rpi_msg_age_ms = std::move(arg);
    return Init_PicoStatus_watchdog_resets(msg_);
  }

private:
  ::amr_msgs::msg::PicoStatus msg_;
};

class Init_PicoStatus_uptime_ms
{
public:
  explicit Init_PicoStatus_uptime_ms(::amr_msgs::msg::PicoStatus & msg)
  : msg_(msg)
  {}
  Init_PicoStatus_last_rpi_msg_age_ms uptime_ms(::amr_msgs::msg::PicoStatus::_uptime_ms_type arg)
  {
    msg_.uptime_ms = std::move(arg);
    return Init_PicoStatus_last_rpi_msg_age_ms(msg_);
  }

private:
  ::amr_msgs::msg::PicoStatus msg_;
};

class Init_PicoStatus_header
{
public:
  Init_PicoStatus_header()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_PicoStatus_uptime_ms header(::amr_msgs::msg::PicoStatus::_header_type arg)
  {
    msg_.header = std::move(arg);
    return Init_PicoStatus_uptime_ms(msg_);
  }

private:
  ::amr_msgs::msg::PicoStatus msg_;
};

}  // namespace builder

}  // namespace msg

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::msg::PicoStatus>()
{
  return amr_msgs::msg::builder::Init_PicoStatus_header();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__PICO_STATUS__BUILDER_HPP_
