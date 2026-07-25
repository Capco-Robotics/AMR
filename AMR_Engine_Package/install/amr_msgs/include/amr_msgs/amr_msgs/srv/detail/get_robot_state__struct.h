// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:srv/GetRobotState.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__STRUCT_H_
#define AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetRobotState in the package amr_msgs.
typedef struct amr_msgs__srv__GetRobotState_Request
{
  uint8_t structure_needs_at_least_one_member;
} amr_msgs__srv__GetRobotState_Request;

// Struct for a sequence of amr_msgs__srv__GetRobotState_Request.
typedef struct amr_msgs__srv__GetRobotState_Request__Sequence
{
  amr_msgs__srv__GetRobotState_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__GetRobotState_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'state'
// Member 'active_faults'
#include "rosidl_runtime_c/string.h"

/// Struct defined in srv/GetRobotState in the package amr_msgs.
typedef struct amr_msgs__srv__GetRobotState_Response
{
  rosidl_runtime_c__String state;
  rosidl_runtime_c__String__Sequence active_faults;
} amr_msgs__srv__GetRobotState_Response;

// Struct for a sequence of amr_msgs__srv__GetRobotState_Response.
typedef struct amr_msgs__srv__GetRobotState_Response__Sequence
{
  amr_msgs__srv__GetRobotState_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__GetRobotState_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__STRUCT_H_
