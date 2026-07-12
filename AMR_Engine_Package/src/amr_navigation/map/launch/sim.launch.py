from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument, IncludeLaunchDescription
from launch.conditions import IfCondition
from launch.launch_description_sources import PythonLaunchDescriptionSource
from launch.substitutions import LaunchConfiguration
from ament_index_python.packages import get_package_share_directory

from launch_ros.actions import Node


def generate_launch_description():

    use_console = LaunchConfiguration('use_console')
    noise = LaunchConfiguration('noise')
    rviz = LaunchConfiguration('rviz')

    map_pkg = get_package_share_directory('amr_navigation_map')

    slam_launch = IncludeLaunchDescription(
        PythonLaunchDescriptionSource(
            map_pkg + '/launch/slam.launch.py'
        )
    )

    return LaunchDescription([

        DeclareLaunchArgument(
            'use_console',
            default_value='false'
        ),

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

        Node(
            package='amr_navigation_map',
            executable='fake_scan_publisher.py',
            name='fake_scan_publisher',
            output='screen',
            parameters=[
                {
                    'use_sim_time': False,
                    'noise': noise
                }
            ],
        ),

        Node(
            package='tf2_ros',
            executable='static_transform_publisher',
            name='base_link_to_laser',
            arguments=[
                '0',
                '0',
                '0.1',
                '0',
                '0',
                '0',
                'base_link',
                'laser'
            ],
        ),

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
