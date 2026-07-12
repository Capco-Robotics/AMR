// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:msg/PicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__PICO_STATUS__STRUCT_H_
#define AMR_MSGS__MSG__DETAIL__PICO_STATUS__STRUCT_H_

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

/// Struct defined in msg/PicoStatus in the package amr_msgs.
typedef struct amr_msgs__msg__PicoStatus
{
  std_msgs__msg__Header header;
  uint32_t uptime_ms;
  uint32_t last_rpi_msg_age_ms;
  uint32_t watchdog_resets;
  uint32_t free_mem_bytes;
} amr_msgs__msg__PicoStatus;

// Struct for a sequence of amr_msgs__msg__PicoStatus.
typedef struct amr_msgs__msg__PicoStatus__Sequence
{
  amr_msgs__msg__PicoStatus * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__msg__PicoStatus__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__MSG__DETAIL__PICO_STATUS__STRUCT_H_
