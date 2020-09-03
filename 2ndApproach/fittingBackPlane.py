import numpy as np
import matplotlib.pyplot as plt
import open3d as o3d

fig = plt.figure()
ax = fig.gca(projection='3d')


# The function that gets the best fitting plane
def fitPlaneLTSQ(XYZ):
    (rows, cols) = XYZ.shape
    G = np.ones((rows, 3))
    G[:, 0] = XYZ[:, 0]  # X
    G[:, 1] = XYZ[:, 1]  # Y
    Z = XYZ[:, 2]
    (a, b, c), resid, rank, s = np.linalg.lstsq(G, Z)
    normal = (a, b, -1)
    nn = np.linalg.norm(normal)
    normal = normal / nn
    print(a, " ", b, " ", c)
    return (c, normal)


pcd_load = o3d.io.read_point_cloud('https://github.com/MobMonRob/ShoulderTrackingStudien/blob/dev/data/back.pcd')

data = np.array(pcd_load.points)

c, normal = fitPlaneLTSQ(data)

# plot fitted plane
maxx = np.max(data[:, 0])
maxy = np.max(data[:, 1])
minx = np.min(data[:, 0])
miny = np.min(data[:, 1])

point = np.array([0.0, 0.0, c])
d = -point.dot(normal)

# plot original points
ax.scatter(data[:, 0], data[:, 1], data[:, 2])

# compute needed points for plane plotting
xx, yy = np.meshgrid([minx, maxx], [miny, maxy])
z = (-normal[0] * xx - normal[1] * yy - d) * 1. / normal[2]

# plot plane
ax.plot_surface(xx, yy, z, alpha=0.2)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()

# Source: https://gist.github.com/RustingSword/e22a11e1d391f2ab1f2c#file-fitplane-py-L16
