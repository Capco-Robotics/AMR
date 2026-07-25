#[cfg(feature = "serde")]
use serde::{Deserialize, Serialize};



// Corresponds to amr_msgs__msg__EncoderTicks

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct EncoderTicks {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::EncoderTicks::default())
  }
}

impl rosidl_runtime_rs::Message for EncoderTicks {
  type RmwMsg = super::msg::rmw::EncoderTicks;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        left_ticks: msg.left_ticks,
        right_ticks: msg.right_ticks,
        dt_ms: msg.dt_ms,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      left_ticks: msg.left_ticks,
      right_ticks: msg.right_ticks,
      dt_ms: msg.dt_ms,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      left_ticks: msg.left_ticks,
      right_ticks: msg.right_ticks,
      dt_ms: msg.dt_ms,
    }
  }
}


// Corresponds to amr_msgs__msg__WheelSetpoints
/// Normalized wheel speed commands.
/// Range: [-1.0, 1.0]
/// -1.0 = full reverse
///  0.0 = stop
/// +1.0 = full forward

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct WheelSetpoints {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub left_speed: f32,


    // This member is not documented.
    #[allow(missing_docs)]
    pub right_speed: f32,

}



impl Default for WheelSetpoints {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::WheelSetpoints::default())
  }
}

impl rosidl_runtime_rs::Message for WheelSetpoints {
  type RmwMsg = super::msg::rmw::WheelSetpoints;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        left_speed: msg.left_speed,
        right_speed: msg.right_speed,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      left_speed: msg.left_speed,
      right_speed: msg.right_speed,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      left_speed: msg.left_speed,
      right_speed: msg.right_speed,
    }
  }
}


// Corresponds to amr_msgs__msg__LiftCommand

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LiftCommand {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


    // This member is not documented.
    #[allow(missing_docs)]
    pub target_position: f32,

}



impl Default for LiftCommand {
  fn default() -> Self {
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::LiftCommand::default())
  }
}

impl rosidl_runtime_rs::Message for LiftCommand {
  type RmwMsg = super::msg::rmw::LiftCommand;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        target_position: msg.target_position,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      target_position: msg.target_position,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      target_position: msg.target_position,
    }
  }
}


// Corresponds to amr_msgs__msg__FaultCodes

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::FaultCodes::default())
  }
}

impl rosidl_runtime_rs::Message for FaultCodes {
  type RmwMsg = super::msg::rmw::FaultCodes;

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


// Corresponds to amr_msgs__msg__LiftState

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct LiftState {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::LiftState::default())
  }
}

impl rosidl_runtime_rs::Message for LiftState {
  type RmwMsg = super::msg::rmw::LiftState;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        position: msg.position,
        limit_upper: msg.limit_upper,
        limit_lower: msg.limit_lower,
        actuator_position: msg.actuator_position,
        actuator_current: msg.actuator_current,
        level_fault: msg.level_fault,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      position: msg.position,
      limit_upper: msg.limit_upper,
      limit_lower: msg.limit_lower,
        actuator_position: msg.actuator_position,
        actuator_current: msg.actuator_current,
      level_fault: msg.level_fault,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      position: msg.position,
      limit_upper: msg.limit_upper,
      limit_lower: msg.limit_lower,
      actuator_position: msg.actuator_position,
      actuator_current: msg.actuator_current,
      level_fault: msg.level_fault,
    }
  }
}


// Corresponds to amr_msgs__msg__SignalCommand

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct SignalCommand {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::SignalCommand::default())
  }
}

impl rosidl_runtime_rs::Message for SignalCommand {
  type RmwMsg = super::msg::rmw::SignalCommand;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        siren_on: msg.siren_on,
        light_on: msg.light_on,
        pattern_id: msg.pattern_id,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      siren_on: msg.siren_on,
      light_on: msg.light_on,
      pattern_id: msg.pattern_id,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      siren_on: msg.siren_on,
      light_on: msg.light_on,
      pattern_id: msg.pattern_id,
    }
  }
}


// Corresponds to amr_msgs__msg__PicoStatus

// This struct is not documented.
#[allow(missing_docs)]

#[cfg_attr(feature = "serde", derive(Deserialize, Serialize))]
#[derive(Clone, Debug, PartialEq, PartialOrd)]
pub struct PicoStatus {

    // This member is not documented.
    #[allow(missing_docs)]
    pub header: std_msgs::msg::Header,


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
    <Self as rosidl_runtime_rs::Message>::from_rmw_message(super::msg::rmw::PicoStatus::default())
  }
}

impl rosidl_runtime_rs::Message for PicoStatus {
  type RmwMsg = super::msg::rmw::PicoStatus;

  fn into_rmw_message(msg_cow: std::borrow::Cow<'_, Self>) -> std::borrow::Cow<'_, Self::RmwMsg> {
    match msg_cow {
      std::borrow::Cow::Owned(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Owned(msg.header)).into_owned(),
        uptime_ms: msg.uptime_ms,
        last_rpi_msg_age_ms: msg.last_rpi_msg_age_ms,
        watchdog_resets: msg.watchdog_resets,
        free_mem_bytes: msg.free_mem_bytes,
      }),
      std::borrow::Cow::Borrowed(msg) => std::borrow::Cow::Owned(Self::RmwMsg {
        header: std_msgs::msg::Header::into_rmw_message(std::borrow::Cow::Borrowed(&msg.header)).into_owned(),
      uptime_ms: msg.uptime_ms,
      last_rpi_msg_age_ms: msg.last_rpi_msg_age_ms,
      watchdog_resets: msg.watchdog_resets,
      free_mem_bytes: msg.free_mem_bytes,
      })
    }
  }

  fn from_rmw_message(msg: Self::RmwMsg) -> Self {
    Self {
      header: std_msgs::msg::Header::from_rmw_message(msg.header),
      uptime_ms: msg.uptime_ms,
      last_rpi_msg_age_ms: msg.last_rpi_msg_age_ms,
      watchdog_resets: msg.watchdog_resets,
      free_mem_bytes: msg.free_mem_bytes,
    }
  }
}


