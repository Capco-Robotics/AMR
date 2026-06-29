from setuptools import find_packages, setup

package_name = 'amr_command'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rushil Juneja',
    maintainer_email='rushiljuneja@gmail.com',
    description='Remote/live-info command gateway between the operator console and amr_engine.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'command_gateway_node = amr_command.command_gateway_node:main',
        ],
    },
)
