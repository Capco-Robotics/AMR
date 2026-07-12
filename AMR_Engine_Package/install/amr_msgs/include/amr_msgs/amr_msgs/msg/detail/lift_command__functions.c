// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from amr_msgs:msg/LiftCommand.idl
// generated code does not contain a copyright notice
#include "amr_msgs/msg/detail/lift_command__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
amr_msgs__msg__LiftCommand__init(amr_msgs__msg__LiftCommand * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    amr_msgs__msg__LiftCommand__fini(msg);
    return false;
  }
  // target_position
  return true;
}

void
amr_msgs__msg__LiftCommand__fini(amr_msgs__msg__LiftCommand * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // target_position
}

bool
amr_msgs__msg__LiftCommand__are_equal(const amr_msgs__msg__LiftCommand * lhs, const amr_msgs__msg__LiftCommand * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__are_equal(
      &(lhs->header), &(rhs->header)))
  {
    return false;
  }
  // target_position
  if (lhs->target_position != rhs->target_position) {
    return false;
  }
  return true;
}

bool
amr_msgs__msg__LiftCommand__copy(
  const amr_msgs__msg__LiftCommand * input,
  amr_msgs__msg__LiftCommand * output)
{
  if (!input || !output) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__copy(
      &(input->header), &(output->header)))
  {
    return false;
  }
  // target_position
  output->target_position = input->target_position;
  return true;
}

amr_msgs__msg__LiftCommand *
amr_msgs__msg__LiftCommand__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__LiftCommand * msg = (amr_msgs__msg__LiftCommand *)allocator.allocate(sizeof(amr_msgs__msg__LiftCommand), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(amr_msgs__msg__LiftCommand));
  bool success = amr_msgs__msg__LiftCommand__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
amr_msgs__msg__LiftCommand__destroy(amr_msgs__msg__LiftCommand * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    amr_msgs__msg__LiftCommand__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
amr_msgs__msg__LiftCommand__Sequence__init(amr_msgs__msg__LiftCommand__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__LiftCommand * data = NULL;

  if (size) {
    data = (amr_msgs__msg__LiftCommand *)allocator.zero_allocate(size, sizeof(amr_msgs__msg__LiftCommand), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = amr_msgs__msg__LiftCommand__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        amr_msgs__msg__LiftCommand__fini(&data[i - 1]);
      }
      allocator.deallocate(data, allocator.state);
      return false;
    }
  }
  array->data = data;
  array->size = size;
  array->capacity = size;
  return true;
}

void
amr_msgs__msg__LiftCommand__Sequence__fini(amr_msgs__msg__LiftCommand__Sequence * array)
{
  if (!array) {
    return;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();

  if (array->data) {
    // ensure that data and capacity values are consistent
    assert(array->capacity > 0);
    // finalize all array elements
    for (size_t i = 0; i < array->capacity; ++i) {
      amr_msgs__msg__LiftCommand__fini(&array->data[i]);
    }
    allocator.deallocate(array->data, allocator.state);
    array->data = NULL;
    array->size = 0;
    array->capacity = 0;
  } else {
    // ensure that data, size, and capacity values are consistent
    assert(0 == array->size);
    assert(0 == array->capacity);
  }
}

amr_msgs__msg__LiftCommand__Sequence *
amr_msgs__msg__LiftCommand__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__LiftCommand__Sequence * array = (amr_msgs__msg__LiftCommand__Sequence *)allocator.allocate(sizeof(amr_msgs__msg__LiftCommand__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = amr_msgs__msg__LiftCommand__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
amr_msgs__msg__LiftCommand__Sequence__destroy(amr_msgs__msg__LiftCommand__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    amr_msgs__msg__LiftCommand__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
amr_msgs__msg__LiftCommand__Sequence__are_equal(const amr_msgs__msg__LiftCommand__Sequence * lhs, const amr_msgs__msg__LiftCommand__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!amr_msgs__msg__LiftCommand__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
amr_msgs__msg__LiftCommand__Sequence__copy(
  const amr_msgs__msg__LiftCommand__Sequence * input,
  amr_msgs__msg__LiftCommand__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(amr_msgs__msg__LiftCommand);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    amr_msgs__msg__LiftCommand * data =
      (amr_msgs__msg__LiftCommand *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!amr_msgs__msg__LiftCommand__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          amr_msgs__msg__LiftCommand__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!amr_msgs__msg__LiftCommand__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
