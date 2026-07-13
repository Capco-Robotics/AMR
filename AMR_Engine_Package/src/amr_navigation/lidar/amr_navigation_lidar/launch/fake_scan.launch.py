from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    fake_scan_node = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="fake_scan_publisher",
        output="screen",
    )

    static_tf_node = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="laser_static_tf",
        output="screen",
        arguments=[
            "0.0",
            "0.0",
            "0.15",
            "0.0",
            "0.0",
            "0.0",
            "base_link",
            "laser",
        ],
    )

    return LaunchDescription([
        fake_scan_node,
        static_tf_node,
    ])