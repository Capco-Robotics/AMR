import os

from ament_index_python.packages import get_package_prefix
from launch import LaunchDescription
from launch_ros.actions import Node


def rosidl_env():
    """See the fuller explanation in amr_navigation_map/launch/sim.launch.py.

    Short version: macOS drops DYLD_* across the way launch_ros spawns a Node,
    so amr_msgs' Python typesupport cannot find its sibling dylib through
    @rpath, and every node importing amr_msgs dies on startup. Both nodes here
    use LiftCommand/LiftState. Duplicated rather than shared, because amr_lift
    should not have to depend on amr_navigation_map for a three-line helper.
    """

    lib = os.path.join(get_package_prefix('amr_msgs'), 'lib')

    return {
        'DYLD_LIBRARY_PATH': os.pathsep.join(
            [lib, os.environ.get('DYLD_LIBRARY_PATH', '')]
        )
    }


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='amr_lift',
            executable='lift_control_node',
            name='amr_lift',
            output='screen',
            additional_env=rosidl_env(),
        ),
        Node(
            package='amr_lift',
            executable='fake_lift_pico_node',
            name='fake_lift_pico',
            output='screen',
            additional_env=rosidl_env(),
        ),
    ])
