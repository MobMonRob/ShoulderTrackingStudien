import pcl
import numpy as np
import random


def main():
    cloud = pcl.load('https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/shoulder.pcd')

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
    front = pcl.PointCloud()

    # For the points segmented from the front plane
    points = np.zeros((len(indices), 3), dtype=np.float32)

    # For the all the points of the point cloud without the front plane
    points2 = np.zeros((cloud.size - len(indices), 3), dtype=np.float32)
    ind = 0

    # Loops that fill both arrays
    for j in range(0, cloud.size):
        flag = True
        for i in range(0, len(indices)):
            if j == 0:
                points[i][0] = cloud[indices[i]][0]
                points[i][1] = cloud[indices[i]][1]
                points[i][2] = cloud[indices[i]][2]
            if j == indices[i]:
                flag = False
                break
        if flag:
            points2[ind][0] = cloud[j][0]
            points2[ind][1] = cloud[j][1]
            points2[ind][2] = cloud[j][2]
            ind = ind + 1
    front.from_array(points)
    cropped = pcl.PointCloud()
    cropped.from_array(points2)
    pcl.save(front, 'https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/front.pcd')
    pcl.save(cropped, 'https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/cropped.pcd')


if __name__ == "__main__":
    main()
