// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from amr_msgs:msg/LiftState.idl
// generated code does not contain a copyright notice
#include "amr_msgs/msg/detail/lift_state__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
amr_msgs__msg__LiftState__init(amr_msgs__msg__LiftState * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    amr_msgs__msg__LiftState__fini(msg);
    return false;
  }
  // position
  // limit_upper
  // limit_lower
  return true;
}

void
amr_msgs__msg__LiftState__fini(amr_msgs__msg__LiftState * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // position
  // limit_upper
  // limit_lower
}

bool
amr_msgs__msg__LiftState__are_equal(const amr_msgs__msg__LiftState * lhs, const amr_msgs__msg__LiftState * rhs)
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
  // position
  if (lhs->position != rhs->position) {
    return false;
  }
  // limit_upper
  if (lhs->limit_upper != rhs->limit_upper) {
    return false;
  }
  // limit_lower
  if (lhs->limit_lower != rhs->limit_lower) {
    return false;
  }
  return true;
}

bool
amr_msgs__msg__LiftState__copy(
  const amr_msgs__msg__LiftState * input,
  amr_msgs__msg__LiftState * output)
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
  // position
  output->position = input->position;
  // limit_upper
  output->limit_upper = input->limit_upper;
  // limit_lower
  output->limit_lower = input->limit_lower;
  return true;
}

amr_msgs__msg__LiftState *
amr_msgs__msg__LiftState__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__LiftState * msg = (amr_msgs__msg__LiftState *)allocator.allocate(sizeof(amr_msgs__msg__LiftState), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(amr_msgs__msg__LiftState));
  bool success = amr_msgs__msg__LiftState__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
amr_msgs__msg__LiftState__destroy(amr_msgs__msg__LiftState * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    amr_msgs__msg__LiftState__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
amr_msgs__msg__LiftState__Sequence__init(amr_msgs__msg__LiftState__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__LiftState * data = NULL;

  if (size) {
    data = (amr_msgs__msg__LiftState *)allocator.zero_allocate(size, sizeof(amr_msgs__msg__LiftState), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = amr_msgs__msg__LiftState__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        amr_msgs__msg__LiftState__fini(&data[i - 1]);
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
amr_msgs__msg__LiftState__Sequence__fini(amr_msgs__msg__LiftState__Sequence * array)
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
      amr_msgs__msg__LiftState__fini(&array->data[i]);
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

amr_msgs__msg__LiftState__Sequence *
amr_msgs__msg__LiftState__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__LiftState__Sequence * array = (amr_msgs__msg__LiftState__Sequence *)allocator.allocate(sizeof(amr_msgs__msg__LiftState__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = amr_msgs__msg__LiftState__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
amr_msgs__msg__LiftState__Sequence__destroy(amr_msgs__msg__LiftState__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    amr_msgs__msg__LiftState__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
amr_msgs__msg__LiftState__Sequence__are_equal(const amr_msgs__msg__LiftState__Sequence * lhs, const amr_msgs__msg__LiftState__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!amr_msgs__msg__LiftState__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
amr_msgs__msg__LiftState__Sequence__copy(
  const amr_msgs__msg__LiftState__Sequence * input,
  amr_msgs__msg__LiftState__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(amr_msgs__msg__LiftState);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    amr_msgs__msg__LiftState * data =
      (amr_msgs__msg__LiftState *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!amr_msgs__msg__LiftState__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          amr_msgs__msg__LiftState__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!amr_msgs__msg__LiftState__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
