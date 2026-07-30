"""Start the frontier explorer on its own.

    ros2 launch amr_navigation_explore explore.launch.py

The node only *decides where to go* -- it needs SLAM Toolbox publishing /map
and Nav2 offering navigate_to_pose to do anything, so in practice this is
included from sim.launch.py rather than run alone. Starting it early is
harmless: it sits idle until something sends an explore_area goal.
"""

import os

from ament_index_python.packages import get_package_prefix

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration
from launch_ros.actions import Node


def rosidl_env():
    """Loader path amr_msgs' Python typesupport needs on macOS.

    Same fix, and the same reason, as sim.launch.py: launch_ros drops DYLD_*
    when it spawns a node, so anything importing amr_msgs dies on import with
    "Could not import 'rosidl_typesupport_c'". Ignored on Linux.
    """

    lib = os.path.join(get_package_prefix("amr_msgs"), "lib")

    return {
        "DYLD_LIBRARY_PATH": os.pathsep.join(
            [lib, os.environ.get("DYLD_LIBRARY_PATH", "")]
        )
    }


def generate_launch_description():

    return LaunchDescription([

        DeclareLaunchArgument(
            "min_frontier_size",
            default_value="0.35",
            description="Ignore unexplored gaps narrower than this, in metres.",
        ),

        DeclareLaunchArgument(
            "robot_radius",
            default_value="0.30",
            description="Clearance a frontier goal needs, in metres.",
        ),

        Node(
            package="amr_navigation_explore",
            executable="explorer_node",
            name="amr_explorer",
            output="screen",
            additional_env=rosidl_env(),
            parameters=[{
                "min_frontier_size": LaunchConfiguration("min_frontier_size"),
                "robot_radius": LaunchConfiguration("robot_radius"),
            }],
        ),

    ])
