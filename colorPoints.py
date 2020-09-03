import pcl
import open3d as o3d


def main():
    cloud = o3d.io.read_point_cloud(
        '/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/shoulder.pcd')
    front = o3d.io.read_point_cloud(
        "/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/front.pcd")
    back = o3d.io.read_point_cloud(
        "/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/back.pcd")

    # Paint the original point cloud green
    cloud.paint_uniform_color([0, 1.0, 0])

    # The six points that will be painted
    listBack = [100, 200, 150]
    listFront = [100, 200, 300]

    # Create 2 point clouds from the points that will be painted
    selectedFront = front.select_down_sample(listFront, invert=False)
    selectedBack = back.select_down_sample(listBack, invert=False)

    # Paint the 2 point clouds red
    selectedFront.paint_uniform_color([1.0, 0, 0])
    selectedBack.paint_uniform_color([1.0, 0, 0])

    # Combine the 2 point clouds after being colored with the original point cloud
    combined = o3d.geometry.PointCloud()
    combined += cloud
    combined += selectedFront
    combined += selectedBack
    o3d.io.write_point_cloud("/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/colored.pcd", combined)


if __name__ == "__main__":
    main()
