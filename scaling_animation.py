import matplotlib.pyplot as plt
import matplotlib.animation as animation

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
# SCALING INPUT
# ==================================================

sx = float(input("\nEnter scaling factor in x direction: "))
sy = float(input("Enter scaling factor in y direction: "))

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

# Display original coordinates
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

max_scale = max(abs(sx), abs(sy), 1)
max_val *= max_scale
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
    label='Scaled Object'
)

# ==================================================
# ANIMATION
# ==================================================

frames = 120

def animate(frame):

    t = frame / (frames - 1)

    # Smooth scaling from 1 → target scale
    current_sx = 1 + (sx - 1) * t
    current_sy = 1 + (sy - 1) * t

    x_new = [xi * current_sx for xi in x]
    y_new = [yi * current_sy for yi in y]

    line.set_data(x_new, y_new)

    ax.set_title(
        f"Scaling Animation\n"
        f"Sx = {current_sx:.2f}, Sy = {current_sy:.2f}"
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