// generated from rosidl_generator_c/resource/idl__functions.h.em
// with input from amr_msgs:msg/LiftCommand.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__FUNCTIONS_H_
#define AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__FUNCTIONS_H_

#ifdef __cplusplus
extern "C"
{
#endif

#include <stdbool.h>
#include <stdlib.h>

#include "rosidl_runtime_c/visibility_control.h"
#include "amr_msgs/msg/rosidl_generator_c__visibility_control.h"

#include "amr_msgs/msg/detail/lift_command__struct.h"

/// Initialize msg/LiftCommand message.
/**
 * If the init function is called twice for the same message without
 * calling fini inbetween previously allocated memory will be leaked.
 * \param[in,out] msg The previously allocated message pointer.
 * Fields without a default value will not be initialized by this function.
 * You might want to call memset(msg, 0, sizeof(
 * amr_msgs__msg__LiftCommand
 * )) before or use
 * amr_msgs__msg__LiftCommand__create()
 * to allocate and initialize the message.
 * \return true if initialization was successful, otherwise false
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__LiftCommand__init(amr_msgs__msg__LiftCommand * msg);

/// Finalize msg/LiftCommand message.
/**
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__LiftCommand__fini(amr_msgs__msg__LiftCommand * msg);

/// Create msg/LiftCommand message.
/**
 * It allocates the memory for the message, sets the memory to zero, and
 * calls
 * amr_msgs__msg__LiftCommand__init().
 * \return The pointer to the initialized message if successful,
 * otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
amr_msgs__msg__LiftCommand *
amr_msgs__msg__LiftCommand__create();

/// Destroy msg/LiftCommand message.
/**
 * It calls
 * amr_msgs__msg__LiftCommand__fini()
 * and frees the memory of the message.
 * \param[in,out] msg The allocated message pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__LiftCommand__destroy(amr_msgs__msg__LiftCommand * msg);

/// Check for msg/LiftCommand message equality.
/**
 * \param[in] lhs The message on the left hand size of the equality operator.
 * \param[in] rhs The message on the right hand size of the equality operator.
 * \return true if messages are equal, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__LiftCommand__are_equal(const amr_msgs__msg__LiftCommand * lhs, const amr_msgs__msg__LiftCommand * rhs);

/// Copy a msg/LiftCommand message.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source message pointer.
 * \param[out] output The target message pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer is null
 *   or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__LiftCommand__copy(
  const amr_msgs__msg__LiftCommand * input,
  amr_msgs__msg__LiftCommand * output);

/// Initialize array of msg/LiftCommand messages.
/**
 * It allocates the memory for the number of elements and calls
 * amr_msgs__msg__LiftCommand__init()
 * for each element of the array.
 * \param[in,out] array The allocated array pointer.
 * \param[in] size The size / capacity of the array.
 * \return true if initialization was successful, otherwise false
 * If the array pointer is valid and the size is zero it is guaranteed
 # to return true.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__LiftCommand__Sequence__init(amr_msgs__msg__LiftCommand__Sequence * array, size_t size);

/// Finalize array of msg/LiftCommand messages.
/**
 * It calls
 * amr_msgs__msg__LiftCommand__fini()
 * for each element of the array and frees the memory for the number of
 * elements.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__LiftCommand__Sequence__fini(amr_msgs__msg__LiftCommand__Sequence * array);

/// Create array of msg/LiftCommand messages.
/**
 * It allocates the memory for the array and calls
 * amr_msgs__msg__LiftCommand__Sequence__init().
 * \param[in] size The size / capacity of the array.
 * \return The pointer to the initialized array if successful, otherwise NULL
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
amr_msgs__msg__LiftCommand__Sequence *
amr_msgs__msg__LiftCommand__Sequence__create(size_t size);

/// Destroy array of msg/LiftCommand messages.
/**
 * It calls
 * amr_msgs__msg__LiftCommand__Sequence__fini()
 * on the array,
 * and frees the memory of the array.
 * \param[in,out] array The initialized array pointer.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
void
amr_msgs__msg__LiftCommand__Sequence__destroy(amr_msgs__msg__LiftCommand__Sequence * array);

/// Check for msg/LiftCommand message array equality.
/**
 * \param[in] lhs The message array on the left hand size of the equality operator.
 * \param[in] rhs The message array on the right hand size of the equality operator.
 * \return true if message arrays are equal in size and content, otherwise false.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__LiftCommand__Sequence__are_equal(const amr_msgs__msg__LiftCommand__Sequence * lhs, const amr_msgs__msg__LiftCommand__Sequence * rhs);

/// Copy an array of msg/LiftCommand messages.
/**
 * This functions performs a deep copy, as opposed to the shallow copy that
 * plain assignment yields.
 *
 * \param[in] input The source array pointer.
 * \param[out] output The target array pointer, which must
 *   have been initialized before calling this function.
 * \return true if successful, or false if either pointer
 *   is null or memory allocation fails.
 */
ROSIDL_GENERATOR_C_PUBLIC_amr_msgs
bool
amr_msgs__msg__LiftCommand__Sequence__copy(
  const amr_msgs__msg__LiftCommand__Sequence * input,
  amr_msgs__msg__LiftCommand__Sequence * output);

#ifdef __cplusplus
}
#endif

#endif  // AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__FUNCTIONS_H_
