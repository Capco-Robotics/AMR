// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:srv/GetPicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__TRAITS_HPP_
#define AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/srv/detail/get_pico_status__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetPicoStatus_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetPicoStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetPicoStatus_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::srv::GetPicoStatus_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::GetPicoStatus_Request & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::GetPicoStatus_Request>()
{
  return "amr_msgs::srv::GetPicoStatus_Request";
}

template<>
inline const char * name<amr_msgs::srv::GetPicoStatus_Request>()
{
  return "amr_msgs/srv/GetPicoStatus_Request";
}

template<>
struct has_fixed_size<amr_msgs::srv::GetPicoStatus_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::GetPicoStatus_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::GetPicoStatus_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetPicoStatus_Response & msg,
  std::ostream & out)
{
  out << "{";
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
    out << ", ";
  }

  // member: available
  {
    out << "available: ";
    rosidl_generator_traits::value_to_yaml(msg.available, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetPicoStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
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

  // member: available
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "available: ";
    rosidl_generator_traits::value_to_yaml(msg.available, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetPicoStatus_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace srv

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::srv::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::srv::GetPicoStatus_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::GetPicoStatus_Response & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::GetPicoStatus_Response>()
{
  return "amr_msgs::srv::GetPicoStatus_Response";
}

template<>
inline const char * name<amr_msgs::srv::GetPicoStatus_Response>()
{
  return "amr_msgs/srv/GetPicoStatus_Response";
}

template<>
struct has_fixed_size<amr_msgs::srv::GetPicoStatus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::GetPicoStatus_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::GetPicoStatus_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<amr_msgs::srv::GetPicoStatus>()
{
  return "amr_msgs::srv::GetPicoStatus";
}

template<>
inline const char * name<amr_msgs::srv::GetPicoStatus>()
{
  return "amr_msgs/srv/GetPicoStatus";
}

template<>
struct has_fixed_size<amr_msgs::srv::GetPicoStatus>
  : std::integral_constant<
    bool,
    has_fixed_size<amr_msgs::srv::GetPicoStatus_Request>::value &&
    has_fixed_size<amr_msgs::srv::GetPicoStatus_Response>::value
  >
{
};

template<>
struct has_bounded_size<amr_msgs::srv::GetPicoStatus>
  : std::integral_constant<
    bool,
    has_bounded_size<amr_msgs::srv::GetPicoStatus_Request>::value &&
    has_bounded_size<amr_msgs::srv::GetPicoStatus_Response>::value
  >
{
};

template<>
struct is_service<amr_msgs::srv::GetPicoStatus>
  : std::true_type
{
};

template<>
struct is_service_request<amr_msgs::srv::GetPicoStatus_Request>
  : std::true_type
{
};

template<>
struct is_service_response<amr_msgs::srv::GetPicoStatus_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__TRAITS_HPP_
