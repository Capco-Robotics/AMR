// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:msg/FaultCodes.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__FAULT_CODES__STRUCT_HPP_
#define AMR_MSGS__MSG__DETAIL__FAULT_CODES__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__msg__FaultCodes __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__msg__FaultCodes __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct FaultCodes_
{
  using Type = FaultCodes_<ContainerAllocator>;

  explicit FaultCodes_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit FaultCodes_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  // field types and members
  using _structure_needs_at_least_one_member_type =
    uint8_t;
  _structure_needs_at_least_one_member_type structure_needs_at_least_one_member;


  // constant declarations
  static constexpr uint8_t NONE =
    0u;
  static constexpr uint8_t LIFT_OVERCURRENT =
    1u;
  static constexpr uint8_t LIFT_UNDERCURRENT =
    2u;
  static constexpr uint8_t LIFT_SLANT =
    3u;
  static constexpr uint8_t LIFT_LIMIT_SWITCH =
    4u;
  static constexpr uint8_t LIFT_SENSOR_FAILURE =
    5u;
  static constexpr uint8_t LIFT_TIMEOUT =
    6u;

  // pointer types
  using RawPtr =
    amr_msgs::msg::FaultCodes_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::msg::FaultCodes_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::FaultCodes_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::FaultCodes_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__msg__FaultCodes
    std::shared_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__msg__FaultCodes
    std::shared_ptr<amr_msgs::msg::FaultCodes_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const FaultCodes_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const FaultCodes_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct FaultCodes_

// alias to use template instance with default allocator
using FaultCodes =
  amr_msgs::msg::FaultCodes_<std::allocator<void>>;

// constant definitions
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t FaultCodes_<ContainerAllocator>::NONE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t FaultCodes_<ContainerAllocator>::LIFT_OVERCURRENT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t FaultCodes_<ContainerAllocator>::LIFT_UNDERCURRENT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t FaultCodes_<ContainerAllocator>::LIFT_SLANT;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t FaultCodes_<ContainerAllocator>::LIFT_LIMIT_SWITCH;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t FaultCodes_<ContainerAllocator>::LIFT_SENSOR_FAILURE;
#endif  // __cplusplus < 201703L
#if __cplusplus < 201703L
// static constexpr member variable definitions are only needed in C++14 and below, deprecated in C++17
template<typename ContainerAllocator>
constexpr uint8_t FaultCodes_<ContainerAllocator>::LIFT_TIMEOUT;
#endif  // __cplusplus < 201703L

}  // namespace msg

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__FAULT_CODES__STRUCT_HPP_
