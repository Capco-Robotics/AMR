// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:srv/TriggerEstop.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__STRUCT_HPP_
#define AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__TriggerEstop_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__TriggerEstop_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TriggerEstop_Request_
{
  using Type = TriggerEstop_Request_<ContainerAllocator>;

  explicit TriggerEstop_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->release = false;
    }
  }

  explicit TriggerEstop_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->release = false;
    }
  }

  // field types and members
  using _release_type =
    bool;
  _release_type release;

  // setters for named parameter idiom
  Type & set__release(
    const bool & _arg)
  {
    this->release = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__TriggerEstop_Request
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__TriggerEstop_Request
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TriggerEstop_Request_ & other) const
  {
    if (this->release != other.release) {
      return false;
    }
    return true;
  }
  bool operator!=(const TriggerEstop_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TriggerEstop_Request_

// alias to use template instance with default allocator
using TriggerEstop_Request =
  amr_msgs::srv::TriggerEstop_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__TriggerEstop_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__TriggerEstop_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct TriggerEstop_Response_
{
  using Type = TriggerEstop_Response_<ContainerAllocator>;

  explicit TriggerEstop_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit TriggerEstop_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__TriggerEstop_Response
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__TriggerEstop_Response
    std::shared_ptr<amr_msgs::srv::TriggerEstop_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const TriggerEstop_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const TriggerEstop_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct TriggerEstop_Response_

// alias to use template instance with default allocator
using TriggerEstop_Response =
  amr_msgs::srv::TriggerEstop_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs

namespace amr_msgs
{

namespace srv
{

struct TriggerEstop
{
  using Request = amr_msgs::srv::TriggerEstop_Request;
  using Response = amr_msgs::srv::TriggerEstop_Response;
};

}  // namespace srv

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__STRUCT_HPP_
