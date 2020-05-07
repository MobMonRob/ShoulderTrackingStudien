import pcl
import random


def main():
    cloud = pcl.load('/home/nouran/Desktop/nouran/GUC/bachelor/pointCloud/firstPointCloud.pcd')
    passthrough = cloud.make_passthrough_filter()
    passthrough.set_filter_field_name("x")
    passthrough.set_filter_limits(0.1, 0.3)
    cloud_filtered = passthrough.filter()

    pcl.save(cloud_filtered, '/home/nouran/Desktop/nouran/GUC/bachelor/pointCloud/filterXAxis.pcd')


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()', sort='time')
    main()
