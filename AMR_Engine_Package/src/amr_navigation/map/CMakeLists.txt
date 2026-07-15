cmake_minimum_required(VERSION 3.8)
project(amr_navigation_map)

find_package(ament_cmake REQUIRED)

install(DIRECTORY config launch urdf
  DESTINATION share/${PROJECT_NAME}
)
install(PROGRAMS
  test_scripts/fake_scan_publisher.py
  DESTINATION lib/${PROJECT_NAME}
)
ament_package()
