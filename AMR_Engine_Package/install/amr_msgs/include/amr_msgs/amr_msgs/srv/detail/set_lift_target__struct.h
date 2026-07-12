// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:srv/SetLiftTarget.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__STRUCT_H_
#define AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/SetLiftTarget in the package amr_msgs.
typedef struct amr_msgs__srv__SetLiftTarget_Request
{
  float target_position;
} amr_msgs__srv__SetLiftTarget_Request;

// Struct for a sequence of amr_msgs__srv__SetLiftTarget_Request.
typedef struct amr_msgs__srv__SetLiftTarget_Request__Sequence
{
  amr_msgs__srv__SetLiftTarget_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__SetLiftTarget_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/SetLiftTarget in the package amr_msgs.
typedef struct amr_msgs__srv__SetLiftTarget_Response
{
  bool accepted;
} amr_msgs__srv__SetLiftTarget_Response;

// Struct for a sequence of amr_msgs__srv__SetLiftTarget_Response.
typedef struct amr_msgs__srv__SetLiftTarget_Response__Sequence
{
  amr_msgs__srv__SetLiftTarget_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__SetLiftTarget_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__STRUCT_H_
