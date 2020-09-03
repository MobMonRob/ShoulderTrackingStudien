import pcl


def main():
    cloud = pcl.load('https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/filterXAxis.pcd')
    passthrough = cloud.make_passthrough_filter()

    # choose the axis you want to filter on
    passthrough.set_filter_field_name("y")

    # choose the lower and upper boundaries of the filter (these are the values to be included in the point cloud)
    passthrough.set_filter_limits(-0.2, 0.1)

    cloud_filtered = passthrough.filter()
    pcl.save(cloud_filtered, 'https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/shoulder.pcd')


if __name__ == "__main__":
    main()
