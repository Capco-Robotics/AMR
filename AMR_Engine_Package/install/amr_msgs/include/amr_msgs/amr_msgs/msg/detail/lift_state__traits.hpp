// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:msg/LiftState.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__LIFT_STATE__TRAITS_HPP_
#define AMR_MSGS__MSG__DETAIL__LIFT_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/msg/detail/lift_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__traits.hpp"

namespace amr_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const LiftState & msg,
  std::ostream & out)
{
  out << "{";
  // member: header
  {
    out << "header: ";
    to_flow_style_yaml(msg.header, out);
    out << ", ";
  }

  // member: position
  {
    out << "position: ";
    rosidl_generator_traits::value_to_yaml(msg.position, out);
    out << ", ";
  }

  // member: limit_upper
  {
    out << "limit_upper: ";
    rosidl_generator_traits::value_to_yaml(msg.limit_upper, out);
    out << ", ";
  }

  // member: limit_lower
  {
    out << "limit_lower: ";
    rosidl_generator_traits::value_to_yaml(msg.limit_lower, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const LiftState & msg,
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

  // member: position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "position: ";
    rosidl_generator_traits::value_to_yaml(msg.position, out);
    out << "\n";
  }

  // member: limit_upper
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "limit_upper: ";
    rosidl_generator_traits::value_to_yaml(msg.limit_upper, out);
    out << "\n";
  }

  // member: limit_lower
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "limit_lower: ";
    rosidl_generator_traits::value_to_yaml(msg.limit_lower, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const LiftState & msg, bool use_flow_style = false)
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
  const amr_msgs::msg::LiftState & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::msg::LiftState & msg)
{
  return amr_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::msg::LiftState>()
{
  return "amr_msgs::msg::LiftState";
}

template<>
inline const char * name<amr_msgs::msg::LiftState>()
{
  return "amr_msgs/msg/LiftState";
}

template<>
struct has_fixed_size<amr_msgs::msg::LiftState>
  : std::integral_constant<bool, has_fixed_size<std_msgs::msg::Header>::value> {};

template<>
struct has_bounded_size<amr_msgs::msg::LiftState>
  : std::integral_constant<bool, has_bounded_size<std_msgs::msg::Header>::value> {};

template<>
struct is_message<amr_msgs::msg::LiftState>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__MSG__DETAIL__LIFT_STATE__TRAITS_HPP_
