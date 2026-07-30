from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import (
    get_package_prefix,
    get_package_share_directory,
)
from launch_ros.actions import Node

import os


def rosidl_env():
    """Loader path every node that imports amr_msgs needs, on macOS.

    amr_msgs' Python typesupport extension finds its sibling
    libamr_msgs__rosidl_generator_py.dylib through @rpath, which resolves
    against DYLD_LIBRARY_PATH. macOS drops DYLD_* variables across the way
    launch_ros spawns a Node -- ExecuteProcess and `ros2 run` keep them, which
    is why the same node runs by hand and dies under `ros2 launch` -- and the
    loader then searches only the conda prefix, where that dylib does not
    exist. Every amr_msgs-using node died on import with

        UnsupportedTypeSupport: Could not import 'rosidl_typesupport_c'

    Re-asserting the variable for the child restores it. Harmless on Linux,
    where DYLD_LIBRARY_PATH is simply ignored.
    """

    lib = os.path.join(get_package_prefix("amr_msgs"), "lib")

    return {
        "DYLD_LIBRARY_PATH": os.pathsep.join(
            [lib, os.environ.get("DYLD_LIBRARY_PATH", "")]
        )
    }


def generate_launch_description():

    noise = LaunchConfiguration("noise")
    rviz = LaunchConfiguration("rviz")
    nav = LaunchConfiguration("nav")
    scan_topic = LaunchConfiguration("scan_topic")
    lift = LaunchConfiguration("lift")

    map_pkg = get_package_share_directory("amr_navigation_map")
    lidar_pkg = get_package_share_directory("amr_navigation_lidar")
    description_pkg = get_package_share_directory("amr_description")
    lift_pkg = get_package_share_directory("amr_lift")

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

    lift_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                lift_pkg,
                "launch",
                "lift_sim.launch.py",
            )
        ),
        condition=IfCondition(lift),
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

        DeclareLaunchArgument(
            "lift",
            default_value="false",
        ),

        DeclareLaunchArgument(
            "gateway",
            default_value="false",
            description="Also start amr_command's operator-console gateway.",
        ),

        description_launch,

        # Off by default so this file keeps behaving as it did for anyone
        # already using it; demo.launch.py turns it on.
        Node(
            package="amr_command",
            executable="command_gateway_node",
            name="amr_command",
            output="screen",
            condition=IfCondition(LaunchConfiguration("gateway")),
        ),

        Node(
            package="amr_navigation_move",
            executable="fake_pico_node",
            name="fake_pico_node",
            output="screen",
            additional_env=rosidl_env(),
            parameters=[
                {"use_sim_time": False}
            ],
        ),

        Node(
            package="amr_navigation_move",
            executable="drive_controller_node",
            name="drive_controller_node",
            output="screen",
            additional_env=rosidl_env(),
            parameters=[
                {"use_sim_time": False}
            ],
        ),

        Node(
            package="amr_navigation_move",
            executable="odometry_node",
            name="odometry_node",
            output="screen",
            additional_env=rosidl_env(),
            parameters=[
                {"use_sim_time": False}
            ],
        ),

        Node(
            package="amr_engine",
            executable="state_machine_node",
            name="state_machine_node",
            output="screen",
            additional_env=rosidl_env(),
        ),

        lidar_launch,
        slam_launch,
        nav_launch,
        lift_launch,

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