import pcl
import numpy as np


def main():
    cloud = pcl.load('https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/cropped.pcd')

    # Create the segmentation object
    seg = cloud.make_segmenter_normals(ksearch=50)

    # Setting the parameters of the segmenter
    seg.set_optimize_coefficients(True)
    seg.set_model_type(pcl.SACMODEL_NORMAL_PLANE)
    seg.set_method_type(pcl.SAC_RANSAC)
    seg.set_distance_threshold(0.01)
    seg.set_normal_distance_weight(0.01)
    seg.set_max_iterations(100)
    indices, coefficients = seg.segment()

    if len(indices) == 0:
        print('Could not estimate a planar model for the given dataset.')
        exit(0)

    print('Model coefficients: ' + str(coefficients[0]) + ' ' + str(
        coefficients[1]) + ' ' + str(coefficients[2]) + ' ' + str(coefficients[3]))

    print('Model inliers: ' + str(len(indices)))

    points = np.zeros((len(indices), 3), dtype=np.float32)
    back = pcl.PointCloud()

    # Loop to fill points array
    for i in range(0, len(indices)):
        points[i][0] = cloud[indices[i]][0]
        points[i][1] = cloud[indices[i]][1]
        points[i][2] = cloud[indices[i]][2]
    back.from_array(points)

    pcl.save(back, 'https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/back.pcd')


if __name__ == "__main__":
    main()
