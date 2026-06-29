"""Includes nav2_bringup's navigation_launch.py with our params."""
import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    params_file = os.path.join(
        get_package_share_directory('amr_navigation_map'),
        'config', 'nav2_params.yaml',
    )
    nav2_launch_dir = os.path.join(
        get_package_share_directory('nav2_bringup'), 'launch',
    )
    return LaunchDescription([
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_launch_dir, 'navigation_launch.py')),
            launch_arguments={'params_file': params_file}.items(),
        ),
    ])
