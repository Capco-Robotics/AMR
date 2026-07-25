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
        # Confirm executable and parameter names after vendoring
        # ydlidar_ros_driver into the workspace.
        Node(
            package="ydlidar_ros_driver",
            executable="ydlidar_ros_driver_node",
            name="ydlidar_ros_driver",
            output="screen",
            parameters=[
                {
                    "serial_port": serial_port,
                    "baudrate": baudrate,
                    "frame_id": frame_id,
                }
            ],
        ),

    ])