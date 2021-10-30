import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def plot3d(verts, facecolor):
  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111, projection = "3d")
  poly = Poly3DCollection(verts, alpha = 0.5, linewidths = 2, edgecolors = "green", facecolor = facecolor)
  ax.add_collection3d(poly)

  ax.set_xlim(-2,6)
  ax.set_ylim(-2,6)
  ax.set_zlim(0,8)
  ax.set_xlabel("X")
  ax.set_ylabel("Y")
  ax.set_zlabel("Z")
  ax.grid(True)

  plt.show()

def vertsPyramid(points):
  P = points
  verts = [ [P[0], P[1], P[2], P[3]],
            [P[0], P[1], P[4]],
            [P[0], P[3], P[4]],
            [P[2], P[1], P[4]],
            [P[2], P[3], P[4]], ]
  return verts

def vertsQuadrilateral(points):
  P = points
  verts = [ [P[0], P[1], P[2], P[3]],
            [P[5], P[4], P[7], P[6]],
            [P[0], P[1], P[5], P[4]],
            [P[2], P[6], P[7], P[3]],
            [P[1], P[2], P[6], P[5]],
            [P[0], P[3], P[7], P[4]], ]
  return verts

pyramid = np.array([ [-1.0, -1.0, 0.0],
                     [1.0, -1.0, 0.0],
                     [1.0, 1.0, 0.0],
                     [-1.0, 1.0, 0.0],
                     [0.0, 0.0, 3.0], ])

cube = np.array([ [-0.75, -0.75, 0.0],
                  [0.75, -0.75, 0.0],
                  [0.75, 0.75, 0.0],
                  [-0.75, 0.75, 0.0],
                  [-0.75, -0.75, 1.5],
                  [0.75, -0.75, 1.5],
                  [0.75, 0.75, 1.5],
                  [-0.75, 0.75, 1.5], ])

parallelepiped = np.array([ [0.0, 0.0, 0.0],
                            [1.5, 0.0, 0.0],
                            [1.5, 5.0, 0.0],
                            [0.0, 5.0, 0.0],
                            [0.0, 0.0, 2.5],
                            [1.5, 0.0, 2.5],
                            [1.5, 5.0, 2.5],
                            [0.0, 5.0, 2.5], ])

pyramidTrunk = np.array([ [0.0, 0.0, 0.0],
                          [3.0, 0.0, 0.0],
                          [3.0, 3.0, 0.0],
                          [0.0, 3.0, 0.0],
                          [0.85, 0.85, 2.5],
                          [1.95, 0.85, 2.5],
                          [1.95, 1.95, 2.5],
                          [0.85, 1.95, 2.5], ])


plot3d(vertsPyramid(pyramid), 'blue')
plot3d(vertsQuadrilateral(cube), 'orange')
plot3d(vertsQuadrilateral(parallelepiped), 'yellow' )
plot3d(vertsQuadrilateral(pyramidTrunk), 'red')
