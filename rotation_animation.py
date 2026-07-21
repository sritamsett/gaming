import matplotlib.pyplot as plt
import matplotlib.animation as animation
import math

# ==================================================
# INPUT OBJECT
# ==================================================

n = int(input("Enter number of vertices: "))

x = []
y = []

print("\nEnter coordinates of the object:")

for i in range(n):
    x_point = float(input(f"Enter x{i+1}: "))
    y_point = float(input(f"Enter y{i+1}: "))

    x.append(x_point)
    y.append(y_point)

# Close the polygon
x.append(x[0])
y.append(y[0])

# ==================================================
# ROTATION INPUT
# ==================================================

angle = float(input("\nEnter rotation angle (degrees): "))

# ==================================================
# FIGURE SETUP
# ==================================================

fig, ax = plt.subplots(figsize=(10, 10))

ax.axhline(0, color='black')
ax.axvline(0, color='black')
ax.grid(True, linestyle='--')

# Original Object
ax.plot(
    x,
    y,
    'bo--',
    linewidth=2,
    markersize=6,
    label='Original Object'
)

# Display Original Coordinates
for i in range(len(x) - 1):
    ax.text(
        x[i],
        y[i],
        f"({x[i]}, {y[i]})",
        fontsize=8,
        color='blue'
    )

# ==================================================
# AXIS LIMITS
# ==================================================

max_val = max(
    max(abs(v) for v in x),
    max(abs(v) for v in y)
)

max_val += 10

ax.set_xlim(-max_val, max_val)
ax.set_ylim(-max_val, max_val)

ax.set_aspect('equal')

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

# ==================================================
# ANIMATED OBJECT
# ==================================================

line, = ax.plot(
    [],
    [],
    'ro-',
    linewidth=3,
    markersize=8,
    label='Rotated Object'
)

# ==================================================
# ANIMATION
# ==================================================

frames = 120

def animate(frame):

    t = frame / (frames - 1)

    current_angle = angle * t
    rad = math.radians(current_angle)

    x_new = []
    y_new = []

    for i in range(len(x)):

        xr = (
            x[i] * math.cos(rad)
            - y[i] * math.sin(rad)
        )

        yr = (
            x[i] * math.sin(rad)
            + y[i] * math.cos(rad)
        )

        x_new.append(xr)
        y_new.append(yr)

    line.set_data(x_new, y_new)

    ax.set_title(
        f"Rotation Animation\n"
        f"Angle = {current_angle:.2f}°"
    )

    return line,

# ==================================================
# RUN ANIMATION
# ==================================================

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=frames,
    interval=30,
    blit=True,
    repeat=False
)

plt.legend()
plt.show()