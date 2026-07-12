// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:srv/GetRobotState.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__TRAITS_HPP_
#define AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/srv/detail/get_robot_state__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetRobotState_Request & msg,
  std::ostream & out)
{
  (void)msg;
  out << "null";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetRobotState_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  (void)msg;
  (void)indentation;
  out << "null\n";
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetRobotState_Request & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::GetRobotState_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::GetRobotState_Request & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::GetRobotState_Request>()
{
  return "amr_msgs::srv::GetRobotState_Request";
}

template<>
inline const char * name<amr_msgs::srv::GetRobotState_Request>()
{
  return "amr_msgs/srv/GetRobotState_Request";
}

template<>
struct has_fixed_size<amr_msgs::srv::GetRobotState_Request>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::srv::GetRobotState_Request>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::srv::GetRobotState_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace amr_msgs
{

namespace srv
{

inline void to_flow_style_yaml(
  const GetRobotState_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: state
  {
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << ", ";
  }

  // member: active_faults
  {
    if (msg.active_faults.size() == 0) {
      out << "active_faults: []";
    } else {
      out << "active_faults: [";
      size_t pending_items = msg.active_faults.size();
      for (auto item : msg.active_faults) {
        rosidl_generator_traits::value_to_yaml(item, out);
        if (--pending_items > 0) {
          out << ", ";
        }
      }
      out << "]";
    }
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const GetRobotState_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: state
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "state: ";
    rosidl_generator_traits::value_to_yaml(msg.state, out);
    out << "\n";
  }

  // member: active_faults
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    if (msg.active_faults.size() == 0) {
      out << "active_faults: []\n";
    } else {
      out << "active_faults:\n";
      for (auto item : msg.active_faults) {
        if (indentation > 0) {
          out << std::string(indentation, ' ');
        }
        out << "- ";
        rosidl_generator_traits::value_to_yaml(item, out);
        out << "\n";
      }
    }
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const GetRobotState_Response & msg, bool use_flow_style = false)
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
  const amr_msgs::srv::GetRobotState_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::srv::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::srv::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::srv::GetRobotState_Response & msg)
{
  return amr_msgs::srv::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::srv::GetRobotState_Response>()
{
  return "amr_msgs::srv::GetRobotState_Response";
}

template<>
inline const char * name<amr_msgs::srv::GetRobotState_Response>()
{
  return "amr_msgs/srv/GetRobotState_Response";
}

template<>
struct has_fixed_size<amr_msgs::srv::GetRobotState_Response>
  : std::integral_constant<bool, false> {};

template<>
struct has_bounded_size<amr_msgs::srv::GetRobotState_Response>
  : std::integral_constant<bool, false> {};

template<>
struct is_message<amr_msgs::srv::GetRobotState_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<amr_msgs::srv::GetRobotState>()
{
  return "amr_msgs::srv::GetRobotState";
}

template<>
inline const char * name<amr_msgs::srv::GetRobotState>()
{
  return "amr_msgs/srv/GetRobotState";
}

template<>
struct has_fixed_size<amr_msgs::srv::GetRobotState>
  : std::integral_constant<
    bool,
    has_fixed_size<amr_msgs::srv::GetRobotState_Request>::value &&
    has_fixed_size<amr_msgs::srv::GetRobotState_Response>::value
  >
{
};

template<>
struct has_bounded_size<amr_msgs::srv::GetRobotState>
  : std::integral_constant<
    bool,
    has_bounded_size<amr_msgs::srv::GetRobotState_Request>::value &&
    has_bounded_size<amr_msgs::srv::GetRobotState_Response>::value
  >
{
};

template<>
struct is_service<amr_msgs::srv::GetRobotState>
  : std::true_type
{
};

template<>
struct is_service_request<amr_msgs::srv::GetRobotState_Request>
  : std::true_type
{
};

template<>
struct is_service_response<amr_msgs::srv::GetRobotState_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

#endif  // AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__TRAITS_HPP_
