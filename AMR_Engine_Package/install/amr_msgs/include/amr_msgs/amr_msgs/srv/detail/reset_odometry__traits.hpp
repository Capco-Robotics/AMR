// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:srv/ResetOdometry.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__RESET_ODOMETRY__TRAITS_HPP_
#define AMR_MSGS__SRV__DETAIL__RESET_ODOMETRY__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/srv/detail/reset_odometry__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const ResetOdometry_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: x
  {
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << ", ";
  }

  // member: y
  {
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << ", ";
  }

  // member: theta
  {
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ResetOdometry_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: x
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "x: ";
    rosidl_generator_traits::value_to_yaml(msg.x, out);
    out << "\n";
  }

  // member: y
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "y: ";
    rosidl_generator_traits::value_to_yaml(msg.y, out);
    out << "\n";
  }

  // member: theta
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "theta: ";
    rosidl_generator_traits::value_to_yaml(msg.theta, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ResetOdometry_Request & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::ResetOdometry_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::ResetOdometry_Request & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::ResetOdometry_Request>()
{
  return "amr_msgs::srv::ResetOdometry_Request";
}

template<>
inline const char * name<amr_msgs::srv::ResetOdometry_Request>()
{
  return "amr_msgs/srv/ResetOdometry_Request";
}

template<>
struct has_fixed_size<amr_msgs::srv::ResetOdometry_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::ResetOdometry_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::ResetOdometry_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const ResetOdometry_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const ResetOdometry_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: success
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const ResetOdometry_Response & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::ResetOdometry_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::ResetOdometry_Response & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::ResetOdometry_Response>()
{
  return "amr_msgs::srv::ResetOdometry_Response";
}

template<>
inline const char * name<amr_msgs::srv::ResetOdometry_Response>()
{
  return "amr_msgs/srv/ResetOdometry_Response";
}

template<>
struct has_fixed_size<amr_msgs::srv::ResetOdometry_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::ResetOdometry_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::ResetOdometry_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<amr_msgs::srv::ResetOdometry>()
{
  return "amr_msgs::srv::ResetOdometry";
}

template<>
inline const char * name<amr_msgs::srv::ResetOdometry>()
{
  return "amr_msgs/srv/ResetOdometry";
}

template<>
struct has_fixed_size<amr_msgs::srv::ResetOdometry>
  : std::integral_constant<
    bool,
    has_fixed_size<amr_msgs::srv::ResetOdometry_Request>::value &&
    has_fixed_size<amr_msgs::srv::ResetOdometry_Response>::value
  >
{
};

template<>
struct has_bounded_size<amr_msgs::srv::ResetOdometry>
  : std::integral_constant<
    bool,
    has_bounded_size<amr_msgs::srv::ResetOdometry_Request>::value &&
    has_bounded_size<amr_msgs::srv::ResetOdometry_Response>::value
  >
{
};

template<>
struct is_service<amr_msgs::srv::ResetOdometry>
  : std::true_type
{
};

template<>
struct is_service_request<amr_msgs::srv::ResetOdometry_Request>
  : std::true_type
{
};

template<>
struct is_service_response<amr_msgs::srv::ResetOdometry_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__SRV__DETAIL__RESET_ODOMETRY__TRAITS_HPP_
