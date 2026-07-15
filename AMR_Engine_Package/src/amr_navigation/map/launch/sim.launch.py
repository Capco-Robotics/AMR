from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory
import os
from launch_ros.actions import Node


def generate_launch_description():

    noise = LaunchConfiguration('noise')
    rviz = LaunchConfiguration('rviz')

    map_pkg = get_package_share_directory('amr_navigation_map')
    lidar_pkg = get_package_share_directory('amr_navigation_lidar')

    lidar_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            os.path.join(
                lidar_pkg,
                'launch',
                'fake_scan.launch.py'
            )
        )
    )
    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            map_pkg + '/launch/slam.launch.py'
        )
    )

    return LaunchDescription([
        DeclareLaunchArgument(
            'noise',
            default_value='false'
        ),

        DeclareLaunchArgument(
            'rviz',
            default_value='true'
        ),

        Node(
            package='amr_navigation_move',
            executable='fake_pico_node',
            name='fake_pico_node',
            output='screen',
            parameters=[
                {'use_sim_time': False}
            ],
        ),

        Node(
            package='amr_navigation_move',
            executable='drive_controller_node',
            name='drive_controller_node',
            output='screen',
            parameters=[
                {'use_sim_time': False}
            ],
        ),

        Node(
            package='amr_navigation_move',
            executable='odometry_node',
            name='odometry_node',
            output='screen',
            parameters=[
                {'use_sim_time': False}
            ],
        ),

        lidar_launch,
        slam_launch,

        Node(
            package='rviz2',
            executable='rviz2',
            name='rviz2',
            output='screen',
            condition=IfCondition(rviz),
            arguments=[
                '-d',
                map_pkg + '/config/slam_sim.rviz'
            ],
        ),
    ])
