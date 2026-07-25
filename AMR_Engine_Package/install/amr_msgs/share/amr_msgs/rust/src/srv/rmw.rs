#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__ResetOdometry_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__ResetOdometry_Request__init(msg: *mut ResetOdometry_Request) -> bool;
    fn amr_msgs__srv__ResetOdometry_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetOdometry_Request>, size: usize) -> bool;
    fn amr_msgs__srv__ResetOdometry_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetOdometry_Request>);
    fn amr_msgs__srv__ResetOdometry_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetOdometry_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetOdometry_Request>) -> bool;
}

// Corresponds to amr_msgs__srv__ResetOdometry_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetOdometry_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub x: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub y: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub theta: f32,

}



impl Default for ResetOdometry_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__ResetOdometry_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__ResetOdometry_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetOdometry_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__ResetOdometry_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__ResetOdometry_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__ResetOdometry_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetOdometry_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetOdometry_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/ResetOdometry_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__ResetOdometry_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__ResetOdometry_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__ResetOdometry_Response__init(msg: *mut ResetOdometry_Response) -> bool;
    fn amr_msgs__srv__ResetOdometry_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<ResetOdometry_Response>, size: usize) -> bool;
    fn amr_msgs__srv__ResetOdometry_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<ResetOdometry_Response>);
    fn amr_msgs__srv__ResetOdometry_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<ResetOdometry_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<ResetOdometry_Response>) -> bool;
}

// Corresponds to amr_msgs__srv__ResetOdometry_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetOdometry_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for ResetOdometry_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__ResetOdometry_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__ResetOdometry_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for ResetOdometry_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__ResetOdometry_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__ResetOdometry_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__ResetOdometry_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for ResetOdometry_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for ResetOdometry_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/ResetOdometry_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__ResetOdometry_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetRobotState_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__GetRobotState_Request__init(msg: *mut GetRobotState_Request) -> bool;
    fn amr_msgs__srv__GetRobotState_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetRobotState_Request>, size: usize) -> bool;
    fn amr_msgs__srv__GetRobotState_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetRobotState_Request>);
    fn amr_msgs__srv__GetRobotState_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetRobotState_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetRobotState_Request>) -> bool;
}

// Corresponds to amr_msgs__srv__GetRobotState_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetRobotState_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetRobotState_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__GetRobotState_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__GetRobotState_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetRobotState_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetRobotState_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetRobotState_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetRobotState_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetRobotState_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetRobotState_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/GetRobotState_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetRobotState_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetRobotState_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__GetRobotState_Response__init(msg: *mut GetRobotState_Response) -> bool;
    fn amr_msgs__srv__GetRobotState_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetRobotState_Response>, size: usize) -> bool;
    fn amr_msgs__srv__GetRobotState_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetRobotState_Response>);
    fn amr_msgs__srv__GetRobotState_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetRobotState_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetRobotState_Response>) -> bool;
}

// Corresponds to amr_msgs__srv__GetRobotState_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetRobotState_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub state: rosidl_runtime_rs::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub active_faults: rosidl_runtime_rs::Sequence<rosidl_runtime_rs::String>,

}



impl Default for GetRobotState_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__GetRobotState_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__GetRobotState_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetRobotState_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetRobotState_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetRobotState_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetRobotState_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetRobotState_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetRobotState_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/GetRobotState_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetRobotState_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__AcknowledgeFault_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__AcknowledgeFault_Request__init(msg: *mut AcknowledgeFault_Request) -> bool;
    fn amr_msgs__srv__AcknowledgeFault_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AcknowledgeFault_Request>, size: usize) -> bool;
    fn amr_msgs__srv__AcknowledgeFault_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AcknowledgeFault_Request>);
    fn amr_msgs__srv__AcknowledgeFault_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AcknowledgeFault_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<AcknowledgeFault_Request>) -> bool;
}

// Corresponds to amr_msgs__srv__AcknowledgeFault_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AcknowledgeFault_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub fault_id: rosidl_runtime_rs::String,

}



impl Default for AcknowledgeFault_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__AcknowledgeFault_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__AcknowledgeFault_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AcknowledgeFault_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__AcknowledgeFault_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__AcknowledgeFault_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__AcknowledgeFault_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AcknowledgeFault_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AcknowledgeFault_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/AcknowledgeFault_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__AcknowledgeFault_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__AcknowledgeFault_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__AcknowledgeFault_Response__init(msg: *mut AcknowledgeFault_Response) -> bool;
    fn amr_msgs__srv__AcknowledgeFault_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<AcknowledgeFault_Response>, size: usize) -> bool;
    fn amr_msgs__srv__AcknowledgeFault_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<AcknowledgeFault_Response>);
    fn amr_msgs__srv__AcknowledgeFault_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<AcknowledgeFault_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<AcknowledgeFault_Response>) -> bool;
}

