# Dimitri packages

Install:

`sudo apt-get install ros-melodic-ros-control ros-melodic-ros-controllers ros-melodic-joint-state-controller ros-melodic-effort-controllers ros-melodic-position-controllers ros-melodic-gazebo-ros-pkgs ros-melodic-gazebo-ros-control ` Change the melodic to your ROS version.

Do:

` catkin_make `

To see and move the robot on Rviz:

` roslaunch dimitri_description display.launch `

To use the Gazebo simulation: 

`roslaunch dimitri_description dimitri_sim.launch`

`roslaunch dimitri_control dimitri_control.launch` 

To move publish on the topic:

`/dimitri/joint*_position_controller/command` th * is a number from 1 to 18.

The camera images are on the topic:

`/dimitri/camera1/image_raw`, Type: `sensor_msgs/Image`

To see the joints go to:

`dimitri_control/config/dimitri_control.yaml`
