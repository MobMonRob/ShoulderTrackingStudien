import numpy as np
import open3d as o3d
from open3d.open3d.geometry import KDTreeSearchParamHybrid


def main():
    pcd = o3d.io.read_point_cloud("https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/shoulder.pcd")
    pcd.estimate_normals(search_param=KDTreeSearchParamHybrid(radius=0.1, max_nn=30), fast_normal_computation=True)

    # Compute the necessary radius parameter based on the average distances computed from all the distances between points
    distances = pcd.compute_nearest_neighbor_distance()
    avg_dist = np.mean(distances)
    radius = 1.5 * avg_dist

    # Create a mesh and store it in bpa_mesh variable
    bpa_mesh = o3d.geometry.TriangleMesh.create_from_point_cloud_ball_pivoting(pcd, o3d.utility.DoubleVector(
        [radius, radius * 2]))

    # Downsample the result to an acceptable number of triangles
    dec_mesh = bpa_mesh.simplify_quadric_decimation(100000)

    # To insure the consistency of the mesh
    dec_mesh.remove_degenerate_triangles()
    dec_mesh.remove_duplicated_triangles()
    dec_mesh.remove_duplicated_vertices()
    dec_mesh.remove_non_manifold_edges()

    # Export the BPA reconstruction as .ply file
    o3d.io.write_triangle_mesh("https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/ballPivotingMesh.ply", dec_mesh,
                               write_ascii=True)


if __name__ == "__main__":
    main()


# Source: https://towardsdatascience.com/5-step-guide-to-generate-3d-meshes-from-point-clouds-with-python-36bad397d8ba