// Corresponds to amr_msgs__srv__AcknowledgeFault_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AcknowledgeFault_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for AcknowledgeFault_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__AcknowledgeFault_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__AcknowledgeFault_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for AcknowledgeFault_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__AcknowledgeFault_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__AcknowledgeFault_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__AcknowledgeFault_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for AcknowledgeFault_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for AcknowledgeFault_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/AcknowledgeFault_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__AcknowledgeFault_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetLiftTarget_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__SetLiftTarget_Request__init(msg: *mut SetLiftTarget_Request) -> bool;
    fn amr_msgs__srv__SetLiftTarget_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetLiftTarget_Request>, size: usize) -> bool;
    fn amr_msgs__srv__SetLiftTarget_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetLiftTarget_Request>);
    fn amr_msgs__srv__SetLiftTarget_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetLiftTarget_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<SetLiftTarget_Request>) -> bool;
}

// Corresponds to amr_msgs__srv__SetLiftTarget_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetLiftTarget_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub target_position: f32,

}



impl Default for SetLiftTarget_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__SetLiftTarget_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__SetLiftTarget_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetLiftTarget_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetLiftTarget_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetLiftTarget_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetLiftTarget_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetLiftTarget_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetLiftTarget_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/SetLiftTarget_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetLiftTarget_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetLiftTarget_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__SetLiftTarget_Response__init(msg: *mut SetLiftTarget_Response) -> bool;
    fn amr_msgs__srv__SetLiftTarget_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetLiftTarget_Response>, size: usize) -> bool;
    fn amr_msgs__srv__SetLiftTarget_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetLiftTarget_Response>);
    fn amr_msgs__srv__SetLiftTarget_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetLiftTarget_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<SetLiftTarget_Response>) -> bool;
}

// Corresponds to amr_msgs__srv__SetLiftTarget_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetLiftTarget_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,

}



impl Default for SetLiftTarget_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__SetLiftTarget_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__SetLiftTarget_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetLiftTarget_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetLiftTarget_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetLiftTarget_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetLiftTarget_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetLiftTarget_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetLiftTarget_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/SetLiftTarget_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetLiftTarget_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetPicoStatus_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__GetPicoStatus_Request__init(msg: *mut GetPicoStatus_Request) -> bool;
    fn amr_msgs__srv__GetPicoStatus_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetPicoStatus_Request>, size: usize) -> bool;
    fn amr_msgs__srv__GetPicoStatus_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetPicoStatus_Request>);
    fn amr_msgs__srv__GetPicoStatus_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetPicoStatus_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<GetPicoStatus_Request>) -> bool;
}

// Corresponds to amr_msgs__srv__GetPicoStatus_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetPicoStatus_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetPicoStatus_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__GetPicoStatus_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__GetPicoStatus_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetPicoStatus_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetPicoStatus_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetPicoStatus_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetPicoStatus_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetPicoStatus_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetPicoStatus_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/GetPicoStatus_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetPicoStatus_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetPicoStatus_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__GetPicoStatus_Response__init(msg: *mut GetPicoStatus_Response) -> bool;
    fn amr_msgs__srv__GetPicoStatus_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<GetPicoStatus_Response>, size: usize) -> bool;
    fn amr_msgs__srv__GetPicoStatus_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<GetPicoStatus_Response>);
    fn amr_msgs__srv__GetPicoStatus_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<GetPicoStatus_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<GetPicoStatus_Response>) -> bool;
}

// Corresponds to amr_msgs__srv__GetPicoStatus_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetPicoStatus_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub uptime_ms: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub last_rpi_msg_age_ms: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub watchdog_resets: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub free_mem_bytes: u32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub available: bool,

}



impl Default for GetPicoStatus_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__GetPicoStatus_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__GetPicoStatus_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for GetPicoStatus_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetPicoStatus_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetPicoStatus_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__GetPicoStatus_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for GetPicoStatus_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for GetPicoStatus_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/GetPicoStatus_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__GetPicoStatus_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetDriveLimits_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__SetDriveLimits_Request__init(msg: *mut SetDriveLimits_Request) -> bool;
    fn amr_msgs__srv__SetDriveLimits_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetDriveLimits_Request>, size: usize) -> bool;
    fn amr_msgs__srv__SetDriveLimits_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetDriveLimits_Request>);
    fn amr_msgs__srv__SetDriveLimits_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetDriveLimits_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<SetDriveLimits_Request>) -> bool;
}

// Corresponds to amr_msgs__srv__SetDriveLimits_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetDriveLimits_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub max_linear_mps: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub max_angular_rps: f32,

}



impl Default for SetDriveLimits_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__SetDriveLimits_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__SetDriveLimits_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetDriveLimits_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetDriveLimits_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetDriveLimits_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetDriveLimits_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetDriveLimits_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetDriveLimits_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/SetDriveLimits_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetDriveLimits_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetDriveLimits_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__SetDriveLimits_Response__init(msg: *mut SetDriveLimits_Response) -> bool;
    fn amr_msgs__srv__SetDriveLimits_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SetDriveLimits_Response>, size: usize) -> bool;
    fn amr_msgs__srv__SetDriveLimits_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SetDriveLimits_Response>);
    fn amr_msgs__srv__SetDriveLimits_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SetDriveLimits_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<SetDriveLimits_Response>) -> bool;
}

