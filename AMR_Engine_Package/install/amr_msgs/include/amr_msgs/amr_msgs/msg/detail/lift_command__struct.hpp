// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:msg/LiftCommand.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__STRUCT_HPP_
#define AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__STRUCT_HPP_

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
# define DEPRECATED__amr_msgs__msg__LiftCommand __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__msg__LiftCommand __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct LiftCommand_
{
  using Type = LiftCommand_<ContainerAllocator>;

  explicit LiftCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_position = 0.0f;
    }
  }

  explicit LiftCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_position = 0.0f;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _target_position_type =
    float;
  _target_position_type target_position;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__target_position(
    const float & _arg)
  {
    this->target_position = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::msg::LiftCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::msg::LiftCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::LiftCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::LiftCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__msg__LiftCommand
    std::shared_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__msg__LiftCommand
    std::shared_ptr<amr_msgs::msg::LiftCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const LiftCommand_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->target_position != other.target_position) {
      return false;
    }
    return true;
  }
  bool operator!=(const LiftCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct LiftCommand_

// alias to use template instance with default allocator
using LiftCommand =
  amr_msgs::msg::LiftCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__LIFT_COMMAND__STRUCT_HPP_
