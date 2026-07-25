from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
from launch_ros.actions import Node

import os


def generate_launch_description():

    noise = LaunchConfiguration("noise")
    rviz = LaunchConfiguration("rviz")
    nav = LaunchConfiguration("nav")
    scan_topic = LaunchConfiguration("scan_topic")

    map_pkg = get_package_share_directory("amr_navigation_map")
    lidar_pkg = get_package_share_directory("amr_navigation_lidar")
    description_pkg = get_package_share_directory("amr_description")

    description_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                description_pkg,
                "launch",
                "description.launch.py",
            )
        )
    )

    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                lidar_pkg,
                "launch",
                "fake_scan.launch.py",
            )
        ),
        launch_arguments={
            "noise": noise,
        }.items(),
    )

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                map_pkg,
                "launch",
                "slam.launch.py",
            )
        )
    )

    nav_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                map_pkg,
                "launch",
                "nav2.launch.py",
            )
        ),
        condition=IfCondition(nav),
        launch_arguments={
            "use_sim_time": "false",
            "scan_topic": scan_topic,
        }.items(),
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "noise",
            default_value="false",
        ),

        DeclareLaunchArgument(
            "rviz",
            default_value="true",
        ),

        DeclareLaunchArgument(
            "nav",
            default_value="false",
        ),

        DeclareLaunchArgument(
            "scan_topic",
            default_value="/scan",
        ),

        description_launch,

        Node(
            package="amr_navigation_move",
            executable="fake_pico_node",
            name="fake_pico_node",
            output="screen",
            parameters=[
                {"use_sim_time": False}
            ],
        ),

        Node(
            package="amr_navigation_move",
            executable="drive_controller_node",
            name="drive_controller_node",
            output="screen",
            parameters=[
                {"use_sim_time": False}
            ],
        ),

        Node(
            package="amr_navigation_move",
            executable="odometry_node",
            name="odometry_node",
            output="screen",
            parameters=[
                {"use_sim_time": False}
            ],
        ),

        lidar_launch,
        slam_launch,
        nav_launch,

        Node(
            package="rviz2",
            executable="rviz2",
            name="rviz2",
            output="screen",
            condition=IfCondition(rviz),
            arguments=[
                "-d",
                os.path.join(
                    map_pkg,
                    "config",
                    "slam_sim.rviz",
                ),
            ],
        ),
    ])