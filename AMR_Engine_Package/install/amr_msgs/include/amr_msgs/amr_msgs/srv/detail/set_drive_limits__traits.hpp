// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:srv/SetDriveLimits.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__TRAITS_HPP_
#define AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/srv/detail/set_drive_limits__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetDriveLimits_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: max_linear_mps
  {
    out << "max_linear_mps: ";
    rosidl_generator_traits::value_to_yaml(msg.max_linear_mps, out);
    out << ", ";
  }

  // member: max_angular_rps
  {
    out << "max_angular_rps: ";
    rosidl_generator_traits::value_to_yaml(msg.max_angular_rps, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetDriveLimits_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: max_linear_mps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_linear_mps: ";
    rosidl_generator_traits::value_to_yaml(msg.max_linear_mps, out);
    out << "\n";
  }

  // member: max_angular_rps
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "max_angular_rps: ";
    rosidl_generator_traits::value_to_yaml(msg.max_angular_rps, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetDriveLimits_Request & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::SetDriveLimits_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::SetDriveLimits_Request & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::SetDriveLimits_Request>()
{
  return "amr_msgs::srv::SetDriveLimits_Request";
}

template<>
inline const char * name<amr_msgs::srv::SetDriveLimits_Request>()
{
  return "amr_msgs/srv/SetDriveLimits_Request";
}

template<>
struct has_fixed_size<amr_msgs::srv::SetDriveLimits_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::SetDriveLimits_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::SetDriveLimits_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const SetDriveLimits_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const SetDriveLimits_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: accepted
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const SetDriveLimits_Response & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::SetDriveLimits_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::SetDriveLimits_Response & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::SetDriveLimits_Response>()
{
  return "amr_msgs::srv::SetDriveLimits_Response";
}

template<>
inline const char * name<amr_msgs::srv::SetDriveLimits_Response>()
{
  return "amr_msgs/srv/SetDriveLimits_Response";
}

template<>
struct has_fixed_size<amr_msgs::srv::SetDriveLimits_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::SetDriveLimits_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::SetDriveLimits_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<amr_msgs::srv::SetDriveLimits>()
{
  return "amr_msgs::srv::SetDriveLimits";
}

template<>
inline const char * name<amr_msgs::srv::SetDriveLimits>()
{
  return "amr_msgs/srv/SetDriveLimits";
}

template<>
struct has_fixed_size<amr_msgs::srv::SetDriveLimits>
  : std::integral_constant<
    bool,
    has_fixed_size<amr_msgs::srv::SetDriveLimits_Request>::value &&
    has_fixed_size<amr_msgs::srv::SetDriveLimits_Response>::value
  >
{
};

template<>
struct has_bounded_size<amr_msgs::srv::SetDriveLimits>
  : std::integral_constant<
    bool,
    has_bounded_size<amr_msgs::srv::SetDriveLimits_Request>::value &&
    has_bounded_size<amr_msgs::srv::SetDriveLimits_Response>::value
  >
{
};

template<>
struct is_service<amr_msgs::srv::SetDriveLimits>
  : std::true_type
{
};

template<>
struct is_service_request<amr_msgs::srv::SetDriveLimits_Request>
  : std::true_type
{
};

template<>
struct is_service_response<amr_msgs::srv::SetDriveLimits_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__TRAITS_HPP_
