import pcl
import numpy as np


def main():
    cloud = pcl.load("/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/shoulder.pcd")
    print('PointCloud has: ' + str(cloud.size) + ' data points.')

    # Build a passthrough filter to remove spurious NaNs
    passthrough = cloud.make_passthrough_filter()
    passthrough.set_filter_field_name('z')
    passthrough.set_filter_limits(0, 1.5)
    cloud_filtered = passthrough.filter()
    print('PointCloud has: ' + str(cloud_filtered.size) + ' data points.')

    #  Estimate point normals
    ne = cloud_filtered.make_NormalEstimation()
    tree = cloud_filtered.make_kdtree()
    ne.set_SearchMethod(tree)
    ne.set_KSearch(50)

    # Create the segmentation object for the planar model and set all the parameters
    seg = cloud_filtered.make_segmenter_normals(ksearch=50)
    seg.set_optimize_coefficients(True)
    seg.set_model_type(pcl.SACMODEL_NORMAL_PLANE)
    seg.set_normal_distance_weight(0.1)
    seg.set_method_type(pcl.SAC_RANSAC)
    seg.set_max_iterations(100)
    seg.set_distance_threshold(0.03)
    [indices, coefficients_plane] = seg.segment()
    cloud_plane = cloud_filtered.extract(indices, False)
    print('PointCloud representing the planar component: ' +
          str(cloud_plane.size) + ' data points.\n')

    cloud_filtered2 = cloud_filtered.extract(indices, True)

    # Create the segmentation object for cylinder segmentation and set all the parameters
    seg = cloud_filtered2.make_segmenter_normals(ksearch=50)
    seg.set_optimize_coefficients(True)
    seg.set_model_type(pcl.SACMODEL_CYLINDER)
    seg.set_normal_distance_weight(0.001)
    seg.set_method_type(pcl.SAC_RANSAC)
    seg.set_max_iterations(10000)
    seg.set_distance_threshold(0.05)
    seg.set_radius_limits(0, 0.1)
    [indices2, coefficients_cylinder] = seg.segment()
    cloud_cylinder = cloud_filtered2.extract(indices2, False)
    if cloud_cylinder.size == 0:
        print("Can't find the cylindrical component.")
    else:
        print("PointCloud representing the cylindrical component: " +
              str(cloud_cylinder.size) + " data points.")
        pcl.save(cloud_cylinder,
                 'https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/cylinder.pcd')


if __name__ == "__main__":
    main()
