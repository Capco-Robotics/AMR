// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:srv/AcknowledgeFault.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__TRAITS_HPP_
#define AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/srv/detail/acknowledge_fault__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const AcknowledgeFault_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: fault_id
  {
    out << "fault_id: ";
    rosidl_generator_traits::value_to_yaml(msg.fault_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const AcknowledgeFault_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: fault_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "fault_id: ";
    rosidl_generator_traits::value_to_yaml(msg.fault_id, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const AcknowledgeFault_Request & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::AcknowledgeFault_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::AcknowledgeFault_Request & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::AcknowledgeFault_Request>()
{
  return "amr_msgs::srv::AcknowledgeFault_Request";
}

template<>
inline const char * name<amr_msgs::srv::AcknowledgeFault_Request>()
{
  return "amr_msgs/srv/AcknowledgeFault_Request";
}

template<>
struct has_fixed_size<amr_msgs::srv::AcknowledgeFault_Request>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<amr_msgs::srv::AcknowledgeFault_Request>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<amr_msgs::srv::AcknowledgeFault_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const AcknowledgeFault_Response & msg,
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
  const AcknowledgeFault_Response & msg,
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

inline std::string to_yaml(const AcknowledgeFault_Response & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::AcknowledgeFault_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::AcknowledgeFault_Response & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::AcknowledgeFault_Response>()
{
  return "amr_msgs::srv::AcknowledgeFault_Response";
}

template<>
inline const char * name<amr_msgs::srv::AcknowledgeFault_Response>()
{
  return "amr_msgs/srv/AcknowledgeFault_Response";
}

template<>
struct has_fixed_size<amr_msgs::srv::AcknowledgeFault_Response>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::AcknowledgeFault_Response>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::AcknowledgeFault_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<amr_msgs::srv::AcknowledgeFault>()
{
  return "amr_msgs::srv::AcknowledgeFault";
}

template<>
inline const char * name<amr_msgs::srv::AcknowledgeFault>()
{
  return "amr_msgs/srv/AcknowledgeFault";
}

template<>
struct has_fixed_size<amr_msgs::srv::AcknowledgeFault>
  : std::integral_constant<
    bool,
    has_fixed_size<amr_msgs::srv::AcknowledgeFault_Request>::value &&
    has_fixed_size<amr_msgs::srv::AcknowledgeFault_Response>::value
  >
{
};

template<>
struct has_bounded_size<amr_msgs::srv::AcknowledgeFault>
  : std::integral_constant<
    bool,
    has_bounded_size<amr_msgs::srv::AcknowledgeFault_Request>::value &&
    has_bounded_size<amr_msgs::srv::AcknowledgeFault_Response>::value
  >
{
};

template<>
struct is_service<amr_msgs::srv::AcknowledgeFault>
  : std::true_type
{
};

template<>
struct is_service_request<amr_msgs::srv::AcknowledgeFault_Request>
  : std::true_type
{
};

template<>
struct is_service_response<amr_msgs::srv::AcknowledgeFault_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__TRAITS_HPP_
