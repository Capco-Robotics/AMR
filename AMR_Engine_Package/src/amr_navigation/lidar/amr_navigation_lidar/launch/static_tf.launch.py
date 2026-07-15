from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    laser_tf = Node(
        package='tf2_ros',
        executable='static_transform_publisher',
        name='laser_static_tf',
        arguments=[
            # TODO:
            # Confirm both LiDAR mount poses (x, y, z, yaw)
            # after hardware installation.
            # Keep this file as the single source of truth
            # for all LiDAR static transforms.

            '0', '0', '0.0',      # x y z

            # yaw pitch roll
            '0', '0', '0',

            'base_link',
            'laser'
        ],
        output='screen',
    )

    # Future second LiDAR transform.
    # TODO:
    # Add another static_transform_publisher here
    # when the rear LiDAR is installed.

    return LaunchDescription([
        laser_tf,
    ])