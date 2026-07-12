// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:action/MoveLift.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__STRUCT_H_
#define AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_Goal
{
  float target_position;
} amr_msgs__action__MoveLift_Goal;

// Struct for a sequence of amr_msgs__action__MoveLift_Goal.
typedef struct amr_msgs__action__MoveLift_Goal__Sequence
{
  amr_msgs__action__MoveLift_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_Goal__Sequence;


// Constants defined in the message

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_Result
{
  bool success;
  float final_position;
} amr_msgs__action__MoveLift_Result;

// Struct for a sequence of amr_msgs__action__MoveLift_Result.
typedef struct amr_msgs__action__MoveLift_Result__Sequence
{
  amr_msgs__action__MoveLift_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_Feedback
{
  float current_position;
  bool limit_upper;
  bool limit_lower;
} amr_msgs__action__MoveLift_Feedback;

// Struct for a sequence of amr_msgs__action__MoveLift_Feedback.
typedef struct amr_msgs__action__MoveLift_Feedback__Sequence
{
  amr_msgs__action__MoveLift_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "amr_msgs/action/detail/move_lift__struct.h"

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  amr_msgs__action__MoveLift_Goal goal;
} amr_msgs__action__MoveLift_SendGoal_Request;

// Struct for a sequence of amr_msgs__action__MoveLift_SendGoal_Request.
typedef struct amr_msgs__action__MoveLift_SendGoal_Request__Sequence
{
  amr_msgs__action__MoveLift_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} amr_msgs__action__MoveLift_SendGoal_Response;

// Struct for a sequence of amr_msgs__action__MoveLift_SendGoal_Response.
typedef struct amr_msgs__action__MoveLift_SendGoal_Response__Sequence
{
  amr_msgs__action__MoveLift_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} amr_msgs__action__MoveLift_GetResult_Request;

// Struct for a sequence of amr_msgs__action__MoveLift_GetResult_Request.
typedef struct amr_msgs__action__MoveLift_GetResult_Request__Sequence
{
  amr_msgs__action__MoveLift_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "amr_msgs/action/detail/move_lift__struct.h"

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_GetResult_Response
{
  int8_t status;
  amr_msgs__action__MoveLift_Result result;
} amr_msgs__action__MoveLift_GetResult_Response;

// Struct for a sequence of amr_msgs__action__MoveLift_GetResult_Response.
typedef struct amr_msgs__action__MoveLift_GetResult_Response__Sequence
{
  amr_msgs__action__MoveLift_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "amr_msgs/action/detail/move_lift__struct.h"

/// Struct defined in action/MoveLift in the package amr_msgs.
typedef struct amr_msgs__action__MoveLift_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  amr_msgs__action__MoveLift_Feedback feedback;
} amr_msgs__action__MoveLift_FeedbackMessage;

// Struct for a sequence of amr_msgs__action__MoveLift_FeedbackMessage.
typedef struct amr_msgs__action__MoveLift_FeedbackMessage__Sequence
{
  amr_msgs__action__MoveLift_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__MoveLift_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__STRUCT_H_
