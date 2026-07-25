#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};




// Corresponds to amr_msgs__srv__ResetOdometry_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::ResetOdometry_Request::default())
  }
}

impl rosidl_runtime_rs::Message for ResetOdometry_Request {
  type RmwMsg = super::srv::rmw::ResetOdometry_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        x: msg.x,
        y: msg.y,
        theta: msg.theta,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      x: msg.x,
      y: msg.y,
      theta: msg.theta,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      x: msg.x,
      y: msg.y,
      theta: msg.theta,
    }
  }
}


// Corresponds to amr_msgs__srv__ResetOdometry_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct ResetOdometry_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for ResetOdometry_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::ResetOdometry_Response::default())
  }
}

impl rosidl_runtime_rs::Message for ResetOdometry_Response {
  type RmwMsg = super::srv::rmw::ResetOdometry_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
    }
  }
}


// Corresponds to amr_msgs__srv__GetRobotState_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetRobotState_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetRobotState_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetRobotState_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetRobotState_Request {
  type RmwMsg = super::srv::rmw::GetRobotState_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
    }
  }
}


// Corresponds to amr_msgs__srv__GetRobotState_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetRobotState_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub state: std::string::String,


    // This member is not documented.
    #[allow(missing_docs)]
    pub active_faults: Vec<std::string::String>,

}



impl Default for GetRobotState_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetRobotState_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetRobotState_Response {
  type RmwMsg = super::srv::rmw::GetRobotState_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        state: msg.state.as_str().into(),
        active_faults: msg.active_faults
          .into_iter()
          .map(|elem| elem.as_str().into())
          .collect(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        state: msg.state.as_str().into(),
        active_faults: msg.active_faults
          .iter()
          .map(|elem| elem.as_str().into())
          .collect(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      state: msg.state.to_string(),
      active_faults: msg.active_faults
          .into_iter()
          .map(|elem| elem.to_string())
          .collect(),
    }
  }
}


// Corresponds to amr_msgs__srv__AcknowledgeFault_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AcknowledgeFault_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub fault_id: std::string::String,

}



impl Default for AcknowledgeFault_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AcknowledgeFault_Request::default())
  }
}

impl rosidl_runtime_rs::Message for AcknowledgeFault_Request {
  type RmwMsg = super::srv::rmw::AcknowledgeFault_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        fault_id: msg.fault_id.as_str().into(),
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        fault_id: msg.fault_id.as_str().into(),
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      fault_id: msg.fault_id.to_string(),
    }
  }
}


// Corresponds to amr_msgs__srv__AcknowledgeFault_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct AcknowledgeFault_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for AcknowledgeFault_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::AcknowledgeFault_Response::default())
  }
}

impl rosidl_runtime_rs::Message for AcknowledgeFault_Response {
  type RmwMsg = super::srv::rmw::AcknowledgeFault_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
    }
  }
}


// Corresponds to amr_msgs__srv__SetLiftTarget_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetLiftTarget_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub target_position: f32,

}



impl Default for SetLiftTarget_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetLiftTarget_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SetLiftTarget_Request {
  type RmwMsg = super::srv::rmw::SetLiftTarget_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        target_position: msg.target_position,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      target_position: msg.target_position,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      target_position: msg.target_position,
    }
  }
}


// Corresponds to amr_msgs__srv__SetLiftTarget_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetLiftTarget_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,

}



impl Default for SetLiftTarget_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetLiftTarget_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SetLiftTarget_Response {
  type RmwMsg = super::srv::rmw::SetLiftTarget_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        accepted: msg.accepted,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      accepted: msg.accepted,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      accepted: msg.accepted,
    }
  }
}


// Corresponds to amr_msgs__srv__GetPicoStatus_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct GetPicoStatus_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub structure_needs_at_least_one_member: u8,

}



impl Default for GetPicoStatus_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetPicoStatus_Request::default())
  }
}

impl rosidl_runtime_rs::Message for GetPicoStatus_Request {
  type RmwMsg = super::srv::rmw::GetPicoStatus_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      structure_needs_at_least_one_member: msg.structure_needs_at_least_one_member,
    }
  }
}


// Corresponds to amr_msgs__srv__GetPicoStatus_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::GetPicoStatus_Response::default())
  }
}

impl rosidl_runtime_rs::Message for GetPicoStatus_Response {
  type RmwMsg = super::srv::rmw::GetPicoStatus_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        uptime_ms: msg.uptime_ms,
        last_rpi_msg_age_ms: msg.last_rpi_msg_age_ms,
        watchdog_resets: msg.watchdog_resets,
        free_mem_bytes: msg.free_mem_bytes,
        available: msg.available,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      uptime_ms: msg.uptime_ms,
      last_rpi_msg_age_ms: msg.last_rpi_msg_age_ms,
      watchdog_resets: msg.watchdog_resets,
      free_mem_bytes: msg.free_mem_bytes,
      available: msg.available,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      uptime_ms: msg.uptime_ms,
      last_rpi_msg_age_ms: msg.last_rpi_msg_age_ms,
      watchdog_resets: msg.watchdog_resets,
      free_mem_bytes: msg.free_mem_bytes,
      available: msg.available,
    }
  }
}


// Corresponds to amr_msgs__srv__SetDriveLimits_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetDriveLimits_Request::default())
  }
}

impl rosidl_runtime_rs::Message for SetDriveLimits_Request {
  type RmwMsg = super::srv::rmw::SetDriveLimits_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        max_linear_mps: msg.max_linear_mps,
        max_angular_rps: msg.max_angular_rps,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      max_linear_mps: msg.max_linear_mps,
      max_angular_rps: msg.max_angular_rps,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      max_linear_mps: msg.max_linear_mps,
      max_angular_rps: msg.max_angular_rps,
    }
  }
}


// Corresponds to amr_msgs__srv__SetDriveLimits_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SetDriveLimits_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub accepted: bool,

}



impl Default for SetDriveLimits_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::SetDriveLimits_Response::default())
  }
}

impl rosidl_runtime_rs::Message for SetDriveLimits_Response {
  type RmwMsg = super::srv::rmw::SetDriveLimits_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        accepted: msg.accepted,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      accepted: msg.accepted,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      accepted: msg.accepted,
    }
  }
}


// Corresponds to amr_msgs__srv__TriggerEstop_Request

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TriggerEstop_Request {

    // This member is not documented.
    #[allow(missing_docs)]
    pub release: bool,

}



impl Default for TriggerEstop_Request {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::TriggerEstop_Request::default())
  }
}

impl rosidl_runtime_rs::Message for TriggerEstop_Request {
  type RmwMsg = super::srv::rmw::TriggerEstop_Request;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        release: msg.release,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      release: msg.release,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      release: msg.release,
    }
  }
}


// Corresponds to amr_msgs__srv__TriggerEstop_Response

// This struct is not documented.
#[allow(missing_docs)]

#[allow(non_camel_case_types)]
#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct TriggerEstop_Response {

    // This member is not documented.
    #[allow(missing_docs)]
    pub success: bool,

}



impl Default for TriggerEstop_Response {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::srv::rmw::TriggerEstop_Response::default())
  }
}

impl rosidl_runtime_rs::Message for TriggerEstop_Response {
  type RmwMsg = super::srv::rmw::TriggerEstop_Response;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        success: msg.success,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
      success: msg.success,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      success: msg.success,
    }
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


