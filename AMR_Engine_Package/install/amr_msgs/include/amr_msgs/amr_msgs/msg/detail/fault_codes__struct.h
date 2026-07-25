// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:msg/FaultCodes.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__FAULT_CODES__STRUCT_H_
#define AMR_MSGS__MSG__DETAIL__FAULT_CODES__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Constant 'NONE'.
enum
{
  amr_msgs__msg__FaultCodes__NONE = 0
};

/// Constant 'LIFT_OVERCURRENT'.
enum
{
  amr_msgs__msg__FaultCodes__LIFT_OVERCURRENT = 1
};

/// Constant 'LIFT_UNDERCURRENT'.
enum
{
  amr_msgs__msg__FaultCodes__LIFT_UNDERCURRENT = 2
};

/// Constant 'LIFT_SLANT'.
enum
{
  amr_msgs__msg__FaultCodes__LIFT_SLANT = 3
};

/// Constant 'LIFT_LIMIT_SWITCH'.
enum
{
  amr_msgs__msg__FaultCodes__LIFT_LIMIT_SWITCH = 4
};

/// Constant 'LIFT_SENSOR_FAILURE'.
enum
{
  amr_msgs__msg__FaultCodes__LIFT_SENSOR_FAILURE = 5
};

/// Constant 'LIFT_TIMEOUT'.
enum
{
  amr_msgs__msg__FaultCodes__LIFT_TIMEOUT = 6
};

/// Struct defined in msg/FaultCodes in the package amr_msgs.
typedef struct amr_msgs__msg__FaultCodes
{
  uint8_t structure_needs_at_least_one_member;
} amr_msgs__msg__FaultCodes;

// Struct for a sequence of amr_msgs__msg__FaultCodes.
typedef struct amr_msgs__msg__FaultCodes__Sequence
{
  amr_msgs__msg__FaultCodes * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__msg__FaultCodes__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__MSG__DETAIL__FAULT_CODES__STRUCT_H_
