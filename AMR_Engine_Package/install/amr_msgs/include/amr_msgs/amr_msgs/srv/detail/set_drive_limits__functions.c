// generated from rosidl_generator_c/resource/idl__functions.c.em
// with input from amr_msgs:srv/SetDriveLimits.idl
// generated code does not contain a copyright notice
#include "amr_msgs/srv/detail/set_drive_limits__functions.h"

#include <assert.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

#include "rcutils/allocator.h"

bool
amr_msgs__srv__SetDriveLimits_Request__init(amr_msgs__srv__SetDriveLimits_Request * msg)
{
  if (!msg) {
    return false;
  }
  // max_linear_mps
  // max_angular_rps
  return true;
}

void
amr_msgs__srv__SetDriveLimits_Request__fini(amr_msgs__srv__SetDriveLimits_Request * msg)
{
  if (!msg) {
    return;
  }
  // max_linear_mps
  // max_angular_rps
}

bool
amr_msgs__srv__SetDriveLimits_Request__are_equal(const amr_msgs__srv__SetDriveLimits_Request * lhs, const amr_msgs__srv__SetDriveLimits_Request * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // max_linear_mps
  if (lhs->max_linear_mps != rhs->max_linear_mps) {
    return false;
  }
  // max_angular_rps
  if (lhs->max_angular_rps != rhs->max_angular_rps) {
    return false;
  }
  return true;
}

bool
amr_msgs__srv__SetDriveLimits_Request__copy(
  const amr_msgs__srv__SetDriveLimits_Request * input,
  amr_msgs__srv__SetDriveLimits_Request * output)
{
  if (!input || !output) {
    return false;
  }
  // max_linear_mps
  output->max_linear_mps = input->max_linear_mps;
  // max_angular_rps
  output->max_angular_rps = input->max_angular_rps;
  return true;
}

amr_msgs__srv__SetDriveLimits_Request *
amr_msgs__srv__SetDriveLimits_Request__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__srv__SetDriveLimits_Request * msg = (amr_msgs__srv__SetDriveLimits_Request *)allocator.allocate(sizeof(amr_msgs__srv__SetDriveLimits_Request), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(amr_msgs__srv__SetDriveLimits_Request));
  bool success = amr_msgs__srv__SetDriveLimits_Request__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
