import os

from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    # TODO: confirm against real chassis once known
    fake_scan_front = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="fake_scan_publisher_front",
        output="screen",
        parameters=[{
            "scan_topic": "/scan_front",
            "frame_id": "laser_front_left",
            "mount_x": 0.4,
            "mount_y": 0.4,
            "mount_yaw": 0.0,
        }],
    )

    # TODO: confirm against real chassis once known
    fake_scan_rear = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="fake_scan_publisher_rear",
        output="screen",
        parameters=[{
            "scan_topic": "/scan_rear",
            "frame_id": "laser_rear_right",
            "mount_x": -0.4,
            "mount_y": -0.4,
            "mount_yaw": 3.14159,
        }],
    )

    lidar_pkg = get_package_share_directory("amr_navigation_lidar")

    static_tf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                lidar_pkg,
                "launch",
                "static_tf.launch.py",
            )
        )
    )

    return LaunchDescription([
        static_tf_launch,
        fake_scan_front,
        fake_scan_rear,
    ])
