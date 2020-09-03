import pcl


def main():
    cloud = pcl.load('https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/firstPointCloud.pcd')
    passthrough = cloud.make_passthrough_filter()

    # choose the axis you want to filter on
    passthrough.set_filter_field_name("x")

    # choose the lower and upper boundaries of the filter (these are the values to be included in the point cloud)
    passthrough.set_filter_limits(0.1, 0.3)

    cloud_filtered = passthrough.filter()
    pcl.save(cloud_filtered, 'https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/filterXAxis.pcd')


if __name__ == "__main__":
    main()
