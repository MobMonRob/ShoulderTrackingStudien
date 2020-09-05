# ShoulderTrackingStudien
Code to determine the shoulder joint center based on 3dcam data. The aim of this project is to implement a low-cost shoulder motion analysis method based on
point cloud data from 3D cameras to determine the center of the shoulder.The camera used in this project is the Intel Realsense Depth Camera D435. I used the
RTABMap tool which is a ROS tool to extract the point clouds.
## Usage (Ubuntu)
### Clone repository
```
git clone https://github.com/MobMonRob/ShoulderTrackingStudien.git
cd ShoulderTrackingStudien
```
### Install ROS:
```
sudo sh -c 'echo "deb http://packages.ros.org/ros/ubuntu $(lsb_release -sc) main" > /etc/apt/sources.list.d/ros-latest.list'
sudo apt-key adv --keyserver 'hkp://keyserver.ubuntu.com:80' --recv-key C1CF6E31E6BADE8868B172B4F42ED6FBAB17C654
sudo apt update
sudo apt install ros-kinetic-desktop-full
sudo apt install ros-kinetic-desktop
sudo apt install ros-kinetic-ros-base
source /opt/ros/kinetic/setup.bash
sudo apt install python-rosdep python-rosinstall python-rosinstall-generator python-wstool build-essential
sudo apt install python-rosdep
sudo rosdep init
rosdep update
```
### Create a ROS Workspace:
```
mkdir -p ~/catkin_ws/src
cd ~/catkin_ws/
catkin_make
```
### To start a realsense node on Ros:
```
source devel/setup.bash
roslaunch realsense2_camera rs_camera.launch
```
### To open rtabmap with realsense camera: (You first have to start a realsense node on ROS)
```
roslaunch realsense2_camera rs_camera.launch align_depth:=true

roslaunch rtabmap_ros rtabmap.launch rtabmap_args:="--delete_db_on_start" depth_topic:=/camera/aligned_depth_to_color/image_raw rgb_topic:=/camera/color/image_raw camera_info_topic:=/camera/color/camera_info approx_sync:=false
```
### To open realsense camera viewer:
```
realsense-viewer
```
### To view a PCD file:
```
pcl_viewer file.pcd
```
