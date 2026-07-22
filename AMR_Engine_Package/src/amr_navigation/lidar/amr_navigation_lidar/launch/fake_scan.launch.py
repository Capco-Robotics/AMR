from launch import LaunchDescription
from launch_ros.actions import Node



def generate_launch_description():

    fake_scan_node = Node(
        package="amr_navigation_lidar",
        executable="fake_scan_publisher",
        name="fake_scan_publisher",
        output="screen",
    )


    return LaunchDescription([
    fake_scan_node,
    ])