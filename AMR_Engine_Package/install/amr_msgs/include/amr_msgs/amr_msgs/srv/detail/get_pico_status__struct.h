// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:srv/GetPicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__STRUCT_H_
#define AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in srv/GetPicoStatus in the package amr_msgs.
typedef struct amr_msgs__srv__GetPicoStatus_Request
{
  uint8_t structure_needs_at_least_one_member;
} amr_msgs__srv__GetPicoStatus_Request;

// Struct for a sequence of amr_msgs__srv__GetPicoStatus_Request.
typedef struct amr_msgs__srv__GetPicoStatus_Request__Sequence
{
  amr_msgs__srv__GetPicoStatus_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__GetPicoStatus_Request__Sequence;


// Constants defined in the message

/// Struct defined in srv/GetPicoStatus in the package amr_msgs.
typedef struct amr_msgs__srv__GetPicoStatus_Response
{
  uint32_t uptime_ms;
  uint32_t last_rpi_msg_age_ms;
  uint32_t watchdog_resets;
  uint32_t free_mem_bytes;
  bool available;
} amr_msgs__srv__GetPicoStatus_Response;

// Struct for a sequence of amr_msgs__srv__GetPicoStatus_Response.
typedef struct amr_msgs__srv__GetPicoStatus_Response__Sequence
{
  amr_msgs__srv__GetPicoStatus_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__srv__GetPicoStatus_Response__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__STRUCT_H_
