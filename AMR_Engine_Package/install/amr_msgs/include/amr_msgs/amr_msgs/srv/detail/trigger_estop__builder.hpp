// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:srv/TriggerEstop.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__BUILDER_HPP_
#define AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/srv/detail/trigger_estop__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_TriggerEstop_Request_release
{
public:
  Init_TriggerEstop_Request_release()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::TriggerEstop_Request release(::amr_msgs::srv::TriggerEstop_Request::_release_type arg)
  {
    msg_.release = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::TriggerEstop_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::TriggerEstop_Request>()
{
  return amr_msgs::srv::builder::Init_TriggerEstop_Request_release();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_TriggerEstop_Response_success
{
public:
  Init_TriggerEstop_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::TriggerEstop_Response success(::amr_msgs::srv::TriggerEstop_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::TriggerEstop_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::TriggerEstop_Response>()
{
  return amr_msgs::srv::builder::Init_TriggerEstop_Response_success();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__TRIGGER_ESTOP__BUILDER_HPP_
