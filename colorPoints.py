import pcl
import open3d as o3d


def main():
    cloud = o3d.io.read_point_cloud(
        '/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/shoulder.pcd')
    front = o3d.io.read_point_cloud(
        "/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/front.pcd")
    back = o3d.io.read_point_cloud(
        "/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/back.pcd")
    cloud.paint_uniform_color([0, 1.0, 0])
    listBack = [100, 200, 150]
    listFront = [100, 200, 300]
    selectedFront = front.select_down_sample(listFront, invert=False)
    selectedBack = back.select_down_sample(listBack, invert=False)
    selectedFront.paint_uniform_color([1.0, 0, 0])
    selectedBack.paint_uniform_color([1.0, 0, 0])
    combined = o3d.geometry.PointCloud()
    combined += cloud
    combined += selectedFront
    combined += selectedBack
    o3d.io.write_point_cloud("/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/colored.pcd", combined)


if __name__ == "__main__":
    main()