amr_msgs__srv__SetDriveLimits_Request__destroy(amr_msgs__srv__SetDriveLimits_Request * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    amr_msgs__srv__SetDriveLimits_Request__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
amr_msgs__srv__SetDriveLimits_Request__Sequence__init(amr_msgs__srv__SetDriveLimits_Request__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__srv__SetDriveLimits_Request * data = NULL;

  if (size) {
    data = (amr_msgs__srv__SetDriveLimits_Request *)allocator.zero_allocate(size, sizeof(amr_msgs__srv__SetDriveLimits_Request), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = amr_msgs__srv__SetDriveLimits_Request__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        amr_msgs__srv__SetDriveLimits_Request__fini(&data[i - 1]);
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
amr_msgs__srv__SetDriveLimits_Request__Sequence__fini(amr_msgs__srv__SetDriveLimits_Request__Sequence * array)
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
      amr_msgs__srv__SetDriveLimits_Request__fini(&array->data[i]);
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

amr_msgs__srv__SetDriveLimits_Request__Sequence *
amr_msgs__srv__SetDriveLimits_Request__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__srv__SetDriveLimits_Request__Sequence * array = (amr_msgs__srv__SetDriveLimits_Request__Sequence *)allocator.allocate(sizeof(amr_msgs__srv__SetDriveLimits_Request__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = amr_msgs__srv__SetDriveLimits_Request__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
amr_msgs__srv__SetDriveLimits_Request__Sequence__destroy(amr_msgs__srv__SetDriveLimits_Request__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    amr_msgs__srv__SetDriveLimits_Request__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
amr_msgs__srv__SetDriveLimits_Request__Sequence__are_equal(const amr_msgs__srv__SetDriveLimits_Request__Sequence * lhs, const amr_msgs__srv__SetDriveLimits_Request__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!amr_msgs__srv__SetDriveLimits_Request__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
amr_msgs__srv__SetDriveLimits_Request__Sequence__copy(
  const amr_msgs__srv__SetDriveLimits_Request__Sequence * input,
  amr_msgs__srv__SetDriveLimits_Request__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(amr_msgs__srv__SetDriveLimits_Request);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    amr_msgs__srv__SetDriveLimits_Request * data =
      (amr_msgs__srv__SetDriveLimits_Request *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!amr_msgs__srv__SetDriveLimits_Request__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          amr_msgs__srv__SetDriveLimits_Request__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!amr_msgs__srv__SetDriveLimits_Request__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}


bool
amr_msgs__srv__SetDriveLimits_Response__init(amr_msgs__srv__SetDriveLimits_Response * msg)
{
  if (!msg) {
    return false;
  }
  // accepted
  return true;
}

void
amr_msgs__srv__SetDriveLimits_Response__fini(amr_msgs__srv__SetDriveLimits_Response * msg)
{
  if (!msg) {
    return;
  }
  // accepted
}

bool
amr_msgs__srv__SetDriveLimits_Response__are_equal(const amr_msgs__srv__SetDriveLimits_Response * lhs, const amr_msgs__srv__SetDriveLimits_Response * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  // accepted
  if (lhs->accepted != rhs->accepted) {
    return false;
  }
  return true;
}

bool
amr_msgs__srv__SetDriveLimits_Response__copy(
  const amr_msgs__srv__SetDriveLimits_Response * input,
  amr_msgs__srv__SetDriveLimits_Response * output)
{
  if (!input || !output) {
    return false;
  }
  // accepted
  output->accepted = input->accepted;
  return true;
}

amr_msgs__srv__SetDriveLimits_Response *
amr_msgs__srv__SetDriveLimits_Response__create()
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__srv__SetDriveLimits_Response * msg = (amr_msgs__srv__SetDriveLimits_Response *)allocator.allocate(sizeof(amr_msgs__srv__SetDriveLimits_Response), allocator.state);
  if (!msg) {
    return NULL;
  }
  memset(msg, 0, sizeof(amr_msgs__srv__SetDriveLimits_Response));
  bool success = amr_msgs__srv__SetDriveLimits_Response__init(msg);
  if (!success) {
    allocator.deallocate(msg, allocator.state);
    return NULL;
  }
  return msg;
}

void
amr_msgs__srv__SetDriveLimits_Response__destroy(amr_msgs__srv__SetDriveLimits_Response * msg)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (msg) {
    amr_msgs__srv__SetDriveLimits_Response__fini(msg);
  }
  allocator.deallocate(msg, allocator.state);
}


bool
amr_msgs__srv__SetDriveLimits_Response__Sequence__init(amr_msgs__srv__SetDriveLimits_Response__Sequence * array, size_t size)
{
  if (!array) {
    return false;
  }
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__srv__SetDriveLimits_Response * data = NULL;

  if (size) {
    data = (amr_msgs__srv__SetDriveLimits_Response *)allocator.zero_allocate(size, sizeof(amr_msgs__srv__SetDriveLimits_Response), allocator.state);
    if (!data) {
      return false;
    }
    // initialize all array elements
    size_t i;
    for (i = 0; i < size; ++i) {
      bool success = amr_msgs__srv__SetDriveLimits_Response__init(&data[i]);
      if (!success) {
        break;
      }
    }
    if (i < size) {
      // if initialization failed finalize the already initialized array elements
      for (; i > 0; --i) {
        amr_msgs__srv__SetDriveLimits_Response__fini(&data[i - 1]);
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
amr_msgs__srv__SetDriveLimits_Response__Sequence__fini(amr_msgs__srv__SetDriveLimits_Response__Sequence * array)
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
      amr_msgs__srv__SetDriveLimits_Response__fini(&array->data[i]);
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

amr_msgs__srv__SetDriveLimits_Response__Sequence *
amr_msgs__srv__SetDriveLimits_Response__Sequence__create(size_t size)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  amr_msgs__srv__SetDriveLimits_Response__Sequence * array = (amr_msgs__srv__SetDriveLimits_Response__Sequence *)allocator.allocate(sizeof(amr_msgs__srv__SetDriveLimits_Response__Sequence), allocator.state);
  if (!array) {
    return NULL;
  }
  bool success = amr_msgs__srv__SetDriveLimits_Response__Sequence__init(array, size);
  if (!success) {
    allocator.deallocate(array, allocator.state);
    return NULL;
  }
  return array;
}

void
amr_msgs__srv__SetDriveLimits_Response__Sequence__destroy(amr_msgs__srv__SetDriveLimits_Response__Sequence * array)
{
  rcutils_allocator_t allocator = rcutils_get_default_allocator();
  if (array) {
    amr_msgs__srv__SetDriveLimits_Response__Sequence__fini(array);
  }
  allocator.deallocate(array, allocator.state);
}

bool
amr_msgs__srv__SetDriveLimits_Response__Sequence__are_equal(const amr_msgs__srv__SetDriveLimits_Response__Sequence * lhs, const amr_msgs__srv__SetDriveLimits_Response__Sequence * rhs)
{
  if (!lhs || !rhs) {
    return false;
  }
  if (lhs->size != rhs->size) {
    return false;
  }
  for (size_t i = 0; i < lhs->size; ++i) {
    if (!amr_msgs__srv__SetDriveLimits_Response__are_equal(&(lhs->data[i]), &(rhs->data[i]))) {
      return false;
    }
  }
  return true;
}

bool
amr_msgs__srv__SetDriveLimits_Response__Sequence__copy(
  const amr_msgs__srv__SetDriveLimits_Response__Sequence * input,
  amr_msgs__srv__SetDriveLimits_Response__Sequence * output)
{
  if (!input || !output) {
    return false;
  }
  if (output->capacity < input->size) {
    const size_t allocation_size =
      input->size * sizeof(amr_msgs__srv__SetDriveLimits_Response);
    rcutils_allocator_t allocator = rcutils_get_default_allocator();
    amr_msgs__srv__SetDriveLimits_Response * data =
      (amr_msgs__srv__SetDriveLimits_Response *)allocator.reallocate(
      output->data, allocation_size, allocator.state);
    if (!data) {
      return false;
    }
    // If reallocation succeeded, memory may or may not have been moved
    // to fulfill the allocation request, invalidating output->data.
    output->data = data;
    for (size_t i = output->capacity; i < input->size; ++i) {
      if (!amr_msgs__srv__SetDriveLimits_Response__init(&output->data[i])) {
        // If initialization of any new item fails, roll back
        // all previously initialized items. Existing items
        // in output are to be left unmodified.
        for (; i-- > output->capacity; ) {
          amr_msgs__srv__SetDriveLimits_Response__fini(&output->data[i]);
        }
        return false;
      }
    }
    output->capacity = input->size;
  }
  output->size = input->size;
  for (size_t i = 0; i < input->size; ++i) {
    if (!amr_msgs__srv__SetDriveLimits_Response__copy(
        &(input->data[i]), &(output->data[i])))
    {
      return false;
    }
  }
  return true;
}
