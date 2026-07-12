// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:srv/SetDriveLimits.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__STRUCT_HPP_
#define AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__SetDriveLimits_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__SetDriveLimits_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetDriveLimits_Request_
{
  using Type = SetDriveLimits_Request_<ContainerAllocator>;

  explicit SetDriveLimits_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->max_linear_mps = 0.0f;
      this->max_angular_rps = 0.0f;
    }
  }

  explicit SetDriveLimits_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->max_linear_mps = 0.0f;
      this->max_angular_rps = 0.0f;
    }
  }

  // field types and members
  using _max_linear_mps_type =
    float;
  _max_linear_mps_type max_linear_mps;
  using _max_angular_rps_type =
    float;
  _max_angular_rps_type max_angular_rps;

  // setters for named parameter idiom
  Type & set__max_linear_mps(
    const float & _arg)
  {
    this->max_linear_mps = _arg;
    return *this;
  }
  Type & set__max_angular_rps(
    const float & _arg)
  {
    this->max_angular_rps = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__SetDriveLimits_Request
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__SetDriveLimits_Request
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetDriveLimits_Request_ & other) const
  {
    if (this->max_linear_mps != other.max_linear_mps) {
      return false;
    }
    if (this->max_angular_rps != other.max_angular_rps) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetDriveLimits_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetDriveLimits_Request_

// alias to use template instance with default allocator
using SetDriveLimits_Request =
  amr_msgs::srv::SetDriveLimits_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__SetDriveLimits_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__SetDriveLimits_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetDriveLimits_Response_
{
  using Type = SetDriveLimits_Response_<ContainerAllocator>;

  explicit SetDriveLimits_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit SetDriveLimits_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  // field types and members
  using _accepted_type =
    bool;
  _accepted_type accepted;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__SetDriveLimits_Response
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__SetDriveLimits_Response
    std::shared_ptr<amr_msgs::srv::SetDriveLimits_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetDriveLimits_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetDriveLimits_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetDriveLimits_Response_

// alias to use template instance with default allocator
using SetDriveLimits_Response =
  amr_msgs::srv::SetDriveLimits_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs

namespace amr_msgs
{

namespace srv
{

struct SetDriveLimits
{
  using Request = amr_msgs::srv::SetDriveLimits_Request;
  using Response = amr_msgs::srv::SetDriveLimits_Response;
};

}  // namespace srv

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__SET_DRIVE_LIMITS__STRUCT_HPP_
