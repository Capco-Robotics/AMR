from glob import glob
import os

from setuptools import find_packages, setup

package_name = 'amr_navigation_lidar'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
    (
        'share/ament_index/resource_index/packages',
        ['resource/' + package_name],
    ),
    (
        'share/' + package_name,
        ['package.xml'],
    ),
    (
        os.path.join('share', package_name, 'launch'),
        glob('launch/*.launch.py'),
    ),
   ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rushil Juneja',
    maintainer_email='rushiljuneja@gmail.com',
    description='LiDAR driver integration and simulation utilities.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fake_scan_publisher = amr_navigation_lidar.fake_scan_publisher:main',
        ],
    },
)