// generated from rosidl_typesupport_introspection_c/resource/idl__type_support.c.em
// with input from amr_msgs:srv/GetRobotState.idl
// generated code does not contain a copyright notice

#include <stddef.h>
#include "amr_msgs/srv/detail/get_robot_state__rosidl_typesupport_introspection_c.h"
#include "amr_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
#include "rosidl_typesupport_introspection_c/field_types.h"
#include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/message_introspection.h"
#include "amr_msgs/srv/detail/get_robot_state__functions.h"
#include "amr_msgs/srv/detail/get_robot_state__struct.h"


#ifdef __cplusplus
extern "C"
{
#endif

void amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  amr_msgs__srv__GetRobotState_Request__init(message_memory);
}

void amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_fini_function(void * message_memory)
{
  amr_msgs__srv__GetRobotState_Request__fini(message_memory);
}

static rosidl_typesupport_introspection_c__MessageMember amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_member_array[1] = {
  {
    "structure_needs_at_least_one_member",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_UINT8,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_msgs__srv__GetRobotState_Request, structure_needs_at_least_one_member),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_members = {
  "amr_msgs__srv",  // message namespace
  "GetRobotState_Request",  // message name
  1,  // number of fields
  sizeof(amr_msgs__srv__GetRobotState_Request),
  amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_member_array,  // message members
  amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_init_function,  // function to initialize message memory (memory has to be allocated)
  amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_type_support_handle = {
  0,
  &amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_amr_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, srv, GetRobotState_Request)() {
  if (!amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_type_support_handle.typesupport_identifier) {
    amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &amr_msgs__srv__GetRobotState_Request__rosidl_typesupport_introspection_c__GetRobotState_Request_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

// already included above
// #include <stddef.h>
// already included above
// #include "amr_msgs/srv/detail/get_robot_state__rosidl_typesupport_introspection_c.h"
// already included above
// #include "amr_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "rosidl_typesupport_introspection_c/field_types.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
// already included above
// #include "rosidl_typesupport_introspection_c/message_introspection.h"
// already included above
// #include "amr_msgs/srv/detail/get_robot_state__functions.h"
// already included above
// #include "amr_msgs/srv/detail/get_robot_state__struct.h"


// Include directives for member types
// Member `state`
// Member `active_faults`
#include "rosidl_runtime_c/string_functions.h"

#ifdef __cplusplus
extern "C"
{
#endif

void amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_init_function(
  void * message_memory, enum rosidl_runtime_c__message_initialization _init)
{
  // TODO(karsten1987): initializers are not yet implemented for typesupport c
  // see https://github.com/ros2/ros2/issues/397
  (void) _init;
  amr_msgs__srv__GetRobotState_Response__init(message_memory);
}

void amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_fini_function(void * message_memory)
{
  amr_msgs__srv__GetRobotState_Response__fini(message_memory);
}

size_t amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__size_function__GetRobotState_Response__active_faults(
  const void * untyped_member)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return member->size;
}

const void * amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__get_const_function__GetRobotState_Response__active_faults(
  const void * untyped_member, size_t index)
{
  const rosidl_runtime_c__String__Sequence * member =
    (const rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void * amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__get_function__GetRobotState_Response__active_faults(
  void * untyped_member, size_t index)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  return &member->data[index];
}

void amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__fetch_function__GetRobotState_Response__active_faults(
  const void * untyped_member, size_t index, void * untyped_value)
{
  const rosidl_runtime_c__String * item =
    ((const rosidl_runtime_c__String *)
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__get_const_function__GetRobotState_Response__active_faults(untyped_member, index));
  rosidl_runtime_c__String * value =
    (rosidl_runtime_c__String *)(untyped_value);
  *value = *item;
}

void amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__assign_function__GetRobotState_Response__active_faults(
  void * untyped_member, size_t index, const void * untyped_value)
{
  rosidl_runtime_c__String * item =
    ((rosidl_runtime_c__String *)
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__get_function__GetRobotState_Response__active_faults(untyped_member, index));
  const rosidl_runtime_c__String * value =
    (const rosidl_runtime_c__String *)(untyped_value);
  *item = *value;
}

bool amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__resize_function__GetRobotState_Response__active_faults(
  void * untyped_member, size_t size)
{
  rosidl_runtime_c__String__Sequence * member =
    (rosidl_runtime_c__String__Sequence *)(untyped_member);
  rosidl_runtime_c__String__Sequence__fini(member);
  return rosidl_runtime_c__String__Sequence__init(member, size);
}

static rosidl_typesupport_introspection_c__MessageMember amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_member_array[2] = {
  {
    "state",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    false,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_msgs__srv__GetRobotState_Response, state),  // bytes offset in struct
    NULL,  // default value
    NULL,  // size() function pointer
    NULL,  // get_const(index) function pointer
    NULL,  // get(index) function pointer
    NULL,  // fetch(index, &value) function pointer
    NULL,  // assign(index, value) function pointer
    NULL  // resize(index) function pointer
  },
  {
    "active_faults",  // name
    rosidl_typesupport_introspection_c__ROS_TYPE_STRING,  // type
    0,  // upper bound of string
    NULL,  // members of sub message
    true,  // is array
    0,  // array size
    false,  // is upper bound
    offsetof(amr_msgs__srv__GetRobotState_Response, active_faults),  // bytes offset in struct
    NULL,  // default value
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__size_function__GetRobotState_Response__active_faults,  // size() function pointer
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__get_const_function__GetRobotState_Response__active_faults,  // get_const(index) function pointer
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__get_function__GetRobotState_Response__active_faults,  // get(index) function pointer
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__fetch_function__GetRobotState_Response__active_faults,  // fetch(index, &value) function pointer
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__assign_function__GetRobotState_Response__active_faults,  // assign(index, value) function pointer
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__resize_function__GetRobotState_Response__active_faults  // resize(index) function pointer
  }
};

static const rosidl_typesupport_introspection_c__MessageMembers amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_members = {
  "amr_msgs__srv",  // message namespace
  "GetRobotState_Response",  // message name
  2,  // number of fields
  sizeof(amr_msgs__srv__GetRobotState_Response),
  amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_member_array,  // message members
  amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_init_function,  // function to initialize message memory (memory has to be allocated)
  amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_fini_function  // function to terminate message instance (will not free memory)
};

// this is not const since it must be initialized on first access
// since C does not allow non-integral compile-time constants
static rosidl_message_type_support_t amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_type_support_handle = {
  0,
  &amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_members,
  get_message_typesupport_handle_function,
};

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_amr_msgs
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, srv, GetRobotState_Response)() {
  if (!amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_type_support_handle.typesupport_identifier) {
    amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  return &amr_msgs__srv__GetRobotState_Response__rosidl_typesupport_introspection_c__GetRobotState_Response_message_type_support_handle;
}
#ifdef __cplusplus
}
#endif

#include "rosidl_runtime_c/service_type_support_struct.h"
// already included above
// #include "amr_msgs/msg/rosidl_typesupport_introspection_c__visibility_control.h"
// already included above
// #include "amr_msgs/srv/detail/get_robot_state__rosidl_typesupport_introspection_c.h"
// already included above
// #include "rosidl_typesupport_introspection_c/identifier.h"
#include "rosidl_typesupport_introspection_c/service_introspection.h"

// this is intentionally not const to allow initialization later to prevent an initialization race
static rosidl_typesupport_introspection_c__ServiceMembers amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_service_members = {
  "amr_msgs__srv",  // service namespace
  "GetRobotState",  // service name
  // these two fields are initialized below on the first access
  NULL,  // request message
  // amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_Request_message_type_support_handle,
  NULL  // response message
  // amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_Response_message_type_support_handle
};

static rosidl_service_type_support_t amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_service_type_support_handle = {
  0,
  &amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_service_members,
  get_service_typesupport_handle_function,
};

// Forward declaration of request/response type support functions
const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, srv, GetRobotState_Request)();

const rosidl_message_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, srv, GetRobotState_Response)();

ROSIDL_TYPESUPPORT_INTROSPECTION_C_EXPORT_amr_msgs
const rosidl_service_type_support_t *
ROSIDL_TYPESUPPORT_INTERFACE__SERVICE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, srv, GetRobotState)() {
  if (!amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_service_type_support_handle.typesupport_identifier) {
    amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_service_type_support_handle.typesupport_identifier =
      rosidl_typesupport_introspection_c__identifier;
  }
  rosidl_typesupport_introspection_c__ServiceMembers * service_members =
    (rosidl_typesupport_introspection_c__ServiceMembers *)amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_service_type_support_handle.data;

  if (!service_members->request_members_) {
    service_members->request_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, srv, GetRobotState_Request)()->data;
  }
  if (!service_members->response_members_) {
    service_members->response_members_ =
      (const rosidl_typesupport_introspection_c__MessageMembers *)
      ROSIDL_TYPESUPPORT_INTERFACE__MESSAGE_SYMBOL_NAME(rosidl_typesupport_introspection_c, amr_msgs, srv, GetRobotState_Response)()->data;
  }

  return &amr_msgs__srv__detail__get_robot_state__rosidl_typesupport_introspection_c__GetRobotState_service_type_support_handle;
}
