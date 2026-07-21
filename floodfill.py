import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np
from matplotlib.path import Path as MplPath
from collections import deque

WIDTH, HEIGHT = 100, 100
canvas = np.zeros((HEIGHT, WIDTH), dtype=int)

# 0 = background, 1 = boundary, 2 = filled, 3 = interior

n = int(input("Enter number of vertices: "))
vertices = []
print("Enter polygon coordinates:")
for i in range(n):
    x = int(input(f"x{i+1}: "))
    y = int(input(f"y{i+1}: "))
    vertices.append((x, y))

def draw_line(x1, y1, x2, y2):
    dx = abs(x2-x1)
    dy = abs(y2-y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx-dy
    while True:
        if 0 <= x1 < WIDTH and 0 <= y1 < HEIGHT:
            canvas[y1, x1] = 1
        if x1 == x2 and y1 == y2:
            break
        e2 = 2*err
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

for i in range(n):
    x1,y1 = vertices[i]
    x2,y2 = vertices[(i+1)%n]
    draw_line(x1,y1,x2,y2)

poly = MplPath(vertices)
for yy in range(HEIGHT):
    for xx in range(WIDTH):
        if poly.contains_point((xx,yy)) and canvas[yy,xx] == 0:
            canvas[yy,xx] = 3

seed_x = int(input("Enter Seed X: "))
seed_y = int(input("Enter Seed Y: "))

frames=[]
q=deque()

if 0 <= seed_x < WIDTH and 0 <= seed_y < HEIGHT and canvas[seed_y,seed_x]==3:
    q.append((seed_x,seed_y))
else:
    raise ValueError("Seed point must be inside the polygon.")

while q:
    x,y=q.popleft()
    if not (0 <= x < WIDTH and 0 <= y < HEIGHT):
        continue
    if canvas[y,x] != 3:
        continue
    canvas[y,x]=2
    frames.append(canvas.copy())
    q.append((x+1,y))
    q.append((x-1,y))
    q.append((x,y+1))
    q.append((x,y-1))

fig,ax=plt.subplots(figsize=(7,7))
img=ax.imshow(frames[0],origin="lower",interpolation="nearest",cmap="viridis")
px=[p[0] for p in vertices]+[vertices[0][0]]
py=[p[1] for p in vertices]+[vertices[0][1]]
ax.plot(px,py,"r-",linewidth=2)
ax.set_title("Flood Fill Algorithm")

def animate(i):
    img.set_array(frames[i])
    ax.set_title(f"Flood Fill Algorithm - Step {i+1}")
    return img,

ani=animation.FuncAnimation(fig,animate,frames=len(frames),interval=20,blit=True,repeat=False)
plt.show()
