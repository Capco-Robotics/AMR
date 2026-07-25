// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from amr_msgs:msg/WheelSetpoints.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "amr_msgs/msg/detail/wheel_setpoints__rosidl_typesupport_introspection_c.h"
#include "amr_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "amr_msgs/msg/detail/wheel_setpoints__functions.h"
#include "amr_msgs/msg/detail/wheel_setpoints__struct.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/header.h"
// Member `header`
#include "std_msgs/msg/detail/header__rosidl_typesupport_introspection_c.h"

#ifdef __cplusplus
extern "C"
{
#endif

void amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  amr_msgs__msg__WheelSetpoints__init(message_memory);
}

void amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_fini_function(void * message_memory)
{
  amr_msgs__msg__WheelSetpoints__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_member_array[3] = {
  {
    "header",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_MESSAGE,  // type
    0,  // upper bound of string
    NULL,  // members of sub message (initialized later)
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_msgs__msg__WheelSetpoints, header),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "left_speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_msgs__msg__WheelSetpoints, left_speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "right_speed",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_FLOAT,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_msgs__msg__WheelSetpoints, right_speed),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_members = {
  "amr_msgs__msg",  // message namespace
  "WheelSetpoints",  // message name
  3,  // number of fields
  sizeof(amr_msgs__msg__WheelSetpoints),
  amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_member_array,  // message members
  amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_init_function,  // function to initialize message memory (memory has to be allocated)
  amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_type_support_handle = {
  0,
  &amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_amr_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, msg, WheelSetpoints)() {
  amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_member_array[0].members_ =
    ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, std_msgs, msg, Header)();
  if (!amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_type_support_handle.typesupport_identifier) {
    amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &amr_msgs__msg__WheelSetpoints__rosidl_typesupport_introspection_c__WheelSetpoints_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif
