// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:msg/PicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__PICO_STATUS__TRAITS_HPP_
#define AMR_MSGS__MSG__DETAIL__PICO_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/msg/detail/pico_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace amr_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const PicoStatus & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: uptime_ms
  {
    out << "uptime_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.uptime_ms, out);
    out << ", ";
  }

  // member: last_rpi_msg_age_ms
  {
    out << "last_rpi_msg_age_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.last_rpi_msg_age_ms, out);
    out << ", ";
  }

  // member: watchdog_resets
  {
    out << "watchdog_resets: ";
    rosidl_generator_traits::value_to_yaml(msg.watchdog_resets, out);
    out << ", ";
  }

  // member: free_mem_bytes
  {
    out << "free_mem_bytes: ";
    rosidl_generator_traits::value_to_yaml(msg.free_mem_bytes, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const PicoStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: header
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "header:\n";
    to_block_style_yaml(msg.header, out, indentation + 2);
  }

  // member: uptime_ms
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "uptime_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.uptime_ms, out);
    out << "\n";
  }

  // member: last_rpi_msg_age_ms
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "last_rpi_msg_age_ms: ";
    rosidl_generator_traits::value_to_yaml(msg.last_rpi_msg_age_ms, out);
    out << "\n";
  }

  // member: watchdog_resets
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "watchdog_resets: ";
    rosidl_generator_traits::value_to_yaml(msg.watchdog_resets, out);
    out << "\n";
  }

  // member: free_mem_bytes
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "free_mem_bytes: ";
    rosidl_generator_traits::value_to_yaml(msg.free_mem_bytes, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const PicoStatus & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace msg

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::msg::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::msg::PicoStatus & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::msg::PicoStatus & msg)
{
  return amr_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::msg::PicoStatus>()
{
  return "amr_msgs::msg::PicoStatus";
}

template<>
inline const char * name<amr_msgs::msg::PicoStatus>()
{
  return "amr_msgs/msg/PicoStatus";
}

template<>
struct has_fixed_size<amr_msgs::msg::PicoStatus>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<amr_msgs::msg::PicoStatus>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<amr_msgs::msg::PicoStatus>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__MSG__DETAIL__PICO_STATUS__TRAITS_HPP_
