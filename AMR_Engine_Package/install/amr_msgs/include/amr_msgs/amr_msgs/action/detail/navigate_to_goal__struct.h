// generated from rosidl_generator_c/resource/idl__struct.h.em
// with input from amr_msgs:action/NavigateToGoal.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__ACTION__DETAIL__NAVIGATE_TO_GOAL__STRUCT_H_
#define AMR_MSGS__ACTION__DETAIL__NAVIGATE_TO_GOAL__STRUCT_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stddef.h>
#include <stdint.h>


// Constants defined in the message

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_Goal
{
  float goal_x;
  float goal_y;
  float goal_theta;
} amr_msgs__action__NavigateToGoal_Goal;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_Goal.
typedef struct amr_msgs__action__NavigateToGoal_Goal__Sequence
{
  amr_msgs__action__NavigateToGoal_Goal * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_Goal__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'outcome'
#include "rosidl_runtime_c/string.h"

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_Result
{
  bool success;
  rosidl_runtime_c__String outcome;
} amr_msgs__action__NavigateToGoal_Result;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_Result.
typedef struct amr_msgs__action__NavigateToGoal_Result__Sequence
{
  amr_msgs__action__NavigateToGoal_Result * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_Result__Sequence;


// Constants defined in the message

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_Feedback
{
  float current_x;
  float current_y;
  float distance_remaining;
} amr_msgs__action__NavigateToGoal_Feedback;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_Feedback.
typedef struct amr_msgs__action__NavigateToGoal_Feedback__Sequence
{
  amr_msgs__action__NavigateToGoal_Feedback * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_Feedback__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'goal'
#include "amr_msgs/action/detail/navigate_to_goal__struct.h"

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_SendGoal_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
  amr_msgs__action__NavigateToGoal_Goal goal;
} amr_msgs__action__NavigateToGoal_SendGoal_Request;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_SendGoal_Request.
typedef struct amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence
{
  amr_msgs__action__NavigateToGoal_SendGoal_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.h"

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_SendGoal_Response
{
  bool accepted;
  builtin_interfaces__msg__Time stamp;
} amr_msgs__action__NavigateToGoal_SendGoal_Response;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_SendGoal_Response.
typedef struct amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence
{
  amr_msgs__action__NavigateToGoal_SendGoal_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_GetResult_Request
{
  unique_identifier_msgs__msg__UUID goal_id;
} amr_msgs__action__NavigateToGoal_GetResult_Request;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_GetResult_Request.
typedef struct amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence
{
  amr_msgs__action__NavigateToGoal_GetResult_Request * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'result'
// already included above
// #include "amr_msgs/action/detail/navigate_to_goal__struct.h"

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_GetResult_Response
{
  int8_t status;
  amr_msgs__action__NavigateToGoal_Result result;
} amr_msgs__action__NavigateToGoal_GetResult_Response;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_GetResult_Response.
typedef struct amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence
{
  amr_msgs__action__NavigateToGoal_GetResult_Response * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence;


// Constants defined in the message

// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.h"
// Member 'feedback'
// already included above
// #include "amr_msgs/action/detail/navigate_to_goal__struct.h"

/// Struct defined in action/NavigateToGoal in the package amr_msgs.
typedef struct amr_msgs__action__NavigateToGoal_FeedbackMessage
{
  unique_identifier_msgs__msg__UUID goal_id;
  amr_msgs__action__NavigateToGoal_Feedback feedback;
} amr_msgs__action__NavigateToGoal_FeedbackMessage;

// Struct for a sequence of amr_msgs__action__NavigateToGoal_FeedbackMessage.
typedef struct amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence
{
  amr_msgs__action__NavigateToGoal_FeedbackMessage * data;
  /// The number of valid items in data
  size_t size;
  /// The number of allocated items in data
  size_t capacity;
} amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence;

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__ACTION__DETAIL__NAVIGATE_TO_GOAL__STRUCT_H_
