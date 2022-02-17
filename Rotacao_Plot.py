
#ROTAÇÃO

import matplotlib.pyplot as plt
import math
import numpy as np

def rotacao(ang_tmp):
    rot = np.array([ [math.cos(ang_tmp) , -math.sin(ang_tmp)], [math.sin(ang_tmp), math.cos(ang_tmp)] ])
    return rot

elo = 2
elo_ang1 = 30
elo_theta = -30

ang_tmp = math.radians(elo_ang1)
x1 = elo*math.cos(ang_tmp)
y1 = elo*math.sin(ang_tmp)
eixo_x1 = [0, x1]
eixo_y1 = [0, y1]

ang_tmp = math.radians(elo_theta)
pos1 = np.array([x1, y1])
[x2, y2] = pos1 @ rotacao(ang_tmp)
eixo_x2 = [0, x2]
eixo_y2 = [0, y2]

plt.plot(eixo_x1, eixo_y1, label = "linha1")
plt.plot(eixo_x2, eixo_y2, label = "linha2")

plt.title("Braço robotico")
plt.xlabel("X")
plt.ylabel("Y")
plt.legend(bbox_to_anchor=(0.5,1))
plt.grid(True)

plt.show()

#PLOT 3D

import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

x = [5]
y = [5]
z = [5]

fig = plt.figure()
ax = fig.add_subplot(1,1,1, projection='3d')
ax.set_xlim(0, 10)
ax.set_ylim(0, 10)
ax.set_zlim(0, 10)
ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")

ax.plot([0,x[0]], [0, y[0]], zs=[0,z[0]], linewidth=2)
plt.show()

eixo_x = [0, x[0]]
eixo_y = [0, y[0]]
eixo_z = [0, z[0]]
plt.plot(eixo_x, eixo_y, label = "XY")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid()
plt.show()
plt.plot(eixo_x, eixo_z, label = "XZ")
plt.xlabel("X")
plt.ylabel("Z")
plt.grid()
plt.show
plt.plot(eixo_y, eixo_z, label = "YZ")
plt.xlabel("Y")
plt.ylabel("Z")
plt.grid()
plt.show
