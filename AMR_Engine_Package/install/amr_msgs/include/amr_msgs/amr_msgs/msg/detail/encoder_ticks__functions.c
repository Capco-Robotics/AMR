// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from amr_msgs:msg/EncoderTicks.idl
// generated code does not contain a copyright notice
#include "amr_msgs/msg/detail/encoder_ticks__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"


// Include directives for member types
// Member `header`
#include "std_msgs/msg/detail/header__functions.h"

bool
amr_msgs__msg__EncoderTicks__init(amr_msgs__msg__EncoderTicks * msg)
{
  if (!msg) {
    return false;
  }
  // header
  if (!std_msgs__msg__Header__init(&msg->header)) {
    amr_msgs__msg__EncoderTicks__fini(msg);
    return false;
  }
  // left_ticks
  // right_ticks
  // dt_ms
  return true;
}

void
amr_msgs__msg__EncoderTicks__fini(amr_msgs__msg__EncoderTicks * msg)
{
  if (!msg) {
    return;
  }
  // header
  std_msgs__msg__Header__fini(&msg->header);
  // left_ticks
  // right_ticks
  // dt_ms
}

bool
amr_msgs__msg__EncoderTicks__are_equal(const amr_msgs__msg__EncoderTicks * lhs, const amr_msgs__msg__EncoderTicks * rhs)
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
  // left_ticks
  if (lhs->left_ticks != rhs->left_ticks) {
    return false;
  }
  // right_ticks
  if (lhs->right_ticks != rhs->right_ticks) {
    return false;
  }
  // dt_ms
  if (lhs->dt_ms != rhs->dt_ms) {
    return false;
  }
  return true;
}

bool
amr_msgs__msg__EncoderTicks__copy(
  const amr_msgs__msg__EncoderTicks * input,
  amr_msgs__msg__EncoderTicks * output)
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
  // left_ticks
  output->left_ticks = input->left_ticks;
  // right_ticks
  output->right_ticks = input->right_ticks;
  // dt_ms
  output->dt_ms = input->dt_ms;
  return true;
}

amr_msgs__msg__EncoderTicks *
amr_msgs__msg__EncoderTicks__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__EncoderTicks * msg = (amr_msgs__msg__EncoderTicks *)allocator.allocate(sizeof(amr_msgs__msg__EncoderTicks), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(amr_msgs__msg__EncoderTicks));
  bool success = amr_msgs__msg__EncoderTicks__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
amr_msgs__msg__EncoderTicks__destroy(amr_msgs__msg__EncoderTicks * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    amr_msgs__msg__EncoderTicks__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
amr_msgs__msg__EncoderTicks__Sequence__init(amr_msgs__msg__EncoderTicks__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__EncoderTicks * data = NULL;

  if (size) {
    data = (amr_msgs__msg__EncoderTicks *)allocator.zero_allocate(size, sizeof(amr_msgs__msg__EncoderTicks), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = amr_msgs__msg__EncoderTicks__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        amr_msgs__msg__EncoderTicks__fini(&data[i - 1]);
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
amr_msgs__msg__EncoderTicks__Sequence__fini(amr_msgs__msg__EncoderTicks__Sequence * array)
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
      amr_msgs__msg__EncoderTicks__fini(&array->data[i]);
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

amr_msgs__msg__EncoderTicks__Sequence *
amr_msgs__msg__EncoderTicks__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__msg__EncoderTicks__Sequence * array = (amr_msgs__msg__EncoderTicks__Sequence *)allocator.allocate(sizeof(amr_msgs__msg__EncoderTicks__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = amr_msgs__msg__EncoderTicks__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
amr_msgs__msg__EncoderTicks__Sequence__destroy(amr_msgs__msg__EncoderTicks__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    amr_msgs__msg__EncoderTicks__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
amr_msgs__msg__EncoderTicks__Sequence__are_equal(const amr_msgs__msg__EncoderTicks__Sequence * lhs, const amr_msgs__msg__EncoderTicks__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!amr_msgs__msg__EncoderTicks__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
amr_msgs__msg__EncoderTicks__Sequence__copy(
  const amr_msgs__msg__EncoderTicks__Sequence * input,
  amr_msgs__msg__EncoderTicks__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(amr_msgs__msg__EncoderTicks);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    amr_msgs__msg__EncoderTicks * data =
      (amr_msgs__msg__EncoderTicks *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!amr_msgs__msg__EncoderTicks__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          amr_msgs__msg__EncoderTicks__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!amr_msgs__msg__EncoderTicks__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
