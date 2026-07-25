"""Launch AMR simulation together with Nav2."""

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    package_dir = get_package_share_directory("amr_navigation_map")

    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                package_dir,
                "launch",
                "sim.launch.py",
            )
        ),
        launch_arguments={
            "nav": "false",
        }.items(),
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                package_dir,
                "launch",
                "nav2.launch.py",
            )
        )
    )

    return LaunchDescription([
        sim_launch,
        nav2_launch,
    ])
