import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

def baseChange(solid):
  eye = np.array([6,-6,6])

  homoSolid1 = np.ones((len(solid[1]), 4))
  for i in range(len(solid[1])):
    for j in range(3):
      homoSolid1[i,j] = solid[1][i,j] 
  homoSolid2 = np.ones((len(solid[0]), 4))
  for i in range(len(solid[0])):
    for j in range(3):
      homoSolid2[i,j] = solid[0][i,j]

  meanX = (solid[0][:,0].mean() + solid[1][:,0].mean())/2
  meanY = (solid[0][:,1].mean() + solid[1][:,1].mean())/2
  meanZ = (solid[0][:,2].mean() + solid[1][:,2].mean())/2
  at = [meanX, meanY, meanZ]
  
  N = (at - eye)
  N = N/np.linalg.norm(N)
  up = [0.7, 0.02, -1.7]
  V = np.cross(N, up)
  V= V/np.linalg.norm(V)
  U = np.cross(N, V)
  U = U/np.linalg.norm(U)
  
  R = np.array([ [V[0], V[1], V[2], 0],
                 [N[0], N[1], N[2], 0],
                 [U[0], U[1], U[2], 0],
                 [0, 0, 0, 1], ])
  iR = np.linalg.inv(R)
  T = np.array([ [1, 0, 0, -eye[0]],
                 [0, 1, 0, -eye[1]],
                 [0, 0, 1, -eye[2]],
                 [0, 0, 0, 1], ])
  RT = np.dot(R, T)

  p = np.ones(4)
  for i in range(len(eye)):
    p[i] = eye[i]
  pl = np.dot(RT, p)

  homoSolid2l = np.dot(iR, homoSolid2.T)
  homoSolid2l = homoSolid2l.T
  homoSolid1l = np.dot(iR, homoSolid1.T)
  homoSolid1l = homoSolid1l.T
  for i in range(len(solid[0])):
    for j in range(3):
      solid[0][i,j] = homoSolid2l[i,j]
  for i in range(len(solid[1])):
    for j in range(3):
      solid[1][i,j] = homoSolid1l[i,j]
  return solid

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

def plot2d(edgesList, colorList):
  fig = plt.figure(figsize=(8,8))
  ax = fig.add_subplot(111)

  for i in range(len(edgesList)):
      for j in edgesList[i]:
        ax.plot(j[:,0], j[:,1], color=colorList[i])

  plt.show()

def edgesQuadrilateral(points):
  P = points
  edges = np.array([ [P[0], P[1]],
                     [P[1], P[2]],
                     [P[2], P[3]],
                     [P[3], P[0]],
                     [P[0], P[4]],
                     [P[1], P[5]],
                     [P[2], P[6]],
                     [P[3], P[7]],
                     [P[4], P[5]],
                     [P[5], P[6]],
                     [P[6], P[7]],
                     [P[7], P[4]], ])
  return edges

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

changeds = baseChange([pyramidTrunk, parallelepiped])

edgesList = [edgesQuadrilateral(changeds[0]), edgesQuadrilateral(changeds[1])]
colorList = [ 'red', 'yellow']

plot2d(edgesList, colorList)
