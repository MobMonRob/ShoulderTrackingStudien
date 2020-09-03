import pcl
import pcl.pcl_visualization


def main():
    cloud = pcl.load('https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/shoulder.pcd')

    # Create the filtering object
    sor = cloud.make_voxel_grid_filter()
    sor.set_leaf_size(0.02, 0.02, 0.02)
    cloud_filtered = sor.filter()

    pcl.save(cloud_filtered, 'https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/voxelGrid.pcd')


if __name__ == "__main__":
    main()
