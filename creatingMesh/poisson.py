import open3d as o3d
from open3d.open3d.geometry import KDTreeSearchParamHybrid


def main():
    pcd = o3d.io.read_point_cloud("https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/shoulder.pcd")
    pcd.estimate_normals(search_param=KDTreeSearchParamHybrid(radius=0.1, max_nn=30), fast_normal_computation=True)
    poisson_mesh = \
    o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8, width=0, scale=1.1, linear_fit=False)[0]

    # To filter all surfaces from the mesh outside the bounding-box
    bbox = pcd.get_axis_aligned_bounding_box()
    p_mesh_crop = poisson_mesh.crop(bbox)

    o3d.io.write_triangle_mesh("https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/poissonMesh.ply",
                               p_mesh_crop,
                               write_ascii=True)


if __name__ == "__main__":
    main()

# Source: https://towardsdatascience.com/5-step-guide-to-generate-3d-meshes-from-point-clouds-with-python-36bad397d8ba