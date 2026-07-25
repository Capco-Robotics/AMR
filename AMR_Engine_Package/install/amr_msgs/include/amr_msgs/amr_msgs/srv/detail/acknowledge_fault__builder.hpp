// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:srv/AcknowledgeFault.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__BUILDER_HPP_
#define AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/srv/detail/acknowledge_fault__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_AcknowledgeFault_Request_fault_id
{
public:
  Init_AcknowledgeFault_Request_fault_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::AcknowledgeFault_Request fault_id(::amr_msgs::srv::AcknowledgeFault_Request::_fault_id_type arg)
  {
    msg_.fault_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::AcknowledgeFault_Request msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::AcknowledgeFault_Request>()
{
  return amr_msgs::srv::builder::Init_AcknowledgeFault_Request_fault_id();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace srv
{

namespace builder
{

class Init_AcknowledgeFault_Response_success
{
public:
  Init_AcknowledgeFault_Response_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::srv::AcknowledgeFault_Response success(::amr_msgs::srv::AcknowledgeFault_Response::_success_type arg)
  {
    msg_.success = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::srv::AcknowledgeFault_Response msg_;
};

}  // namespace builder

}  // namespace srv

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::srv::AcknowledgeFault_Response>()
{
  return amr_msgs::srv::builder::Init_AcknowledgeFault_Response_success();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__SRV__DETAIL__ACKNOWLEDGE_FAULT__BUILDER_HPP_
