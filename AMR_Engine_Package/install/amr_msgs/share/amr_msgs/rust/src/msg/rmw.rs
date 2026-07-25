#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__EncoderTicks() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__EncoderTicks__init(msg: *mut EncoderTicks) -> bool;
    fn amr_msgs__msg__EncoderTicks__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<EncoderTicks>, size: usize) -> bool;
    fn amr_msgs__msg__EncoderTicks__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<EncoderTicks>);
    fn amr_msgs__msg__EncoderTicks__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<EncoderTicks>, out_seq: *mut rosidl_runtime_rs::Sequence<EncoderTicks>) -> bool;
}

// Corresponds to amr_msgs__msg__EncoderTicks
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EncoderTicks {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub left_ticks: i64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub right_ticks: i64,


    // This member is not documented.
    #[allow(missing_docs)]
    pub dt_ms: u32,

}



impl Default for EncoderTicks {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__EncoderTicks__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__EncoderTicks__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for EncoderTicks {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__EncoderTicks__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__EncoderTicks__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__EncoderTicks__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for EncoderTicks {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for EncoderTicks where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/EncoderTicks";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__EncoderTicks() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__WheelSetpoints() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__WheelSetpoints__init(msg: *mut WheelSetpoints) -> bool;
    fn amr_msgs__msg__WheelSetpoints__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<WheelSetpoints>, size: usize) -> bool;
    fn amr_msgs__msg__WheelSetpoints__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<WheelSetpoints>);
    fn amr_msgs__msg__WheelSetpoints__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<WheelSetpoints>, out_seq: *mut rosidl_runtime_rs::Sequence<WheelSetpoints>) -> bool;
}

// Corresponds to amr_msgs__msg__WheelSetpoints
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]

/// Normalized wheel speed commands.
/// Range: [-1.0, 1.0]
/// -1.0 = full reverse
///  0.0 = stop
/// +1.0 = full forward

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WheelSetpoints {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub left_speed: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub right_speed: f32,

}



impl Default for WheelSetpoints {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__WheelSetpoints__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__WheelSetpoints__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for WheelSetpoints {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__WheelSetpoints__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__WheelSetpoints__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__WheelSetpoints__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for WheelSetpoints {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for WheelSetpoints where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/WheelSetpoints";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__WheelSetpoints() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__LiftCommand() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__LiftCommand__init(msg: *mut LiftCommand) -> bool;
    fn amr_msgs__msg__LiftCommand__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<LiftCommand>, size: usize) -> bool;
    fn amr_msgs__msg__LiftCommand__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<LiftCommand>);
    fn amr_msgs__msg__LiftCommand__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<LiftCommand>, out_seq: *mut rosidl_runtime_rs::Sequence<LiftCommand>) -> bool;
}

// Corresponds to amr_msgs__msg__LiftCommand
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LiftCommand {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub target_position: f32,

}



impl Default for LiftCommand {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__LiftCommand__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__LiftCommand__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for LiftCommand {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__LiftCommand__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__LiftCommand__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__LiftCommand__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for LiftCommand {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for LiftCommand where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/LiftCommand";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__LiftCommand() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__FaultCodes() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__FaultCodes__init(msg: *mut FaultCodes) -> bool;
    fn amr_msgs__msg__FaultCodes__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<FaultCodes>, size: usize) -> bool;
    fn amr_msgs__msg__FaultCodes__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<FaultCodes>);
    fn amr_msgs__msg__FaultCodes__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<FaultCodes>, out_seq: *mut rosidl_runtime_rs::Sequence<FaultCodes>) -> bool;
}

// Corresponds to amr_msgs__msg__FaultCodes
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct FaultCodes {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}

impl FaultCodes {

    // This constant is not documented.
    #[allow(missing_docs)]
    pub const NONE: u8 = 0;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const LIFT_OVERCURRENT: u8 = 1;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const LIFT_UNDERCURRENT: u8 = 2;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const LIFT_SLANT: u8 = 3;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const LIFT_LIMIT_SWITCH: u8 = 4;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const LIFT_SENSOR_FAILURE: u8 = 5;


    // This constant is not documented.
    #[allow(missing_docs)]
    pub const LIFT_TIMEOUT: u8 = 6;

}


impl Default for FaultCodes {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__FaultCodes__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__FaultCodes__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for FaultCodes {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__FaultCodes__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__FaultCodes__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__FaultCodes__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for FaultCodes {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for FaultCodes where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/FaultCodes";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__FaultCodes() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__LiftState() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__LiftState__init(msg: *mut LiftState) -> bool;
    fn amr_msgs__msg__LiftState__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<LiftState>, size: usize) -> bool;
    fn amr_msgs__msg__LiftState__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<LiftState>);
    fn amr_msgs__msg__LiftState__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<LiftState>, out_seq: *mut rosidl_runtime_rs::Sequence<LiftState>) -> bool;
}

