from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    fake_scan_node = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="fake_scan_publisher",
        output="screen",
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

    return LaunchDescription([
        fake_scan_node,
        static_tf_launch,
    ])