
#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_Goal() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_Goal__init(msg: *mut NavigateToGoal_Goal) -> bool;
    fn amr_msgs__action__NavigateToGoal_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Goal>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Goal>);
    fn amr_msgs__action__NavigateToGoal_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Goal>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_Goal {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_x: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_y: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_theta: f32,

}



impl Default for NavigateToGoal_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_Goal__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_Goal() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_Result() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_Result__init(msg: *mut NavigateToGoal_Result) -> bool;
    fn amr_msgs__action__NavigateToGoal_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Result>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Result>);
    fn amr_msgs__action__NavigateToGoal_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Result>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub outcome: rosidl_runtime_rs::String,

}



impl Default for NavigateToGoal_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_Result__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_Result where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_Result() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_Feedback__init(msg: *mut NavigateToGoal_Feedback) -> bool;
    fn amr_msgs__action__NavigateToGoal_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Feedback>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Feedback>);
    fn amr_msgs__action__NavigateToGoal_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_Feedback>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub current_x: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub current_y: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub distance_remaining: f32,

}



impl Default for NavigateToGoal_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_Feedback__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_Feedback() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_FeedbackMessage__init(msg: *mut NavigateToGoal_FeedbackMessage) -> bool;
    fn amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_FeedbackMessage>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_FeedbackMessage>);
    fn amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_FeedbackMessage>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::NavigateToGoal_Feedback,

}



impl Default for NavigateToGoal_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_FeedbackMessage() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_Goal() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_Goal__init(msg: *mut MoveLift_Goal) -> bool;
    fn amr_msgs__action__MoveLift_Goal__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Goal>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_Goal__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Goal>);
    fn amr_msgs__action__MoveLift_Goal__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_Goal>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Goal>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_Goal
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_Goal {

    // This member is not documented.
    #[allow(missing_docs)]
    pub target_position: f32,

}



impl Default for MoveLift_Goal {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_Goal__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_Goal__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_Goal {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Goal__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Goal__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Goal__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_Goal {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_Goal where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_Goal";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_Goal() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_Result() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_Result__init(msg: *mut MoveLift_Result) -> bool;
    fn amr_msgs__action__MoveLift_Result__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Result>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_Result__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Result>);
    fn amr_msgs__action__MoveLift_Result__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_Result>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Result>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_Result
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_Result {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub final_position: f32,

}



impl Default for MoveLift_Result {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_Result__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_Result__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_Result {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Result__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Result__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Result__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_Result {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_Result where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_Result";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_Result() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_Feedback() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_Feedback__init(msg: *mut MoveLift_Feedback) -> bool;
    fn amr_msgs__action__MoveLift_Feedback__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Feedback>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_Feedback__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Feedback>);
    fn amr_msgs__action__MoveLift_Feedback__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_Feedback>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_Feedback>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_Feedback
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_Feedback {

    // This member is not documented.
    #[allow(missing_docs)]
    pub current_position: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub limit_upper: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub limit_lower: bool,

}



impl Default for MoveLift_Feedback {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_Feedback__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_Feedback__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_Feedback {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Feedback__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Feedback__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_Feedback__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_Feedback {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_Feedback where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_Feedback";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_Feedback() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_FeedbackMessage() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_FeedbackMessage__init(msg: *mut MoveLift_FeedbackMessage) -> bool;
    fn amr_msgs__action__MoveLift_FeedbackMessage__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_FeedbackMessage>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_FeedbackMessage__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_FeedbackMessage>);
    fn amr_msgs__action__MoveLift_FeedbackMessage__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_FeedbackMessage>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_FeedbackMessage>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_FeedbackMessage
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_FeedbackMessage {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub feedback: super::super::action::rmw::MoveLift_Feedback,

}



impl Default for MoveLift_FeedbackMessage {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_FeedbackMessage__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_FeedbackMessage__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_FeedbackMessage {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_FeedbackMessage__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_FeedbackMessage__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_FeedbackMessage__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_FeedbackMessage {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_FeedbackMessage where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_FeedbackMessage";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_FeedbackMessage() }
  }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_SendGoal_Request__init(msg: *mut NavigateToGoal_SendGoal_Request) -> bool;
    fn amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Request>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Request>);
    fn amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Request>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::NavigateToGoal_Goal,

}



impl Default for NavigateToGoal_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_SendGoal_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_SendGoal_Response__init(msg: *mut NavigateToGoal_SendGoal_Response) -> bool;
    fn amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Response>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Response>);
    fn amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_SendGoal_Response>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for NavigateToGoal_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_SendGoal_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_GetResult_Request__init(msg: *mut NavigateToGoal_GetResult_Request) -> bool;
    fn amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Request>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Request>);
    fn amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Request>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for NavigateToGoal_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_GetResult_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__NavigateToGoal_GetResult_Response__init(msg: *mut NavigateToGoal_GetResult_Response) -> bool;
    fn amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Response>, size: usize) -> bool;
    fn amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Response>);
    fn amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<NavigateToGoal_GetResult_Response>) -> bool;
}

