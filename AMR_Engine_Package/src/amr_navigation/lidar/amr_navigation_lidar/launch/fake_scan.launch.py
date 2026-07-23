from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    front_scan_node = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="fake_scan_front",
        output="screen",
        parameters=[
            {
                "scan_topic": "/scan_front",
                "frame_id": "front_laser",
                "mount_x": 0.25,
                "mount_y": 0.0,
                "mount_yaw": 0.0,
            }
        ],
    )

    rear_scan_node = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="fake_scan_rear",
        output="screen",
        parameters=[
            {
                "scan_topic": "/scan_rear",
                "frame_id": "rear_laser",
                "mount_x": -0.25,
                "mount_y": 0.0,
                "mount_yaw": 3.14159,
            }
        ],
    )

    static_tf_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                get_package_share_directory("amr_navigation_lidar"),
                "launch",
                "static_tf.launch.py",
            )
        )
    )

    return LaunchDescription(
        [
            front_scan_node,
            rear_scan_node,
            static_tf_launch,
        ]
    )