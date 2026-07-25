// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:msg/FaultCodes.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__FAULT_CODES__TRAITS_HPP_
#define AMR_MSGS__MSG__DETAIL__FAULT_CODES__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/msg/detail/fault_codes__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace msg
{

inline void to_flow_style_yaml(
  const FaultCodes & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const FaultCodes & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const FaultCodes & msg, bool use_flow_style = false)
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
  const amr_msgs::msg::FaultCodes & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::msg::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::msg::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::msg::FaultCodes & msg)
{
  return amr_msgs::msg::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::msg::FaultCodes>()
{
  return "amr_msgs::msg::FaultCodes";
}

template<>
inline const char * name<amr_msgs::msg::FaultCodes>()
{
  return "amr_msgs/msg/FaultCodes";
}

template<>
struct has_fixed_size<amr_msgs::msg::FaultCodes>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::msg::FaultCodes>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::msg::FaultCodes>
  : std::true_type {};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__MSG__DETAIL__FAULT_CODES__TRAITS_HPP_
