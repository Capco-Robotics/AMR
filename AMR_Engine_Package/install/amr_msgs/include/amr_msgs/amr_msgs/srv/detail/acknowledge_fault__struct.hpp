// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:srv/AcknowledgeFault.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__STRUCT_HPP_
#define AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__AcknowledgeFault_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__AcknowledgeFault_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AcknowledgeFault_Request_
{
  using Type = AcknowledgeFault_Request_<ContainerAllocator>;

  explicit AcknowledgeFault_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->fault_id = "";
    }
  }

  explicit AcknowledgeFault_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : fault_id(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->fault_id = "";
    }
  }

  // field types and members
  using _fault_id_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _fault_id_type fault_id;

  // setters for named parameter idiom
  Type & set__fault_id(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->fault_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__AcknowledgeFault_Request
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__AcknowledgeFault_Request
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AcknowledgeFault_Request_ & other) const
  {
    if (this->fault_id != other.fault_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const AcknowledgeFault_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AcknowledgeFault_Request_

// alias to use template instance with default allocator
using AcknowledgeFault_Request =
  amr_msgs::srv::AcknowledgeFault_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__AcknowledgeFault_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__AcknowledgeFault_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct AcknowledgeFault_Response_
{
  using Type = AcknowledgeFault_Response_<ContainerAllocator>;

  explicit AcknowledgeFault_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
    }
  }

  explicit AcknowledgeFault_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__AcknowledgeFault_Response
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__AcknowledgeFault_Response
    std::shared_ptr<amr_msgs::srv::AcknowledgeFault_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const AcknowledgeFault_Response_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    return true;
  }
  bool operator!=(const AcknowledgeFault_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct AcknowledgeFault_Response_

// alias to use template instance with default allocator
using AcknowledgeFault_Response =
  amr_msgs::srv::AcknowledgeFault_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs

namespace amr_msgs
{

namespace srv
{

struct AcknowledgeFault
{
  using Request = amr_msgs::srv::AcknowledgeFault_Request;
  using Response = amr_msgs::srv::AcknowledgeFault_Response;
};

}  // namespace srv

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__STRUCT_HPP_