// Corresponds to amr_msgs__msg__LiftState
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LiftState {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub position: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub limit_upper: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub limit_lower: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub actuator_position: [f32; 2],


    // This member is not documented.
    #[allow(missing_docs)]
    pub actuator_current: [f32; 2],


    // This member is not documented.
    #[allow(missing_docs)]
    pub level_fault: bool,

}



impl Default for LiftState {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__LiftState__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__LiftState__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for LiftState {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__LiftState__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__LiftState__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__LiftState__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for LiftState {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for LiftState where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/LiftState";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__LiftState() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__SignalCommand() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__SignalCommand__init(msg: *mut SignalCommand) -> bool;
    fn amr_msgs__msg__SignalCommand__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<SignalCommand>, size: usize) -> bool;
    fn amr_msgs__msg__SignalCommand__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<SignalCommand>);
    fn amr_msgs__msg__SignalCommand__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<SignalCommand>, out_seq: *mut rosidl_runtime_rs::Sequence<SignalCommand>) -> bool;
}

// Corresponds to amr_msgs__msg__SignalCommand
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SignalCommand {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub siren_on: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub light_on: bool,


    // This member is not documented.
    #[allow(missing_docs)]
    pub pattern_id: u8,

}



impl Default for SignalCommand {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__SignalCommand__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__SignalCommand__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for SignalCommand {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__SignalCommand__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__SignalCommand__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__SignalCommand__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for SignalCommand {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for SignalCommand where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/SignalCommand";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__SignalCommand() }
  }
}


#[link(name = "amr_msgs__rosidl_typesupport_c")]
extern "C" {
    fn rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__PicoStatus() -> *const std::ffi::c_void;
}

#[link(name = "amr_msgs__rosidl_generator_c")]
extern "C" {
    fn amr_msgs__msg__PicoStatus__init(msg: *mut PicoStatus) -> bool;
    fn amr_msgs__msg__PicoStatus__Sequence__init(seq: *mut rosidl_runtime_rs::Sequence<PicoStatus>, size: usize) -> bool;
    fn amr_msgs__msg__PicoStatus__Sequence__fini(seq: *mut rosidl_runtime_rs::Sequence<PicoStatus>);
    fn amr_msgs__msg__PicoStatus__Sequence__copy(in_seq: &rosidl_runtime_rs::Sequence<PicoStatus>, out_seq: *mut rosidl_runtime_rs::Sequence<PicoStatus>) -> bool;
}

// Corresponds to amr_msgs__msg__PicoStatus
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]


// This struct is not documented.
#[allow(missing_docs)]

#[repr(C)]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PicoStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::rmw::Header,


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

}



impl Default for PicoStatus {
  fn default() -> Self {
    unsafe {
      let mut msg = std::mem::zeroed();
      if !amr_msgs__msg__PicoStatus__init(&mut msg as *mut _) {
        panic!("Call to amr_msgs__msg__PicoStatus__init() failed");
      }
      msg
    }
  }
}

impl rosidl_runtime_rs::SequenceAlloc for PicoStatus {
  fn sequence_init(seq: &mut rosidl_runtime_rs::Sequence<Self>, size: usize) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__PicoStatus__Sequence__init(seq as *mut _, size) }
  }
  fn sequence_fini(seq: &mut rosidl_runtime_rs::Sequence<Self>) {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__PicoStatus__Sequence__fini(seq as *mut _) }
  }
  fn sequence_copy(in_seq: &rosidl_runtime_rs::Sequence<Self>, out_seq: &mut rosidl_runtime_rs::Sequence<Self>) -> bool {
    // SAFETY: This is safe since the pointer is guaranteed to be valid/initialized.
    unsafe { amr_msgs__msg__PicoStatus__Sequence__copy(in_seq, out_seq as *mut _) }
  }
}

impl rosidl_runtime_rs::Message for PicoStatus {
  type RmwMsg = Self;
  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> { msg_cow }
  fn from_rmw_message(msg: Self::RmwMsg) -> Self { msg }
}

impl rosidl_runtime_rs::RmwMessage for PicoStatus where Self: Sized {
  const TYPE_NAME: &'static str = "amr_msgs/msg/PicoStatus";
  fn get_type_support() -> *const std::ffi::c_void {
    // SAFETY: No preconditions for this function.
    unsafe { rosidl_typesupport_c__get_message_type_support_handle__amr_msgs__msg__PicoStatus() }
  }
}


