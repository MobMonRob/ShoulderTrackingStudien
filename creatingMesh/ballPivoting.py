import numpy as np
import open3d as o3d
from open3d.open3d.geometry import KDTreeSearchParamHybrid


def main():
    output_path = "/home/nouran/Desktop/nouran/GUC/bachelor/pointCloud/"
    pcd = o3d.io.read_point_cloud("/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/shoulder.pcd")
    pcd.estimate_normals(search_param=KDTreeSearchParamHybrid(radius=0.1, max_nn=30), fast_normal_computation=True)

    distances = pcd.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 1.5 * avg_dist
    bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, o3d.utility.DoubleVector(
        [radius, radius * 2]))
    dec_mesh = bpa_mesh.simplify_quadric_decimation(100000)
    dec_mesh.remove_degenerate_triangles()
    dec_mesh.remove_duplicated_triangles()
    dec_mesh.remove_duplicated_vertices()
    dec_mesh.remove_non_manifold_edges()
    o3d.io.write_triangle_mesh("/home/nouran/Desktop/nouran/GUC/bachelor/repo/ShoulderTrackingStudien/data/ballPivotingMesh.ply", dec_mesh,
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
