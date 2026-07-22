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

    return LaunchDescription([
        fake_scan_front,
        fake_scan_rear,
    ])
