from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    # One pose-aware arena simulator now produces all three scan topics:
    #   /scan_front (laser_front_left), /scan_rear (laser_rear_right),
    #   and the merged /scan (base_link) that SLAM + Nav2 consume.
    arena_scan_sim = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="arena_scan_sim",
        output="screen",
    )

    return LaunchDescription([
        arena_scan_sim,
    ])
