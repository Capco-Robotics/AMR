// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from amr_msgs:action/MoveLift.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__STRUCT_HPP_
#define AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <cstdint>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_Goal __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_Goal __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_Goal_
{
  using Type = MoveLift_Goal_<ContainerAllocator>;

  explicit MoveLift_Goal_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->target_position = 0.0f;
    }
  }

  explicit MoveLift_Goal_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
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
    amr_msgs::action::MoveLift_Goal_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_Goal_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_Goal_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_Goal_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_Goal
    std::shared_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_Goal
    std::shared_ptr<amr_msgs::action::MoveLift_Goal_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_Goal_ & other) const
  {
    if (this->target_position != other.target_position) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_Goal_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_Goal_

// alias to use template instance with default allocator
using MoveLift_Goal =
  amr_msgs::action::MoveLift_Goal_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_Result __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_Result __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_Result_
{
  using Type = MoveLift_Result_<ContainerAllocator>;

  explicit MoveLift_Result_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->final_position = 0.0f;
    }
  }

  explicit MoveLift_Result_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->success = false;
      this->final_position = 0.0f;
    }
  }

  // field types and members
  using _success_type =
    bool;
  _success_type success;
  using _final_position_type =
    float;
  _final_position_type final_position;

  // setters for named parameter idiom
  Type & set__success(
    const bool & _arg)
  {
    this->success = _arg;
    return *this;
  }
  Type & set__final_position(
    const float & _arg)
  {
    this->final_position = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::action::MoveLift_Result_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_Result_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_Result_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_Result_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_Result
    std::shared_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_Result
    std::shared_ptr<amr_msgs::action::MoveLift_Result_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_Result_ & other) const
  {
    if (this->success != other.success) {
      return false;
    }
    if (this->final_position != other.final_position) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_Result_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_Result_

// alias to use template instance with default allocator
using MoveLift_Result =
  amr_msgs::action::MoveLift_Result_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs


#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_Feedback __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_Feedback __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_Feedback_
{
  using Type = MoveLift_Feedback_<ContainerAllocator>;

  explicit MoveLift_Feedback_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_position = 0.0f;
      this->limit_upper = false;
      this->limit_lower = false;
    }
  }

  explicit MoveLift_Feedback_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    (void)_alloc;
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->current_position = 0.0f;
      this->limit_upper = false;
      this->limit_lower = false;
    }
  }

  // field types and members
  using _current_position_type =
    float;
  _current_position_type current_position;
  using _limit_upper_type =
    bool;
  _limit_upper_type limit_upper;
  using _limit_lower_type =
    bool;
  _limit_lower_type limit_lower;

  // setters for named parameter idiom
  Type & set__current_position(
    const float & _arg)
  {
    this->current_position = _arg;
    return *this;
  }
  Type & set__limit_upper(
    const bool & _arg)
  {
    this->limit_upper = _arg;
    return *this;
  }
  Type & set__limit_lower(
    const bool & _arg)
  {
    this->limit_lower = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::action::MoveLift_Feedback_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_Feedback_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_Feedback_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_Feedback_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_Feedback
    std::shared_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_Feedback
    std::shared_ptr<amr_msgs::action::MoveLift_Feedback_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_Feedback_ & other) const
  {
    if (this->current_position != other.current_position) {
      return false;
    }
    if (this->limit_upper != other.limit_upper) {
      return false;
    }
    if (this->limit_lower != other.limit_lower) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_Feedback_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_Feedback_

// alias to use template instance with default allocator
using MoveLift_Feedback =
  amr_msgs::action::MoveLift_Feedback_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs


// Include directives for member types
// Member 'goal_id'
#include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'goal'
#include "amr_msgs/action/detail/move_lift__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_SendGoal_Request_
{
  using Type = MoveLift_SendGoal_Request_<ContainerAllocator>;

  explicit MoveLift_SendGoal_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    goal(_init)
  {
    (void)_init;
  }

  explicit MoveLift_SendGoal_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    goal(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _goal_type =
    amr_msgs::action::MoveLift_Goal_<ContainerAllocator>;
  _goal_type goal;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__goal(
    const amr_msgs::action::MoveLift_Goal_<ContainerAllocator> & _arg)
  {
    this->goal = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Request
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Request
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_SendGoal_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->goal != other.goal) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_SendGoal_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_SendGoal_Request_

// alias to use template instance with default allocator
using MoveLift_SendGoal_Request =
  amr_msgs::action::MoveLift_SendGoal_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs


// Include directives for member types
// Member 'stamp'
#include "builtin_interfaces/msg/detail/time__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_SendGoal_Response_
{
  using Type = MoveLift_SendGoal_Response_<ContainerAllocator>;

  explicit MoveLift_SendGoal_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->accepted = false;
    }
  }

  explicit MoveLift_SendGoal_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : stamp(_alloc, _init)
  {
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
  using _stamp_type =
    builtin_interfaces::msg::Time_<ContainerAllocator>;
  _stamp_type stamp;

  // setters for named parameter idiom
  Type & set__accepted(
    const bool & _arg)
  {
    this->accepted = _arg;
    return *this;
  }
  Type & set__stamp(
    const builtin_interfaces::msg::Time_<ContainerAllocator> & _arg)
  {
    this->stamp = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Response
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_SendGoal_Response
    std::shared_ptr<amr_msgs::action::MoveLift_SendGoal_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_SendGoal_Response_ & other) const
  {
    if (this->accepted != other.accepted) {
      return false;
    }
    if (this->stamp != other.stamp) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_SendGoal_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_SendGoal_Response_

// alias to use template instance with default allocator
using MoveLift_SendGoal_Response =
  amr_msgs::action::MoveLift_SendGoal_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs

namespace amr_msgs
{

namespace action
{

struct MoveLift_SendGoal
{
  using Request = amr_msgs::action::MoveLift_SendGoal_Request;
  using Response = amr_msgs::action::MoveLift_SendGoal_Response;
};

}  // namespace action

}  // namespace amr_msgs


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_GetResult_Request __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_GetResult_Request __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_GetResult_Request_
{
  using Type = MoveLift_GetResult_Request_<ContainerAllocator>;

  explicit MoveLift_GetResult_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init)
  {
    (void)_init;
  }

  explicit MoveLift_GetResult_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_GetResult_Request
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_GetResult_Request
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_GetResult_Request_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_GetResult_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_GetResult_Request_

// alias to use template instance with default allocator
using MoveLift_GetResult_Request =
  amr_msgs::action::MoveLift_GetResult_Request_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs


// Include directives for member types
// Member 'result'
// already included above
// #include "amr_msgs/action/detail/move_lift__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_GetResult_Response __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_GetResult_Response __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_GetResult_Response_
{
  using Type = MoveLift_GetResult_Response_<ContainerAllocator>;

  explicit MoveLift_GetResult_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  explicit MoveLift_GetResult_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : result(_alloc, _init)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->status = 0;
    }
  }

  // field types and members
  using _status_type =
    int8_t;
  _status_type status;
  using _result_type =
    amr_msgs::action::MoveLift_Result_<ContainerAllocator>;
  _result_type result;

  // setters for named parameter idiom
  Type & set__status(
    const int8_t & _arg)
  {
    this->status = _arg;
    return *this;
  }
  Type & set__result(
    const amr_msgs::action::MoveLift_Result_<ContainerAllocator> & _arg)
  {
    this->result = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_GetResult_Response
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_GetResult_Response
    std::shared_ptr<amr_msgs::action::MoveLift_GetResult_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_GetResult_Response_ & other) const
  {
    if (this->status != other.status) {
      return false;
    }
    if (this->result != other.result) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_GetResult_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_GetResult_Response_

// alias to use template instance with default allocator
using MoveLift_GetResult_Response =
  amr_msgs::action::MoveLift_GetResult_Response_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs

namespace amr_msgs
{

namespace action
{

struct MoveLift_GetResult
{
  using Request = amr_msgs::action::MoveLift_GetResult_Request;
  using Response = amr_msgs::action::MoveLift_GetResult_Response;
};

}  // namespace action

}  // namespace amr_msgs


// Include directives for member types
// Member 'goal_id'
// already included above
// #include "unique_identifier_msgs/msg/detail/uuid__struct.hpp"
// Member 'feedback'
// already included above
// #include "amr_msgs/action/detail/move_lift__struct.hpp"

#ifndef _WIN32
# define DEPRECATED__amr_msgs__action__MoveLift_FeedbackMessage __attribute__((deprecated))
#else
# define DEPRECATED__amr_msgs__action__MoveLift_FeedbackMessage __declspec(deprecated)
#endif

namespace amr_msgs
{

namespace action
{

// message struct
template<class ContainerAllocator>
struct MoveLift_FeedbackMessage_
{
  using Type = MoveLift_FeedbackMessage_<ContainerAllocator>;

  explicit MoveLift_FeedbackMessage_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_init),
    feedback(_init)
  {
    (void)_init;
  }

  explicit MoveLift_FeedbackMessage_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : goal_id(_alloc, _init),
    feedback(_alloc, _init)
  {
    (void)_init;
  }

  // field types and members
  using _goal_id_type =
    unique_identifier_msgs::msg::UUID_<ContainerAllocator>;
  _goal_id_type goal_id;
  using _feedback_type =
    amr_msgs::action::MoveLift_Feedback_<ContainerAllocator>;
  _feedback_type feedback;

  // setters for named parameter idiom
  Type & set__goal_id(
    const unique_identifier_msgs::msg::UUID_<ContainerAllocator> & _arg)
  {
    this->goal_id = _arg;
    return *this;
  }
  Type & set__feedback(
    const amr_msgs::action::MoveLift_Feedback_<ContainerAllocator> & _arg)
  {
    this->feedback = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator> *;
  using ConstRawPtr =
    const amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__amr_msgs__action__MoveLift_FeedbackMessage
    std::shared_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__amr_msgs__action__MoveLift_FeedbackMessage
    std::shared_ptr<amr_msgs::action::MoveLift_FeedbackMessage_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const MoveLift_FeedbackMessage_ & other) const
  {
    if (this->goal_id != other.goal_id) {
      return false;
    }
    if (this->feedback != other.feedback) {
      return false;
    }
    return true;
  }
  bool operator!=(const MoveLift_FeedbackMessage_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct MoveLift_FeedbackMessage_

// alias to use template instance with default allocator
using MoveLift_FeedbackMessage =
  amr_msgs::action::MoveLift_FeedbackMessage_<std::allocator<void>>;

// constant definitions

}  // namespace action

}  // namespace amr_msgs

#include "action_msgs/srv/cancel_goal.hpp"
#include "action_msgs/msg/goal_info.hpp"
#include "action_msgs/msg/goal_status_array.hpp"

namespace amr_msgs
{

namespace action
{

struct MoveLift
{
  /// The goal message defined in the action definition.
  using Goal = amr_msgs::action::MoveLift_Goal;
  /// The result message defined in the action definition.
  using Result = amr_msgs::action::MoveLift_Result;
  /// The feedback message defined in the action definition.
  using Feedback = amr_msgs::action::MoveLift_Feedback;

  struct Impl
  {
    /// The send_goal service using a wrapped version of the goal message as a request.
    using SendGoalService = amr_msgs::action::MoveLift_SendGoal;
    /// The get_result service using a wrapped version of the result message as a response.
    using GetResultService = amr_msgs::action::MoveLift_GetResult;
    /// The feedback message with generic fields which wraps the feedback message.
    using FeedbackMessage = amr_msgs::action::MoveLift_FeedbackMessage;

    /// The generic service to cancel a goal.
    using CancelGoalService = action_msgs::srv::CancelGoal;
    /// The generic message for the status of a goal.
    using GoalStatusMessage = action_msgs::msg::GoalStatusArray;
  };
};

typedef struct MoveLift MoveLift;

}  // namespace action

}  // namespace amr_msgs

#endif  // AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__STRUCT_HPP_
