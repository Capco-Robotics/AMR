// generated from rosidl_generator_cpp/resource/idl__traits.hpp.em
// with input from amr_msgs:action/MoveLift.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__TRAITS_HPP_
#define AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__TRAITS_HPP_

#include <stdint.h>

#include <sstream>
#include <string>
#include <type_traits>

#include "amr_msgs/action/detail/move_lift__struct.hpp"
#include "rosidl_runtime_cpp/traits.hpp"

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_Goal & msg,
  std::ostream & out)
{
  out << "{";
  // member: target_position
  {
    out << "target_position: ";
    rosidl_generator_traits::value_to_yaml(msg.target_position, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveLift_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: target_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "target_position: ";
    rosidl_generator_traits::value_to_yaml(msg.target_position, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveLift_Goal & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_Goal & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_Goal & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_Goal>()
{
  return "amr_msgs::action::MoveLift_Goal";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_Goal>()
{
  return "amr_msgs/action/MoveLift_Goal";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_Goal>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::action::MoveLift_Goal>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_Result & msg,
  std::ostream & out)
{
  out << "{";
  // member: success
  {
    out << "success: ";
    rosidl_generator_traits::value_to_yaml(msg.success, out);
    out << ", ";
  }

  // member: final_position
  {
    out << "final_position: ";
    rosidl_generator_traits::value_to_yaml(msg.final_position, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveLift_Result & msg,
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

  // member: final_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "final_position: ";
    rosidl_generator_traits::value_to_yaml(msg.final_position, out);
    out << "\n";
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveLift_Result & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_Result & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_Result & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_Result>()
{
  return "amr_msgs::action::MoveLift_Result";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_Result>()
{
  return "amr_msgs/action/MoveLift_Result";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_Result>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_Result>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::action::MoveLift_Result>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_Feedback & msg,
  std::ostream & out)
{
  out << "{";
  // member: current_position
  {
    out << "current_position: ";
    rosidl_generator_traits::value_to_yaml(msg.current_position, out);
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
  const MoveLift_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: current_position
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "current_position: ";
    rosidl_generator_traits::value_to_yaml(msg.current_position, out);
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

inline std::string to_yaml(const MoveLift_Feedback & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_Feedback & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_Feedback & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_Feedback>()
{
  return "amr_msgs::action::MoveLift_Feedback";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_Feedback>()
{
  return "amr_msgs/action/MoveLift_Feedback";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_Feedback>
  : std::integral_constant<bool, true> {};

template<>
struct is_message<amr_msgs::action::MoveLift_Feedback>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'goal'
#include "amr_msgs/action/detail/move_lift__traits.hpp"

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_SendGoal_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: goal
  {
    out << "goal: ";
    to_flow_style_yaml(msg.goal, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveLift_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: goal
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal:\n";
    to_block_style_yaml(msg.goal, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveLift_SendGoal_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_SendGoal_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_SendGoal_Request & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_SendGoal_Request>()
{
  return "amr_msgs::action::MoveLift_SendGoal_Request";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_SendGoal_Request>()
{
  return "amr_msgs/action/MoveLift_SendGoal_Request";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_SendGoal_Request>
  : std::integral_constant<bool, has_fixed_size<amr_msgs::action::MoveLift_Goal>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_SendGoal_Request>
  : std::integral_constant<bool, has_bounded_size<amr_msgs::action::MoveLift_Goal>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<amr_msgs::action::MoveLift_SendGoal_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__traits.hpp"

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_SendGoal_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: accepted
  {
    out << "accepted: ";
    rosidl_generator_traits::value_to_yaml(msg.accepted, out);
    out << ", ";
  }

  // member: stamp
  {
    out << "stamp: ";
    to_flow_style_yaml(msg.stamp, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveLift_SendGoal_Response & msg,
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

  // member: stamp
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "stamp:\n";
    to_block_style_yaml(msg.stamp, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveLift_SendGoal_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_SendGoal_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_SendGoal_Response & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_SendGoal_Response>()
{
  return "amr_msgs::action::MoveLift_SendGoal_Response";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_SendGoal_Response>()
{
  return "amr_msgs/action/MoveLift_SendGoal_Response";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_SendGoal_Response>
  : std::integral_constant<bool, has_fixed_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_SendGoal_Response>
  : std::integral_constant<bool, has_bounded_size<builtin_interfaces::msg::Time>::value> {};

template<>
struct is_message<amr_msgs::action::MoveLift_SendGoal_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<amr_msgs::action::MoveLift_SendGoal>()
{
  return "amr_msgs::action::MoveLift_SendGoal";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_SendGoal>()
{
  return "amr_msgs/action/MoveLift_SendGoal";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_SendGoal>
  : std::integral_constant<
    bool,
    has_fixed_size<amr_msgs::action::MoveLift_SendGoal_Request>::value &&
    has_fixed_size<amr_msgs::action::MoveLift_SendGoal_Response>::value
  >
{
};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_SendGoal>
  : std::integral_constant<
    bool,
    has_bounded_size<amr_msgs::action::MoveLift_SendGoal_Request>::value &&
    has_bounded_size<amr_msgs::action::MoveLift_SendGoal_Response>::value
  >
{
};

template<>
struct is_service<amr_msgs::action::MoveLift_SendGoal>
  : std::true_type
{
};

template<>
struct is_service_request<amr_msgs::action::MoveLift_SendGoal_Request>
  : std::true_type
{
};

template<>
struct is_service_response<amr_msgs::action::MoveLift_SendGoal_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_GetResult_Request & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveLift_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveLift_GetResult_Request & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_GetResult_Request & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_GetResult_Request & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_GetResult_Request>()
{
  return "amr_msgs::action::MoveLift_GetResult_Request";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_GetResult_Request>()
{
  return "amr_msgs/action/MoveLift_GetResult_Request";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_GetResult_Request>
  : std::integral_constant<bool, has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_GetResult_Request>
  : std::integral_constant<bool, has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<amr_msgs::action::MoveLift_GetResult_Request>
  : std::true_type {};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'result'
// already included above
// #include "amr_msgs/action/detail/move_lift__traits.hpp"

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_GetResult_Response & msg,
  std::ostream & out)
{
  out << "{";
  // member: status
  {
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << ", ";
  }

  // member: result
  {
    out << "result: ";
    to_flow_style_yaml(msg.result, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveLift_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: status
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "status: ";
    rosidl_generator_traits::value_to_yaml(msg.status, out);
    out << "\n";
  }

  // member: result
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "result:\n";
    to_block_style_yaml(msg.result, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveLift_GetResult_Response & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_GetResult_Response & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_GetResult_Response & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_GetResult_Response>()
{
  return "amr_msgs::action::MoveLift_GetResult_Response";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_GetResult_Response>()
{
  return "amr_msgs/action/MoveLift_GetResult_Response";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_GetResult_Response>
  : std::integral_constant<bool, has_fixed_size<amr_msgs::action::MoveLift_Result>::value> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_GetResult_Response>
  : std::integral_constant<bool, has_bounded_size<amr_msgs::action::MoveLift_Result>::value> {};

template<>
struct is_message<amr_msgs::action::MoveLift_GetResult_Response>
  : std::true_type {};

}  // namespace rosidl_generator_traits

namespace rosidl_generator_traits
{

template<>
inline const char * data_type<amr_msgs::action::MoveLift_GetResult>()
{
  return "amr_msgs::action::MoveLift_GetResult";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_GetResult>()
{
  return "amr_msgs/action/MoveLift_GetResult";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_GetResult>
  : std::integral_constant<
    bool,
    has_fixed_size<amr_msgs::action::MoveLift_GetResult_Request>::value &&
    has_fixed_size<amr_msgs::action::MoveLift_GetResult_Response>::value
  >
{
};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_GetResult>
  : std::integral_constant<
    bool,
    has_bounded_size<amr_msgs::action::MoveLift_GetResult_Request>::value &&
    has_bounded_size<amr_msgs::action::MoveLift_GetResult_Response>::value
  >
{
};

template<>
struct is_service<amr_msgs::action::MoveLift_GetResult>
  : std::true_type
{
};

template<>
struct is_service_request<amr_msgs::action::MoveLift_GetResult_Request>
  : std::true_type
{
};

template<>
struct is_service_response<amr_msgs::action::MoveLift_GetResult_Response>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__traits.hpp"
// Member 'feedback'
// already included above
// #include "amr_msgs/action/detail/move_lift__traits.hpp"

namespace amr_msgs
{

namespace action
{

inline void to_flow_style_yaml(
  const MoveLift_FeedbackMessage & msg,
  std::ostream & out)
{
  out << "{";
  // member: goal_id
  {
    out << "goal_id: ";
    to_flow_style_yaml(msg.goal_id, out);
    out << ", ";
  }

  // member: feedback
  {
    out << "feedback: ";
    to_flow_style_yaml(msg.feedback, out);
  }
  out << "}";
}  // NOLINT(readability/fn_size)

inline void to_block_style_yaml(
  const MoveLift_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  // member: goal_id
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "goal_id:\n";
    to_block_style_yaml(msg.goal_id, out, indentation + 2);
  }

  // member: feedback
  {
    if (indentation > 0) {
      out << std::string(indentation, ' ');
    }
    out << "feedback:\n";
    to_block_style_yaml(msg.feedback, out, indentation + 2);
  }
}  // NOLINT(readability/fn_size)

inline std::string to_yaml(const MoveLift_FeedbackMessage & msg, bool use_flow_style = false)
{
  std::ostringstream out;
  if (use_flow_style) {
    to_flow_style_yaml(msg, out);
  } else {
    to_block_style_yaml(msg, out);
  }
  return out.str();
}

}  // namespace action

}  // namespace amr_msgs

namespace rosidl_generator_traits
{

[[deprecated("use amr_msgs::action::to_block_style_yaml() instead")]]
inline void to_yaml(
  const amr_msgs::action::MoveLift_FeedbackMessage & msg,
  std::ostream & out, size_t indentation = 0)
{
  amr_msgs::action::to_block_style_yaml(msg, out, indentation);
}

[[deprecated("use amr_msgs::action::to_yaml() instead")]]
inline std::string to_yaml(const amr_msgs::action::MoveLift_FeedbackMessage & msg)
{
  return amr_msgs::action::to_yaml(msg);
}

template<>
inline const char * data_type<amr_msgs::action::MoveLift_FeedbackMessage>()
{
  return "amr_msgs::action::MoveLift_FeedbackMessage";
}

template<>
inline const char * name<amr_msgs::action::MoveLift_FeedbackMessage>()
{
  return "amr_msgs/action/MoveLift_FeedbackMessage";
}

template<>
struct has_fixed_size<amr_msgs::action::MoveLift_FeedbackMessage>
  : std::integral_constant<bool, has_fixed_size<amr_msgs::action::MoveLift_Feedback>::value && has_fixed_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct has_bounded_size<amr_msgs::action::MoveLift_FeedbackMessage>
  : std::integral_constant<bool, has_bounded_size<amr_msgs::action::MoveLift_Feedback>::value && has_bounded_size<unique_identifier_msgs::msg::UUID>::value> {};

template<>
struct is_message<amr_msgs::action::MoveLift_FeedbackMessage>
  : std::true_type {};

}  // namespace rosidl_generator_traits


namespace rosidl_generator_traits
{

template<>
struct is_action<amr_msgs::action::MoveLift>
  : std::true_type
{
};

template<>
struct is_action_goal<amr_msgs::action::MoveLift_Goal>
  : std::true_type
{
};

template<>
struct is_action_result<amr_msgs::action::MoveLift_Result>
  : std::true_type
{
};

template<>
struct is_action_feedback<amr_msgs::action::MoveLift_Feedback>
  : std::true_type
{
};

}  // namespace rosidl_generator_traits


#endif  // AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__TRAITS_HPP_
