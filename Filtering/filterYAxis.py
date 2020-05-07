import pcl
import pcl.pcl_visualization

def main():
    cloud = pcl.load('/home/nouran/Desktop/nouran/GUC/bachelor/pointCloud/filterXAxis.pcd')
    passthrough = cloud.make_passthrough_filter()
    passthrough.set_filter_field_name("y")
    passthrough.set_filter_limits(-0.2, 0.1)
    cloud_filtered = passthrough.filter()

    pcl.save(cloud_filtered, '/home/nouran/Desktop/nouran/GUC/bachelor/pointCloud/shoulder.pcd')
    # visual = pcl.pcl_visualization.CloudViewing()
    #
    #
    # visual.ShowMonochromeCloud(cloud_filtered, b'cloud')
    # v = True
    # while v:
    #     v = not (visual.WasStopped())


if __name__ == "__main__":
    # import cProfile
    # cProfile.run('main()', sort='time')
    main()
