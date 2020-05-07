import numpy as np
import scipy.optimize

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.gca(projection='3d')

def fitPlaneLTSQ(XYZ):
    (rows, cols) = XYZ.shape
    G = np.ones((rows, 3))
    G[:, 0] = XYZ[:, 0]  #X
    G[:, 1] = XYZ[:, 1]  #Y
    Z = XYZ[:, 2]
    (a, b, c),resid,rank,s = np.linalg.lstsq(G, Z)
    normal = (a, b, -1)
    nn = np.linalg.norm(normal)
    normal = normal / nn
    print(a," ",b," ",c)
    return (c, normal)

# data = np.random.randn(100, 3)/3
# data[:, 2] /=10
# print(data)
data=np.array([[0.21, -0.07, 0.01],[0.23, -0.071, 0.016],[0.25, -0.097, 0.017],[0.27, -0.11, 0.016],[0.26, -0.088, 0.041],[0.24, -0.11, -0.0028],[0.24, -0.12, 0.0029],[0.25, -0.11, 0.012],[0.25, -0.12, 0.0039],[0.21, -0.1, 0.002],[0.23, -0.092, 0.012],[0.21, -0.11, -0.01],[0.2, -0.1, -0.013],[0.23, -0.11, -0.0072],[0.21, -0.12, -0.017],[0.23, -0.11, 0.0085],[0.25, -0.1, 0.025],[0.27, -0.11, 0.029],[0.25, -0.09, 0.03],[0.21, -0.091, -0.0077],[0.21, -0.089, 0.0077],[0.23, -0.087, 0.023],[0.2, -0.083, 0.0017],[0.19, -0.089, -0.012],[0.27, -0.092, 0.037],[0.26, -0.088, 0.041],[0.25, -0.13, -0.011],[0.23, -0.13, -0.013],[0.25, -0.071, 0.035],[0.23, -0.07, 0.028]])
c, normal = fitPlaneLTSQ(data)

# plot fitted plane
maxx = np.max(data[:,0])
maxy = np.max(data[:,1])
minx = np.min(data[:,0])
miny = np.min(data[:,1])

point = np.array([0.0, 0.0, c])
d = -point.dot(normal)

# plot original points
ax.scatter(data[:, 0], data[:, 1], data[:, 2])

# compute needed points for plane plotting
xx, yy = np.meshgrid([minx, maxx], [miny, maxy])
z = (-normal[0]*xx - normal[1]*yy - d)*1. / normal[2]

# plot plane
ax.plot_surface(xx, yy, z, alpha=0.2)

ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()