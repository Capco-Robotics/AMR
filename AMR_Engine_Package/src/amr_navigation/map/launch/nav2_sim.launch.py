"""Launch simulation together with Nav2."""

import os

from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource


def generate_launch_description():
    map_pkg = get_package_share_directory("amr_navigation_map")
    nav2_pkg = get_package_share_directory("nav2_bringup")

    sim_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                map_pkg,
                "launch",
                "sim.launch.py",
            )
        )
    )

    nav2_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                nav2_pkg,
                "launch",
                "navigation_launch.py",
            )
        ),
        launch_arguments={
            "use_sim_time": "false",
            "params_file": os.path.join(
                map_pkg,
                "config",
                "nav2_params.yaml",
            ),
        }.items(),
    )

    return LaunchDescription([
        sim_launch,
        nav2_launch,
    ])
