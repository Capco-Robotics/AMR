from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    serial_port = LaunchConfiguration("serial_port")
    baudrate = LaunchConfiguration("baudrate")
    frame_id = LaunchConfiguration("frame_id")

    return LaunchDescription([

        DeclareLaunchArgument(
            "serial_port",
            default_value="/dev/ttyUSB0"
        ),

        DeclareLaunchArgument(
            "baudrate",
            default_value="230400"
        ),

        DeclareLaunchArgument(
            "frame_id",
            default_value="laser"
        ),

        # TODO:
        # Replace this placeholder with ydlidar_ros_driver node
        # after the driver package is added to the workspace.

    ])