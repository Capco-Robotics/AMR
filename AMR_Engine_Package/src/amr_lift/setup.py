from setuptools import find_packages, setup

package_name = 'amr_lift'

setup(
    name=package_name,
    version='0.0.1',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        ('share/' + package_name + '/launch', ['launch/lift_sim.launch.py'],),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Rushil Juneja',
    maintainer_email='rushiljuneja@gmail.com',
    description='Lift (linear actuator) target/state coordination.',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'lift_control_node = amr_lift.lift_control_node:main',
            'fake_lift_pico_node = amr_lift.fake_lift_pico_node:main',
        ],
    },
)