// Corresponds to amr_msgs__srv__SetDriveLimits_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetDriveLimits_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,

}



impl Default for SetDriveLimits_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__SetDriveLimits_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__SetDriveLimits_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SetDriveLimits_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetDriveLimits_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetDriveLimits_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__SetDriveLimits_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SetDriveLimits_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SetDriveLimits_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/SetDriveLimits_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__SetDriveLimits_Response() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__TriggerEstop_Request() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__TriggerEstop_Request__init(msg: *mut TriggerEstop_Request) -> bool;
    fn amr_msgs__srv__TriggerEstop_Request__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<TriggerEstop_Request>, size: usize) -> bool;
    fn amr_msgs__srv__TriggerEstop_Request__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<TriggerEstop_Request>);
    fn amr_msgs__srv__TriggerEstop_Request__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<TriggerEstop_Request>, out_seq: *mut rosidl_runtime_rs::Sequence<TriggerEstop_Request>) -> bool;
}

// Corresponds to amr_msgs__srv__TriggerEstop_Request
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TriggerEstop_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub release: bool,

}



impl Default for TriggerEstop_Request {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__TriggerEstop_Request__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__TriggerEstop_Request__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for TriggerEstop_Request {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__TriggerEstop_Request__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__TriggerEstop_Request__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__TriggerEstop_Request__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for TriggerEstop_Request {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for TriggerEstop_Request where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/TriggerEstop_Request";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__TriggerEstop_Request() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__TriggerEstop_Response() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__srv__TriggerEstop_Response__init(msg: *mut TriggerEstop_Response) -> bool;
    fn amr_msgs__srv__TriggerEstop_Response__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<TriggerEstop_Response>, size: usize) -> bool;
    fn amr_msgs__srv__TriggerEstop_Response__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<TriggerEstop_Response>);
    fn amr_msgs__srv__TriggerEstop_Response__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<TriggerEstop_Response>, out_seq: *mut rosidl_runtime_rs::Sequence<TriggerEstop_Response>) -> bool;
}

// Corresponds to amr_msgs__srv__TriggerEstop_Response
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TriggerEstop_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for TriggerEstop_Response {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__srv__TriggerEstop_Response__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__srv__TriggerEstop_Response__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for TriggerEstop_Response {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__TriggerEstop_Response__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__TriggerEstop_Response__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__srv__TriggerEstop_Response__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for TriggerEstop_Response {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for TriggerEstop_Response where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/srv/TriggerEstop_Response";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__srv__TriggerEstop_Response() }
  }
}






#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__ResetOdometry() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__srv__ResetOdometry
#[allow(missing_docs, non_camel_case_types)]
pub struct ResetOdometry;

impl rosidl_runtime_rs::Service for ResetOdometry {
    type Request = ResetOdometry_Request;
    type Response = ResetOdometry_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__ResetOdometry() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__GetRobotState() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__srv__GetRobotState
#[allow(missing_docs, non_camel_case_types)]
pub struct GetRobotState;

impl rosidl_runtime_rs::Service for GetRobotState {
    type Request = GetRobotState_Request;
    type Response = GetRobotState_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__GetRobotState() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__AcknowledgeFault() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__srv__AcknowledgeFault
#[allow(missing_docs, non_camel_case_types)]
pub struct AcknowledgeFault;

impl rosidl_runtime_rs::Service for AcknowledgeFault {
    type Request = AcknowledgeFault_Request;
    type Response = AcknowledgeFault_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__AcknowledgeFault() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__SetLiftTarget() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__srv__SetLiftTarget
#[allow(missing_docs, non_camel_case_types)]
pub struct SetLiftTarget;

impl rosidl_runtime_rs::Service for SetLiftTarget {
    type Request = SetLiftTarget_Request;
    type Response = SetLiftTarget_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__SetLiftTarget() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__GetPicoStatus() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__srv__GetPicoStatus
#[allow(missing_docs, non_camel_case_types)]
pub struct GetPicoStatus;

impl rosidl_runtime_rs::Service for GetPicoStatus {
    type Request = GetPicoStatus_Request;
    type Response = GetPicoStatus_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__GetPicoStatus() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__SetDriveLimits() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__srv__SetDriveLimits
#[allow(missing_docs, non_camel_case_types)]
pub struct SetDriveLimits;

impl rosidl_runtime_rs::Service for SetDriveLimits {
    type Request = SetDriveLimits_Request;
    type Response = SetDriveLimits_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__SetDriveLimits() }
    }
}




#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__TriggerEstop() -> *const std::ffi::c_void;
}

// Corresponds to amr_msgs__srv__TriggerEstop
#[allow(missing_docs, non_camel_case_types)]
pub struct TriggerEstop;

impl rosidl_runtime_rs::Service for TriggerEstop {
    type Request = TriggerEstop_Request;
    type Response = TriggerEstop_Response;

    fn get_type_support() -> *const std::ffi::c_void {
        // SAFETY: No preconditions for this function.
        unsafe { rosidl_typesupport_c__get_service_type_support_handle__amr_msgs__srv__TriggerEstop() }
    }
}


