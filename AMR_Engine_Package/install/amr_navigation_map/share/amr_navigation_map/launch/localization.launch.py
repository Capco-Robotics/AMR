import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def generate_launch_description():

    map_file_name = LaunchConfiguration("map_file_name")

    params_file = os.path.join(
        get_package_share_directory("amr_navigation_map"),
        "config",
        "slam_toolbox_localization_params.yaml",
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            "map_file_name",
            description="Absolute path to slam toolbox posegraph file",
        ),

        Node(
            package="slam_toolbox",
            executable="localization_slam_toolbox_node",
            name="slam_toolbox",
            output="screen",
            parameters=[
                params_file,
                {
                    "map_file_name": map_file_name
                }
            ],
        ),
    ])