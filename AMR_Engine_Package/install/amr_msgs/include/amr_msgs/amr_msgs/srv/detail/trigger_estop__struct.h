// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:srv/TriggerEstop.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__STRUCT_H_
#define AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/TriggerEstop in the package amr_msgs.
typedef struct amr_msgs__srv__TriggerEstop_Request
{
  bool release;
} amr_msgs__srv__TriggerEstop_Request;

// Struct for a sequence of amr_msgs__srv__TriggerEstop_Request.
typedef struct amr_msgs__srv__TriggerEstop_Request__Sequence
{
  amr_msgs__srv__TriggerEstop_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__TriggerEstop_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/TriggerEstop in the package amr_msgs.
typedef struct amr_msgs__srv__TriggerEstop_Response
{
  bool success;
} amr_msgs__srv__TriggerEstop_Response;

// Struct for a sequence of amr_msgs__srv__TriggerEstop_Response.
typedef struct amr_msgs__srv__TriggerEstop_Response__Sequence
{
  amr_msgs__srv__TriggerEstop_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__TriggerEstop_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__STRUCT_H_
