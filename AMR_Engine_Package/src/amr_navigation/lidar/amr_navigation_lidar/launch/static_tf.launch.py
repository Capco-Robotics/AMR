from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():

    front_laser_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="front_laser_static_tf",
        arguments=[
            "0.4", "0.4", "0.0",
            "0", "0", "0",
            "base_link",
            "laser_front_left",
        ],
        output="screen",
    )

    rear_laser_tf = Node(
        package="tf2_ros",
        executable="static_transform_publisher",
        name="rear_laser_static_tf",
        arguments=[
            "-0.4", "-0.4", "0.0",
            "3.14159", "0", "0",
            "base_link",
            "laser_rear_right",
        ],
        output="screen",
    )

    return LaunchDescription([
        front_laser_tf,
        rear_laser_tf,
    ])