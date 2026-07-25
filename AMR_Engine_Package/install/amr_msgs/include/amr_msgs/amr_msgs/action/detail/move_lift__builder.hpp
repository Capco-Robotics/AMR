// generated from rosidl_generator_cpp/resource/idl__builder.hpp.em
// with input from amr_msgs:action/MoveLift.idl
// generated code does not contain a copyright notice

#ifndef AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__BUILDER_HPP_
#define AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__BUILDER_HPP_

#include <algorithm>
#include <utility>

#include "amr_msgs/action/detail/move_lift__struct.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_Goal_target_position
{
public:
  Init_MoveLift_Goal_target_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::action::MoveLift_Goal target_position(::amr_msgs::action::MoveLift_Goal::_target_position_type arg)
  {
    msg_.target_position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_Goal msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_Goal>()
{
  return amr_msgs::action::builder::Init_MoveLift_Goal_target_position();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_Result_final_position
{
public:
  explicit Init_MoveLift_Result_final_position(::amr_msgs::action::MoveLift_Result & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::MoveLift_Result final_position(::amr_msgs::action::MoveLift_Result::_final_position_type arg)
  {
    msg_.final_position = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_Result msg_;
};

class Init_MoveLift_Result_success
{
public:
  Init_MoveLift_Result_success()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveLift_Result_final_position success(::amr_msgs::action::MoveLift_Result::_success_type arg)
  {
    msg_.success = std::move(arg);
    return Init_MoveLift_Result_final_position(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_Result msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_Result>()
{
  return amr_msgs::action::builder::Init_MoveLift_Result_success();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_Feedback_limit_lower
{
public:
  explicit Init_MoveLift_Feedback_limit_lower(::amr_msgs::action::MoveLift_Feedback & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::MoveLift_Feedback limit_lower(::amr_msgs::action::MoveLift_Feedback::_limit_lower_type arg)
  {
    msg_.limit_lower = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_Feedback msg_;
};

class Init_MoveLift_Feedback_limit_upper
{
public:
  explicit Init_MoveLift_Feedback_limit_upper(::amr_msgs::action::MoveLift_Feedback & msg)
  : msg_(msg)
  {}
  Init_MoveLift_Feedback_limit_lower limit_upper(::amr_msgs::action::MoveLift_Feedback::_limit_upper_type arg)
  {
    msg_.limit_upper = std::move(arg);
    return Init_MoveLift_Feedback_limit_lower(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_Feedback msg_;
};

class Init_MoveLift_Feedback_current_position
{
public:
  Init_MoveLift_Feedback_current_position()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveLift_Feedback_limit_upper current_position(::amr_msgs::action::MoveLift_Feedback::_current_position_type arg)
  {
    msg_.current_position = std::move(arg);
    return Init_MoveLift_Feedback_limit_upper(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_Feedback msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_Feedback>()
{
  return amr_msgs::action::builder::Init_MoveLift_Feedback_current_position();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_SendGoal_Request_goal
{
public:
  explicit Init_MoveLift_SendGoal_Request_goal(::amr_msgs::action::MoveLift_SendGoal_Request & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::MoveLift_SendGoal_Request goal(::amr_msgs::action::MoveLift_SendGoal_Request::_goal_type arg)
  {
    msg_.goal = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_SendGoal_Request msg_;
};

class Init_MoveLift_SendGoal_Request_goal_id
{
public:
  Init_MoveLift_SendGoal_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveLift_SendGoal_Request_goal goal_id(::amr_msgs::action::MoveLift_SendGoal_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_MoveLift_SendGoal_Request_goal(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_SendGoal_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_SendGoal_Request>()
{
  return amr_msgs::action::builder::Init_MoveLift_SendGoal_Request_goal_id();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_SendGoal_Response_stamp
{
public:
  explicit Init_MoveLift_SendGoal_Response_stamp(::amr_msgs::action::MoveLift_SendGoal_Response & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::MoveLift_SendGoal_Response stamp(::amr_msgs::action::MoveLift_SendGoal_Response::_stamp_type arg)
  {
    msg_.stamp = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_SendGoal_Response msg_;
};

class Init_MoveLift_SendGoal_Response_accepted
{
public:
  Init_MoveLift_SendGoal_Response_accepted()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveLift_SendGoal_Response_stamp accepted(::amr_msgs::action::MoveLift_SendGoal_Response::_accepted_type arg)
  {
    msg_.accepted = std::move(arg);
    return Init_MoveLift_SendGoal_Response_stamp(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_SendGoal_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_SendGoal_Response>()
{
  return amr_msgs::action::builder::Init_MoveLift_SendGoal_Response_accepted();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_GetResult_Request_goal_id
{
public:
  Init_MoveLift_GetResult_Request_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  ::amr_msgs::action::MoveLift_GetResult_Request goal_id(::amr_msgs::action::MoveLift_GetResult_Request::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_GetResult_Request msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_GetResult_Request>()
{
  return amr_msgs::action::builder::Init_MoveLift_GetResult_Request_goal_id();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_GetResult_Response_result
{
public:
  explicit Init_MoveLift_GetResult_Response_result(::amr_msgs::action::MoveLift_GetResult_Response & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::MoveLift_GetResult_Response result(::amr_msgs::action::MoveLift_GetResult_Response::_result_type arg)
  {
    msg_.result = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_GetResult_Response msg_;
};

class Init_MoveLift_GetResult_Response_status
{
public:
  Init_MoveLift_GetResult_Response_status()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveLift_GetResult_Response_result status(::amr_msgs::action::MoveLift_GetResult_Response::_status_type arg)
  {
    msg_.status = std::move(arg);
    return Init_MoveLift_GetResult_Response_result(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_GetResult_Response msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_GetResult_Response>()
{
  return amr_msgs::action::builder::Init_MoveLift_GetResult_Response_status();
}

}  // namespace amr_msgs


namespace amr_msgs
{

namespace action
{

namespace builder
{

class Init_MoveLift_FeedbackMessage_feedback
{
public:
  explicit Init_MoveLift_FeedbackMessage_feedback(::amr_msgs::action::MoveLift_FeedbackMessage & msg)
  : msg_(msg)
  {}
  ::amr_msgs::action::MoveLift_FeedbackMessage feedback(::amr_msgs::action::MoveLift_FeedbackMessage::_feedback_type arg)
  {
    msg_.feedback = std::move(arg);
    return std::move(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_FeedbackMessage msg_;
};

class Init_MoveLift_FeedbackMessage_goal_id
{
public:
  Init_MoveLift_FeedbackMessage_goal_id()
  : msg_(::rosidl_runtime_cpp::MessageInitialization::SKIP)
  {}
  Init_MoveLift_FeedbackMessage_feedback goal_id(::amr_msgs::action::MoveLift_FeedbackMessage::_goal_id_type arg)
  {
    msg_.goal_id = std::move(arg);
    return Init_MoveLift_FeedbackMessage_feedback(msg_);
  }

private:
  ::amr_msgs::action::MoveLift_FeedbackMessage msg_;
};

}  // namespace builder

}  // namespace action

template<typename MessageType>
auto build();

template<>
inline
auto build<::amr_msgs::action::MoveLift_FeedbackMessage>()
{
  return amr_msgs::action::builder::Init_MoveLift_FeedbackMessage_goal_id();
}

}  // namespace amr_msgs

#endif  // AMR_MSGS__ACTION__DETAIL__MOVE_LIFT__BUILDER_HPP_
