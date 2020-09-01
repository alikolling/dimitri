# Dimitri packages

First:

` catkin_make `

To see and move the robot on Rviz:

` roslaunch dimitri_description display.launch `

To use the Gazebo simulation: 

`roslaunch dimitri_description dimitri_sim.launch`

`roslaunch dimitri_control dimitri_control.launch` 

To move publish on the topic:

`joint*_position_controller/command`

The camera images are on the topic:

`/dimitri/camera1/image_raw`, Type: `sensor_msgs/Image`

To see the joints go to:

`dimitri_control/config/dimitri_control.yaml`

