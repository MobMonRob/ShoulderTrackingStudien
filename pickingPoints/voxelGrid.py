import pcl
import pcl.pcl_visualization


def main():
    cloud = pcl.load('/home/nouran/Desktop/nouran/GUC/bachelor/pointCloud/shoulder.pcd')
    sor = cloud.make_voxel_grid_filter()
    sor.set_leaf_size(0.02, 0.02, 0.02)
    cloud_filtered = sor.filter()

    pcl.save(cloud_filtered, '/home/nouran/Desktop/nouran/GUC/bachelor/pointCloud/voxelGrid.pcd')

    visual = pcl.pcl_visualization.CloudViewing()
    visual.ShowMonochromeCloud(cloud_filtered, b'cloud')
    v = True
    while v:
        v = not (visual.WasStopped())
if __name__ == "__main__":
    main()
