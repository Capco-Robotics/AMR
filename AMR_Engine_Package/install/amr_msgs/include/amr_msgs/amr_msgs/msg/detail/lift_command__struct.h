// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:msg/LiftCommand.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__STRUCT_H_
#define AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.h"

/// Struct defined in msg/LiftCommand in the package amr_msgs.
typedef struct amr_msgs__msg__LiftCommand
{
  std_msgs__msg__Header header;
  float target_position;
} amr_msgs__msg__LiftCommand;

// Struct for a sequence of amr_msgs__msg__LiftCommand.
typedef struct amr_msgs__msg__LiftCommand__Sequence
{
  amr_msgs__msg__LiftCommand * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__msg__LiftCommand__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__STRUCT_H_
