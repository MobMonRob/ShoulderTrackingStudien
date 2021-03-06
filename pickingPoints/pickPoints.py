import open3d as o3d


def demo_crop_geometry():
    print("Demo for manual geometry cropping")
    print("1) Press 'Y' twice to align geometry with negative direction of y-axis")
    print("2) Press 'K' to lock screen and to switch to selection mode")
    print("3) Drag for rectangle selection,")
    print("   or use ctrl + left click for polygon selection")
    print("4) Press 'C' to get a selected geometry and to save it")
    print("5) Press 'F' to switch to freeview mode")
    pcd = o3d.io.read_point_cloud("https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/back.pcd")
    o3d.visualization.draw_geometries_with_editing([pcd])


if __name__ == "__main__":
    demo_crop_geometry()

