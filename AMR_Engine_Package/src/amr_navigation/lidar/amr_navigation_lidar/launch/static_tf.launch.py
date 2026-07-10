from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='laser_static_tf',
            arguments=[
                '0', '0', '0.15',     # x y z
                '0', '0', '0',        # roll pitch yaw
                'base_link',
                'laser'
            ],
            output='screen',
        ),
    ])