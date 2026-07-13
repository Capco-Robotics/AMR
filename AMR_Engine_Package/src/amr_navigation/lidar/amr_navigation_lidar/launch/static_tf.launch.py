from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='laser_static_tf',
            arguments=[
                # TODO:
                # Measure the actual LiDAR mounting position after hardware installation.
                '0', '0', '0.0',      # x y z

                # yaw pitch roll
                '0', '0', '0',

                'base_link',
                'laser'
            ],
            output='screen',
        ),
    ])