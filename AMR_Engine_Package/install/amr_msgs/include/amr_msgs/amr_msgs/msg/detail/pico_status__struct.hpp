// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:msg/PicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__PICO_STATUS__STRUCT_HPP_
#define AMR_MSGS__MSG__DETAIL__PICO_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


// Include directives for member types
// Member 'header'
#include "std_msgs/msg/detail/header__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__amr_msgs__msg__PicoStatus __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__msg__PicoStatus __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct PicoStatus_
{
  using Type = PicoStatus_<ContainerAllocator>;

  explicit PicoStatus_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->uptime_ms = 0ul;
      this->last_rpi_msg_age_ms = 0ul;
      this->watchdog_resets = 0ul;
      this->free_mem_bytes = 0ul;
    }
  }

  explicit PicoStatus_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->uptime_ms = 0ul;
      this->last_rpi_msg_age_ms = 0ul;
      this->watchdog_resets = 0ul;
      this->free_mem_bytes = 0ul;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _uptime_ms_type =
    uint32_t;
  _uptime_ms_type uptime_ms;
  using _last_rpi_msg_age_ms_type =
    uint32_t;
  _last_rpi_msg_age_ms_type last_rpi_msg_age_ms;
  using _watchdog_resets_type =
    uint32_t;
  _watchdog_resets_type watchdog_resets;
  using _free_mem_bytes_type =
    uint32_t;
  _free_mem_bytes_type free_mem_bytes;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__uptime_ms(
    const uint32_t & _arg)
  {
    this->uptime_ms = _arg;
    return *this;
  }
  Type & set__last_rpi_msg_age_ms(
    const uint32_t & _arg)
  {
    this->last_rpi_msg_age_ms = _arg;
    return *this;
  }
  Type & set__watchdog_resets(
    const uint32_t & _arg)
  {
    this->watchdog_resets = _arg;
    return *this;
  }
  Type & set__free_mem_bytes(
    const uint32_t & _arg)
  {
    this->free_mem_bytes = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::msg::PicoStatus_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::msg::PicoStatus_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::PicoStatus_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::PicoStatus_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__msg__PicoStatus
    std::shared_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__msg__PicoStatus
    std::shared_ptr<amr_msgs::msg::PicoStatus_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const PicoStatus_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->uptime_ms != other.uptime_ms) {
      return false;
    }
    if (this->last_rpi_msg_age_ms != other.last_rpi_msg_age_ms) {
      return false;
    }
    if (this->watchdog_resets != other.watchdog_resets) {
      return false;
    }
    if (this->free_mem_bytes != other.free_mem_bytes) {
      return false;
    }
    return true;
  }
  bool operator!=(const PicoStatus_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct PicoStatus_

// alias to use template instance with default allocator
using PicoStatus =
  amr_msgs::msg::PicoStatus_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__PICO_STATUS__STRUCT_HPP_
