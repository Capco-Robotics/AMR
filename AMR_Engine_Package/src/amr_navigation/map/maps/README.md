# AMR Maps

This directory stores generated map artifacts.

Maps are not source files and should normally not be committed.
Only approved demo maps should be checked in.

## SLAM Toolbox serialized map

SLAM Toolbox stores maps as:

<name>.posegraph
<name>.data

Example:

box_demo.posegraph
box_demo.data


Generate using:

ros2 service call /slam_toolbox/serialize_map \
slam_toolbox/srv/SerializePoseGraph \
"{filename: /absolute/path/to/maps/box_demo}"


## Portable occupancy map

Nav2 compatible maps are stored as:

<name>.pgm
<name>.yaml


Generate using:

ros2 run nav2_map_server map_saver_cli \
-f /absolute/path/to/maps/box_demo


The yaml file is used by Nav2 map_server.
The posegraph files are used by slam_toolbox localization.
