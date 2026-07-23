from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    front_laser_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='front_laser_static_tf',
        arguments=[
            '0', '0', '0',
            '0', '0', '0',
            'base_link',
            'front_laser'
        ],
        output='screen',
    )

    rear_laser_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='rear_laser_static_tf',
        arguments=[
            '0', '0', '0',
            '0', '0', '0',
            'base_link',
            'rear_laser'
        ],
        output='screen',
    )

    return LaunchDescription([
        front_laser_tf,
        rear_laser_tf,
    ])