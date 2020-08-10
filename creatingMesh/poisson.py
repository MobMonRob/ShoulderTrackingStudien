import numpy as np
import open3d as o3d
from open3d.open3d.geometry import KDTreeSearchParamHybrid


def main():
    pcd = o3d.io.read_point_cloud("/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/shoulder.pcd")
    pcd.estimate_normals(search_param=KDTreeSearchParamHybrid(radius=0.1, max_nn=30), fast_normal_computation=True)
    poisson_mesh =o3d.geometry.TriangleMesh.create_from_point_cloud_poisson(pcd, depth=8, width=0, scale=1.1, linear_fit=False)[0]
    bbox = pcd.get_axis_aligned_bounding_box()
    p_mesh_crop = poisson_mesh.crop(bbox)
    o3d.io.write_triangle_mesh("/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/poissonMesh.ply", p_mesh_crop,
                               write_ascii=True)


def lod_mesh_export(mesh, lods, extension, path):
    mesh_lods = {}
    for i in lods:
        mesh_lod = mesh.simplify_quadric_decimation(i)
        o3d.io.write_triangle_mesh(path + "lod_" + str(i) + extension, mesh_lod)
        mesh_lods[i] = mesh_lod
    print("generation of " + str(i) + " LoD successful")
    return mesh_lods


if __name__ == "__main__":
    main()
