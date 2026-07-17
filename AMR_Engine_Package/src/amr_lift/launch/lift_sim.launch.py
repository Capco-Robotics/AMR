from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='amr_lift',
            executable='lift_control_node',
            name='amr_lift',
            output='screen'
        ),
        Node(
            package='amr_lift',
            executable='fake_lift_pico_node',
            name='fake_lift_pico',
            output='screen'
        ),
    ])