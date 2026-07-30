"""Everything needed to drive the AMR from the operator console, in one file.

    ros2 launch amr_navigation_map demo.launch.py

Brings up the simulated robot, SLAM, Nav2, RViz and amr_command's websocket
gateway. The only other thing you need is a static file server for the
console itself:

    cd AMR_Operator_Console/frontend && python3 -m http.server 8080

This is sim.launch.py with the arguments a console demo always wants, kept
separate so sim.launch.py's defaults stay what everyone else's branches
expect. Every argument is still forwarded, so `rviz:=false` and friends work
here too.
"""

import os

from ament_index_python.packages import get_package_share_directory

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration


def generate_launch_description():

    package_dir = get_package_share_directory("amr_navigation_map")

    forwarded = ["rviz", "noise", "scan_topic", "lift", "nav", "gateway"]

    return LaunchDescription([

        DeclareLaunchArgument("rviz", default_value="true"),
        DeclareLaunchArgument("noise", default_value="false"),
        DeclareLaunchArgument("scan_topic", default_value="/scan"),
        DeclareLaunchArgument("lift", default_value="false"),

        # The two that make this a demo rather than a bare sim.
        DeclareLaunchArgument("nav", default_value="true"),
        DeclareLaunchArgument("gateway", default_value="true"),

        IncludeLaunchDescription(
            PythonLaunchDescriptionSource(
                os.path.join(package_dir, "launch", "sim.launch.py")
            ),
            launch_arguments={
                name: LaunchConfiguration(name) for name in forwarded
            }.items(),
        ),

    ])
