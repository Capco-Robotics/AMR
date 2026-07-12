// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:srv/GetRobotState.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__STRUCT_HPP_
#define AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__GetRobotState_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__GetRobotState_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetRobotState_Request_
{
  using Type = GetRobotState_Request_<ContainerAllocator>;

  explicit GetRobotState_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GetRobotState_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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

  // pointer types
  using RawPtr =
    amr_msgs::srv::GetRobotState_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::GetRobotState_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetRobotState_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetRobotState_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__GetRobotState_Request
    std::shared_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__GetRobotState_Request
    std::shared_ptr<amr_msgs::srv::GetRobotState_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetRobotState_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetRobotState_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetRobotState_Request_

// alias to use template instance with default allocator
using GetRobotState_Request =
  amr_msgs::srv::GetRobotState_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__GetRobotState_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__GetRobotState_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetRobotState_Response_
{
  using Type = GetRobotState_Response_<ContainerAllocator>;

  explicit GetRobotState_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = "";
    }
  }

  explicit GetRobotState_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : state(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->state = "";
    }
  }

  // field types and members
  using _state_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _state_type state;
  using _active_faults_type =
    std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>>;
  _active_faults_type active_faults;

  // setters for named parameter idiom
  Type & set__state(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->state = _arg;
    return *this;
  }
  Type & set__active_faults(
    const std::vector<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>>> & _arg)
  {
    this->active_faults = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::GetRobotState_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::GetRobotState_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetRobotState_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetRobotState_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__GetRobotState_Response
    std::shared_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__GetRobotState_Response
    std::shared_ptr<amr_msgs::srv::GetRobotState_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetRobotState_Response_ & other) const
  {
    if (this->state != other.state) {
      return false;
    }
    if (this->active_faults != other.active_faults) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetRobotState_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetRobotState_Response_

// alias to use template instance with default allocator
using GetRobotState_Response =
  amr_msgs::srv::GetRobotState_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs

namespace amr_msgs
{

namespace srv
{

struct GetRobotState
{
  using Request = amr_msgs::srv::GetRobotState_Request;
  using Response = amr_msgs::srv::GetRobotState_Response;
};

}  // namespace srv

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__GET_ROBOT_STATE__STRUCT_HPP_
