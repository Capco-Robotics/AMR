// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:srv/GetPicoStatus.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__STRUCT_HPP_
#define AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__GetPicoStatus_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__GetPicoStatus_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetPicoStatus_Request_
{
  using Type = GetPicoStatus_Request_<ContainerAllocator>;

  explicit GetPicoStatus_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->structure_needs_at_least_one_member = 0;
    }
  }

  explicit GetPicoStatus_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__GetPicoStatus_Request
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__GetPicoStatus_Request
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetPicoStatus_Request_ & other) const
  {
    if (this->structure_needs_at_least_one_member != other.structure_needs_at_least_one_member) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetPicoStatus_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetPicoStatus_Request_

// alias to use template instance with default allocator
using GetPicoStatus_Request =
  amr_msgs::srv::GetPicoStatus_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__srv__GetPicoStatus_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__srv__GetPicoStatus_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct GetPicoStatus_Response_
{
  using Type = GetPicoStatus_Response_<ContainerAllocator>;

  explicit GetPicoStatus_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->uptime_ms = 0ul;
      this->last_rpi_msg_age_ms = 0ul;
      this->watchdog_resets = 0ul;
      this->free_mem_bytes = 0ul;
      this->available = false;
    }
  }

  explicit GetPicoStatus_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->uptime_ms = 0ul;
      this->last_rpi_msg_age_ms = 0ul;
      this->watchdog_resets = 0ul;
      this->free_mem_bytes = 0ul;
      this->available = false;
    }
  }

  // field types and members
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
  using _available_type =
    bool;
  _available_type available;

  // setters for named parameter idiom
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
  Type & set__available(
    const bool & _arg)
  {
    this->available = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__srv__GetPicoStatus_Response
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__srv__GetPicoStatus_Response
    std::shared_ptr<amr_msgs::srv::GetPicoStatus_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const GetPicoStatus_Response_ & other) const
  {
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
    if (this->available != other.available) {
      return false;
    }
    return true;
  }
  bool operator!=(const GetPicoStatus_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct GetPicoStatus_Response_

// alias to use template instance with default allocator
using GetPicoStatus_Response =
  amr_msgs::srv::GetPicoStatus_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace amr_msgs

namespace amr_msgs
{

namespace srv
{

struct GetPicoStatus
{
  using Request = amr_msgs::srv::GetPicoStatus_Request;
  using Response = amr_msgs::srv::GetPicoStatus_Response;
};

}  // namespace srv

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__GET_PICO_STATUS__STRUCT_HPP_
