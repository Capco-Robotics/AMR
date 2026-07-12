// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:action/NavigateToGoal.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__ACTION__DETAIL__NAVIGATE_TO_GOAL__BUILDER_HPP_
#define AMR_MSGS__ACTION__DETAIL__NAVIGATE_TO_GOAL__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/action/detail/navigate_to_goal__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_Goal_goal_theta
{
public:
  explicit Init_NavigateToGoal_Goal_goal_theta(::amr_msgs::action::NavigateToGoal_Goal & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::NavigateToGoal_Goal goal_theta(::amr_msgs::action::NavigateToGoal_Goal::_goal_theta_type arg)
  {
    msg_.goal_theta = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Goal msg_;
};

class Init_NavigateToGoal_Goal_goal_y
{
public:
  explicit Init_NavigateToGoal_Goal_goal_y(::amr_msgs::action::NavigateToGoal_Goal & msg)
  : msg_(msg)
  {}
  Init_NavigateToGoal_Goal_goal_theta goal_y(::amr_msgs::action::NavigateToGoal_Goal::_goal_y_type arg)
  {
    msg_.goal_y = std::move(arg);
    return Init_NavigateToGoal_Goal_goal_theta(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Goal msg_;
};

class Init_NavigateToGoal_Goal_goal_x
{
public:
  Init_NavigateToGoal_Goal_goal_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavigateToGoal_Goal_goal_y goal_x(::amr_msgs::action::NavigateToGoal_Goal::_goal_x_type arg)
  {
    msg_.goal_x = std::move(arg);
    return Init_NavigateToGoal_Goal_goal_y(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_Goal>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_Goal_goal_x();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_Result_outcome
{
public:
  explicit Init_NavigateToGoal_Result_outcome(::amr_msgs::action::NavigateToGoal_Result & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::NavigateToGoal_Result outcome(::amr_msgs::action::NavigateToGoal_Result::_outcome_type arg)
  {
    msg_.outcome = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Result msg_;
};

class Init_NavigateToGoal_Result_success
{
public:
  Init_NavigateToGoal_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavigateToGoal_Result_outcome success(::amr_msgs::action::NavigateToGoal_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_NavigateToGoal_Result_outcome(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_Result>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_Result_success();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_Feedback_distance_remaining
{
public:
  explicit Init_NavigateToGoal_Feedback_distance_remaining(::amr_msgs::action::NavigateToGoal_Feedback & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::NavigateToGoal_Feedback distance_remaining(::amr_msgs::action::NavigateToGoal_Feedback::_distance_remaining_type arg)
  {
    msg_.distance_remaining = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Feedback msg_;
};

class Init_NavigateToGoal_Feedback_current_y
{
public:
  explicit Init_NavigateToGoal_Feedback_current_y(::amr_msgs::action::NavigateToGoal_Feedback & msg)
  : msg_(msg)
  {}
  Init_NavigateToGoal_Feedback_distance_remaining current_y(::amr_msgs::action::NavigateToGoal_Feedback::_current_y_type arg)
  {
    msg_.current_y = std::move(arg);
    return Init_NavigateToGoal_Feedback_distance_remaining(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Feedback msg_;
};

class Init_NavigateToGoal_Feedback_current_x
{
public:
  Init_NavigateToGoal_Feedback_current_x()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavigateToGoal_Feedback_current_y current_x(::amr_msgs::action::NavigateToGoal_Feedback::_current_x_type arg)
  {
    msg_.current_x = std::move(arg);
    return Init_NavigateToGoal_Feedback_current_y(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_Feedback>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_Feedback_current_x();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_SendGoal_Request_goal
{
public:
  explicit Init_NavigateToGoal_SendGoal_Request_goal(::amr_msgs::action::NavigateToGoal_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::NavigateToGoal_SendGoal_Request goal(::amr_msgs::action::NavigateToGoal_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_SendGoal_Request msg_;
};

class Init_NavigateToGoal_SendGoal_Request_goal_id
{
public:
  Init_NavigateToGoal_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavigateToGoal_SendGoal_Request_goal goal_id(::amr_msgs::action::NavigateToGoal_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_NavigateToGoal_SendGoal_Request_goal(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_SendGoal_Request>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_SendGoal_Request_goal_id();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_SendGoal_Response_stamp
{
public:
  explicit Init_NavigateToGoal_SendGoal_Response_stamp(::amr_msgs::action::NavigateToGoal_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::NavigateToGoal_SendGoal_Response stamp(::amr_msgs::action::NavigateToGoal_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_SendGoal_Response msg_;
};

class Init_NavigateToGoal_SendGoal_Response_accepted
{
public:
  Init_NavigateToGoal_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavigateToGoal_SendGoal_Response_stamp accepted(::amr_msgs::action::NavigateToGoal_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_NavigateToGoal_SendGoal_Response_stamp(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_SendGoal_Response>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_SendGoal_Response_accepted();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_GetResult_Request_goal_id
{
public:
  Init_NavigateToGoal_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::action::NavigateToGoal_GetResult_Request goal_id(::amr_msgs::action::NavigateToGoal_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_GetResult_Request>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_GetResult_Request_goal_id();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_GetResult_Response_result
{
public:
  explicit Init_NavigateToGoal_GetResult_Response_result(::amr_msgs::action::NavigateToGoal_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::NavigateToGoal_GetResult_Response result(::amr_msgs::action::NavigateToGoal_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_GetResult_Response msg_;
};

class Init_NavigateToGoal_GetResult_Response_status
{
public:
  Init_NavigateToGoal_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavigateToGoal_GetResult_Response_result status(::amr_msgs::action::NavigateToGoal_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_NavigateToGoal_GetResult_Response_result(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_GetResult_Response>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_GetResult_Response_status();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_NavigateToGoal_FeedbackMessage_feedback
{
public:
  explicit Init_NavigateToGoal_FeedbackMessage_feedback(::amr_msgs::action::NavigateToGoal_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::NavigateToGoal_FeedbackMessage feedback(::amr_msgs::action::NavigateToGoal_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_FeedbackMessage msg_;
};

class Init_NavigateToGoal_FeedbackMessage_goal_id
{
public:
  Init_NavigateToGoal_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_NavigateToGoal_FeedbackMessage_feedback goal_id(::amr_msgs::action::NavigateToGoal_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_NavigateToGoal_FeedbackMessage_feedback(msg_);
  }

private:
  ::amr_msgs::action::NavigateToGoal_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::NavigateToGoal_FeedbackMessage>()
{
  return amr_msgs::action::builder::Init_NavigateToGoal_FeedbackMessage_goal_id();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__ACTION__DETAIL__NAVIGATE_TO_GOAL__BUILDER_HPP_
