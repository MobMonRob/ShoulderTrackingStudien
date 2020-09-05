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
### To open realsense camera viewer:
```
realsense-viewer
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
### To view a PCD file:
```
pcl_viewer file.pcd
```
