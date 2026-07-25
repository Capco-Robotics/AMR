// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:msg/SignalCommand.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__MSG__DETAIL__SIGNAL_COMMAND__STRUCT_HPP_
#define AMR_MSGS__MSG__DETAIL__SIGNAL_COMMAND__STRUCT_HPP_

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
# define DEPRECATED__amr_msgs__msg__SignalCommand __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__msg__SignalCommand __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace msg
{

// message struct
template<class ContainerAllocator>
struct SignalCommand_
{
  using Type = SignalCommand_<ContainerAllocator>;

  explicit SignalCommand_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->siren_on = false;
      this->light_on = false;
      this->pattern_id = 0;
    }
  }

  explicit SignalCommand_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : header(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->siren_on = false;
      this->light_on = false;
      this->pattern_id = 0;
    }
  }

  // field types and members
  using _header_type =
    std_msgs::msg::Header_<ContainerAllocator>;
  _header_type header;
  using _siren_on_type =
    bool;
  _siren_on_type siren_on;
  using _light_on_type =
    bool;
  _light_on_type light_on;
  using _pattern_id_type =
    uint8_t;
  _pattern_id_type pattern_id;

  // setters for named parameter idiom
  Type & set__header(
    const std_msgs::msg::Header_<ContainerAllocator> & _arg)
  {
    this->header = _arg;
    return *this;
  }
  Type & set__siren_on(
    const bool & _arg)
  {
    this->siren_on = _arg;
    return *this;
  }
  Type & set__light_on(
    const bool & _arg)
  {
    this->light_on = _arg;
    return *this;
  }
  Type & set__pattern_id(
    const uint8_t & _arg)
  {
    this->pattern_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::msg::SignalCommand_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::msg::SignalCommand_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::SignalCommand_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::msg::SignalCommand_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__msg__SignalCommand
    std::shared_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__msg__SignalCommand
    std::shared_ptr<amr_msgs::msg::SignalCommand_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SignalCommand_ & other) const
  {
    if (this->header != other.header) {
      return false;
    }
    if (this->siren_on != other.siren_on) {
      return false;
    }
    if (this->light_on != other.light_on) {
      return false;
    }
    if (this->pattern_id != other.pattern_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const SignalCommand_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SignalCommand_

// alias to use template instance with default allocator
using SignalCommand =
  amr_msgs::msg::SignalCommand_<std::allocator<void>>;

// constant definitions

}  // namespace msg

}  // namespace amr_msgs

#endif  // AMR_MSGS__MSG__DETAIL__SIGNAL_COMMAND__STRUCT_HPP_
