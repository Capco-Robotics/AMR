// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:srv/SetLiftTarget.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__STRUCT_HPP_
#define AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__SetLiftTarget_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__SetLiftTarget_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetLiftTarget_Request_
{
  using Type = SetLiftTarget_Request_<ContainerAllocator>;

  explicit SetLiftTarget_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_position = 0.0f;
    }
  }

  explicit SetLiftTarget_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_position = 0.0f;
    }
  }

  // field types and members
  using _target_position_type =
    float;
  _target_position_type target_position;

  // setters for named parameter idiom
  Type & set__target_position(
    const float & _arg)
  {
    this->target_position = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__SetLiftTarget_Request
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__SetLiftTarget_Request
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetLiftTarget_Request_ & other) const
  {
    if (this->target_position != other.target_position) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetLiftTarget_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetLiftTarget_Request_

// alias to use template instance with default allocator
using SetLiftTarget_Request =
  amr_msgs::srv::SetLiftTarget_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__SetLiftTarget_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__SetLiftTarget_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct SetLiftTarget_Response_
{
  using Type = SetLiftTarget_Response_<ContainerAllocator>;

  explicit SetLiftTarget_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit SetLiftTarget_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__SetLiftTarget_Response
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__SetLiftTarget_Response
    std::shared_ptr<amr_msgs::srv::SetLiftTarget_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const SetLiftTarget_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    return true;
  }
  bool operator!=(const SetLiftTarget_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct SetLiftTarget_Response_

// alias to use template instance with default allocator
using SetLiftTarget_Response =
  amr_msgs::srv::SetLiftTarget_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs

namespace amr_msgs
{

namespace srv
{

struct SetLiftTarget
{
  using Request = amr_msgs::srv::SetLiftTarget_Request;
  using Response = amr_msgs::srv::SetLiftTarget_Response;
};

}  // namespace srv

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__SET_LIFT_TARGET__STRUCT_HPP_