// Corresponds to amr_msgs__action__NavigateToGoal_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct NavigateToGoal_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::NavigateToGoal_Result,

}



impl Default for NavigateToGoal_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__NavigateToGoal_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__NavigateToGoal_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for NavigateToGoal_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__NavigateToGoal_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for NavigateToGoal_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for NavigateToGoal_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/NavigateToGoal_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__NavigateToGoal_GetResult_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_SendGoal_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_SendGoal_Request__init(msg: *mut MoveLift_SendGoal_Request) -> bool;
    fn amr_msgs__action__MoveLift_SendGoal_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Request>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_SendGoal_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Request>);
    fn amr_msgs__action__MoveLift_SendGoal_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Request>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_SendGoal_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_SendGoal_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,


    // This member is not documented.
    #[allow(missing_docs)]
    pub goal: super::super::action::rmw::MoveLift_Goal,

}



impl Default for MoveLift_SendGoal_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_SendGoal_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_SendGoal_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_SendGoal_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_SendGoal_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_SendGoal_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_SendGoal_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_SendGoal_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_SendGoal_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_SendGoal_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_SendGoal_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_SendGoal_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_SendGoal_Response__init(msg: *mut MoveLift_SendGoal_Response) -> bool;
    fn amr_msgs__action__MoveLift_SendGoal_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Response>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_SendGoal_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Response>);
    fn amr_msgs__action__MoveLift_SendGoal_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_SendGoal_Response>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_SendGoal_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_SendGoal_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub stamp: builtin_interfaces::msg::rmw::Time,

}



impl Default for MoveLift_SendGoal_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_SendGoal_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_SendGoal_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_SendGoal_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_SendGoal_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_SendGoal_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_SendGoal_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_SendGoal_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_SendGoal_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_SendGoal_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_SendGoal_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_GetResult_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_GetResult_Request__init(msg: *mut MoveLift_GetResult_Request) -> bool;
    fn amr_msgs__action__MoveLift_GetResult_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_GetResult_Request>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_GetResult_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_GetResult_Request>);
    fn amr_msgs__action__MoveLift_GetResult_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_GetResult_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_GetResult_Request>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_GetResult_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_GetResult_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub goal_id: unique_identifier_msgs::msg::rmw::UUID,

}



impl Default for MoveLift_GetResult_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_GetResult_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_GetResult_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_GetResult_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_GetResult_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_GetResult_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_GetResult_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_GetResult_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_GetResult_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_GetResult_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_GetResult_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_GetResult_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__action__MoveLift_GetResult_Response__init(msg: *mut MoveLift_GetResult_Response) -> bool;
    fn amr_msgs__action__MoveLift_GetResult_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_GetResult_Response>, size: usize) -> bool;
    fn amr_msgs__action__MoveLift_GetResult_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<MoveLift_GetResult_Response>);
    fn amr_msgs__action__MoveLift_GetResult_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<MoveLift_GetResult_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<MoveLift_GetResult_Response>) -> bool;
}

// Corresponds to amr_msgs__action__MoveLift_GetResult_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct MoveLift_GetResult_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub status: i8,


    // This member is not documented.
    #[allow(missing_docs)]
    pub result: super::super::action::rmw::MoveLift_Result,

}



impl Default for MoveLift_GetResult_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__action__MoveLift_GetResult_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__action__MoveLift_GetResult_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for MoveLift_GetResult_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_GetResult_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_GetResult_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__action__MoveLift_GetResult_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for MoveLift_GetResult_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for MoveLift_GetResult_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/action/MoveLift_GetResult_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__action__MoveLift_GetResult_Response() }
  }
}






#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__NavigateToGoal_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__action__NavigateToGoal_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct NavigateToGoal_SendGoal;

impl rosidl_runtime_rs::Service for NavigateToGoal_SendGoal {
    type Request = NavigateToGoal_SendGoal_Request;
    type Response = NavigateToGoal_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__NavigateToGoal_SendGoal() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__NavigateToGoal_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__action__NavigateToGoal_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct NavigateToGoal_GetResult;

impl rosidl_runtime_rs::Service for NavigateToGoal_GetResult {
    type Request = NavigateToGoal_GetResult_Request;
    type Response = NavigateToGoal_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__NavigateToGoal_GetResult() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__MoveLift_SendGoal() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__action__MoveLift_SendGoal
#[allow(missing_docs, non_camel_case_types)]
pub struct MoveLift_SendGoal;

impl rosidl_runtime_rs::Service for MoveLift_SendGoal {
    type Request = MoveLift_SendGoal_Request;
    type Response = MoveLift_SendGoal_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__MoveLift_SendGoal() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__MoveLift_GetResult() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__action__MoveLift_GetResult
#[allow(missing_docs, non_camel_case_types)]
pub struct MoveLift_GetResult;

impl rosidl_runtime_rs::Service for MoveLift_GetResult {
    type Request = MoveLift_GetResult_Request;
    type Response = MoveLift_GetResult_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__action__MoveLift_GetResult() }
    }
}


