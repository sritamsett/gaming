import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import numpy as np

# ------------------ WINDOW TO VIEWPORT FORMULA ------------------
def window_to_viewport(xw, yw,
                       XWmin, YWmin, XWmax, YWmax,
                       XVmin, YVmin, XVmax, YVmax):

    xv = XVmin + ((xw - XWmin) * (XVmax - XVmin)) / (XWmax - XWmin)
    yv = YVmin + ((yw - YWmin) * (YVmax - YVmin)) / (YWmax - YWmin)

    return xv, yv


# ------------------ INPUT ------------------
print("========== WINDOW TO VIEWPORT MAPPING ==========\n")

print("Enter Window Coordinates")
XWmin = int(input("Window Xmin: "))
YWmin = int(input("Window Ymin: "))
XWmax = int(input("Window Xmax: "))
YWmax = int(input("Window Ymax: "))

print("\nEnter Viewport Coordinates")
XVmin = int(input("Viewport Xmin: "))
YVmin = int(input("Viewport Ymin: "))
XVmax = int(input("Viewport Xmax: "))
YVmax = int(input("Viewport Ymax: "))

n = int(input("\nEnter number of polygon vertices: "))

window_points = []

print("\nEnter Polygon Coordinates")

for i in range(n):
    x = float(input(f"Vertex {i+1} X: "))
    y = float(input(f"Vertex {i+1} Y: "))
    window_points.append((x, y))

# Close Polygon
window_points.append(window_points[0])

# ------------------ MAP POINTS ------------------
viewport_points = []

for x, y in window_points:
    xv, yv = window_to_viewport(
        x, y,
        XWmin, YWmin, XWmax, YWmax,
        XVmin, YVmin, XVmax, YVmax
    )
    viewport_points.append((xv, yv))

# ------------------ FIGURE ------------------
fig, ax = plt.subplots(figsize=(12, 7))

# Window Rectangle
window_rect = plt.Rectangle(
    (XWmin, YWmin),
    XWmax - XWmin,
    YWmax - YWmin,
    fill=False,
    linewidth=2,
    color='blue',
    label='Window'
)

ax.add_patch(window_rect)

# Viewport Rectangle
viewport_rect = plt.Rectangle(
    (XVmin, YVmin),
    XVmax - XVmin,
    YVmax - YVmin,
    fill=False,
    linewidth=2,
    color='green',
    label='Viewport'
)

ax.add_patch(viewport_rect)

# Original Polygon
wx = [p[0] for p in window_points]
wy = [p[1] for p in window_points]

ax.plot(wx, wy,
        color='blue',
        marker='o',
        linewidth=2,
        label="Original Polygon")

# Animated Polygon
animated_line, = ax.plot([], [],
                         color='red',
                         marker='o',
                         linewidth=2,
                         label="Mapped Polygon")

labels = []

# ------------------ ANIMATION ------------------
steps = 40

frames = []

for t in np.linspace(0, 1, steps):

    frame = []

    for (x1, y1), (x2, y2) in zip(window_points, viewport_points):

        x = x1 + (x2 - x1) * t
        y = y1 + (y2 - y1) * t

        frame.append((x, y))

    frames.append(frame)


def init():
    animated_line.set_data([], [])
    return animated_line,


def animate(i):

    global labels

    for txt in labels:
        txt.remove()

    labels.clear()

    pts = frames[i]

    xs = [p[0] for p in pts]
    ys = [p[1] for p in pts]

    animated_line.set_data(xs, ys)

    for x, y in pts:
        labels.append(
            ax.text(
                x + 0.3,
                y + 0.3,
                f"({x:.1f},{y:.1f})",
                fontsize=8,
                color="darkred"
            )
        )

    return [animated_line] + labels


ani = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=len(frames),
    interval=80,
    repeat=False,
    blit=False
)

# ------------------ SETTINGS ------------------
ax.grid(True)

ax.set_title("Window to Viewport Mapping Animation")

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

ax.set_aspect('equal')

margin = 10

xmin = min(XWmin, XVmin) - margin
xmax = max(XWmax, XVmax) + margin

ymin = min(YWmin, YVmin) - margin
ymax = max(YWmax, YVmax) + margin

ax.set_xlim(xmin, xmax)
ax.set_ylim(ymin, ymax)

ax.legend()

plt.show()