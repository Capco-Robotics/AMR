"""Launch Nav2 with rewritten parameters for the AMR simulation."""

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration

from nav2_common.launch import RewrittenYaml


def generate_launch_description():
    package_dir = get_package_share_directory("amr_navigation_map")
    nav2_launch_dir = os.path.join(
        get_package_share_directory("nav2_bringup"),
        "launch",
    )

    namespace = LaunchConfiguration("namespace")
    use_sim_time = LaunchConfiguration("use_sim_time")
    autostart = LaunchConfiguration("autostart")
    scan_topic = LaunchConfiguration("scan_topic")

    params_file = os.path.join(
        package_dir,
        "config",
        "nav2_params.yaml",
    )

    configured_params = RewrittenYaml(
        source_file=params_file,
        root_key=namespace,
        param_rewrites={
            "use_sim_time": use_sim_time,
            "scan_topic": scan_topic,
            "autostart": autostart,
        },
        convert_types=True,
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            "namespace",
            default_value="",
        ),
        DeclareLaunchArgument(
            "use_sim_time",
            default_value="false",
        ),
        DeclareLaunchArgument(
            "autostart",
            default_value="true",
        ),
        DeclareLaunchArgument(
            "scan_topic",
            default_value="/scan",
        ),
        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(nav2_launch_dir, "navigation_launch.py")
            ),
            launch_arguments={
                "namespace": namespace,
                "use_sim_time": use_sim_time,
                "autostart": autostart,
                "params_file": configured_params,
            }.items(),
        ),
    ])
