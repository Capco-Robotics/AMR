"""Top-level launch file: loads and initializes every AMR package.

This is the literal "load different packages and initialize them"
mechanism -- ROS2 starts nodes via launch files, not by one node spawning
others, so the actual bringup work happens here while amr_engine.py /
state_machine_node.py hold the supervisor logic.
"""
from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(package='amr_pico_bridge', executable='bridge_node', name='amr_pico_bridge'),
        Node(package='amr_navigation_move', executable='drive_controller_node', name='drive_controller'),
        Node(package='amr_navigation_move', executable='odometry_node', name='odometry'),
        Node(package='amr_lift', executable='lift_control_node', name='amr_lift'),
        Node(package='amr_error', executable='signal_system_node', name='amr_error'),
        Node(package='amr_charging', executable='bms_node', name='amr_charging'),
        Node(package='amr_command', executable='command_gateway_node', name='amr_command'),
        Node(package='amr_engine', executable='amr_engine', name='amr_engine'),
        # amr_navigation_map (SLAM/Nav2) is intentionally launched separately
        # via amr_navigation_map/launch/slam.launch.py and nav2.launch.py,
        # since they're swapped in/out depending on mapping vs. localization mode.
    ])
