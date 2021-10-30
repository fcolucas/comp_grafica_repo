import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def translationTransformation(solid, x, y, z, n=8):
  ones = np.ones((n, 4))
  for i in range(n):
    for j in range(3):
      ones[i][j] = solid[i][j]
  translar = np.array([ [1, 0, 0, x],
                        [0, 1, 0, y],
                        [0, 0, 1, z],
                        [0, 0, 0, 1], ])
  aux = np.dot(translar, ones.T)
  aux = aux.T

  result = np.ndarray((n, 3))
  for i in range(n):
    for j in range(3):
      result[i][j] = aux[i][j]
  return result

def plot3d(vertsList, facecolorList):
  x = np.array([-6, 6, 0, 0, 0, 0, 0, 0])
  y = np.array([0, 0, 0, -6, 6, 0, 0, 0])
  z = np.array([0, 0, 0, 0, 0, 0, -6, 6])

  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111, projection = "3d")
  ax.plot(x,y,z, color='black')

  for i in range(len(vertsList)):
    poly = Poly3DCollection(vertsList[i], alpha = 0.5, linewidths = 2, edgecolors = "green", facecolor = facecolorList[i])
    ax.add_collection3d(poly)

  ax.set_xlim(-6,6)
  ax.set_ylim(-6,6)
  ax.set_zlim(-6,6)
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
            [P[0], P[1], P[5],P[4]],
            [P[2], P[6], P[7],P[3]],
            [P[1], P[2], P[6],P[5]],
            [P[0], P[3], P[7],P[4]], ]
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


parallelepiped = translationTransformation(parallelepiped, x=-5.25, y=-5.5, z=0)
pyramidTrunk = translationTransformation(pyramidTrunk, x=-3.25, y=-4, z=0)
pyramid = translationTransformation(pyramid, x=1.5, y=1.5, z=0, n=len(pyramid))
cube = translationTransformation(cube, x=4, y=1.5, z=0)

vertsList = [vertsPyramid(pyramid), vertsQuadrilateral(cube), vertsQuadrilateral(parallelepiped), vertsQuadrilateral(pyramidTrunk)]
facecolorList = ['blue', 'orange', 'yellow', 'red']
plot3d(vertsList, facecolorList)
