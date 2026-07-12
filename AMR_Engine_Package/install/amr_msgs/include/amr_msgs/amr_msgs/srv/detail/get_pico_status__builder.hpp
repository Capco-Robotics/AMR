// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:srv/GetPicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__BUILDER_HPP_
#define AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/srv/detail/get_pico_status__struct.hpp"
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
auto build<::amr_msgs::srv::GetPicoStatus_Request>()
{
  return ::amr_msgs::srv::GetPicoStatus_Request(rosidl_runtime_cpp::MessageInitialization::ZERO);
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_GetPicoStatus_Response_available
{
public:
  explicit Init_GetPicoStatus_Response_available(::amr_msgs::srv::GetPicoStatus_Response & msg)
  : msg_(msg)
  {}
  ::amr_msgs::srv::GetPicoStatus_Response available(::amr_msgs::srv::GetPicoStatus_Response::_available_type arg)
  {
    msg_.available = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::GetPicoStatus_Response msg_;
};

class Init_GetPicoStatus_Response_free_mem_bytes
{
public:
  explicit Init_GetPicoStatus_Response_free_mem_bytes(::amr_msgs::srv::GetPicoStatus_Response & msg)
  : msg_(msg)
  {}
  Init_GetPicoStatus_Response_available free_mem_bytes(::amr_msgs::srv::GetPicoStatus_Response::_free_mem_bytes_type arg)
  {
    msg_.free_mem_bytes = std::move(arg);
    return Init_GetPicoStatus_Response_available(msg_);
  }

private:
  ::amr_msgs::srv::GetPicoStatus_Response msg_;
};

class Init_GetPicoStatus_Response_watchdog_resets
{
public:
  explicit Init_GetPicoStatus_Response_watchdog_resets(::amr_msgs::srv::GetPicoStatus_Response & msg)
  : msg_(msg)
  {}
  Init_GetPicoStatus_Response_free_mem_bytes watchdog_resets(::amr_msgs::srv::GetPicoStatus_Response::_watchdog_resets_type arg)
  {
    msg_.watchdog_resets = std::move(arg);
    return Init_GetPicoStatus_Response_free_mem_bytes(msg_);
  }

private:
  ::amr_msgs::srv::GetPicoStatus_Response msg_;
};

class Init_GetPicoStatus_Response_last_rpi_msg_age_ms
{
public:
  explicit Init_GetPicoStatus_Response_last_rpi_msg_age_ms(::amr_msgs::srv::GetPicoStatus_Response & msg)
  : msg_(msg)
  {}
  Init_GetPicoStatus_Response_watchdog_resets last_rpi_msg_age_ms(::amr_msgs::srv::GetPicoStatus_Response::_last_rpi_msg_age_ms_type arg)
  {
    msg_.last_rpi_msg_age_ms = std::move(arg);
    return Init_GetPicoStatus_Response_watchdog_resets(msg_);
  }

private:
  ::amr_msgs::srv::GetPicoStatus_Response msg_;
};

class Init_GetPicoStatus_Response_uptime_ms
{
public:
  Init_GetPicoStatus_Response_uptime_ms()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_GetPicoStatus_Response_last_rpi_msg_age_ms uptime_ms(::amr_msgs::srv::GetPicoStatus_Response::_uptime_ms_type arg)
  {
    msg_.uptime_ms = std::move(arg);
    return Init_GetPicoStatus_Response_last_rpi_msg_age_ms(msg_);
  }

private:
  ::amr_msgs::srv::GetPicoStatus_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::GetPicoStatus_Response>()
{
  return amr_msgs::srv::builder::Init_GetPicoStatus_Response_uptime_ms();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__BUILDER_HPP_
