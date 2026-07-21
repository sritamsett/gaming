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
# MENU
# ==================================================

print("\n========== 2D TRANSFORMATIONS ==========")
print("1. Translation")
print("2. Scaling")
print("3. Rotation")
print("4. Shearing")

choice = int(input("\nEnter your choice: "))

# ==================================================
# PARAMETERS
# ==================================================

tx = ty = 0
sx = sy = 1
angle = 0
shx = shy = 0

if choice == 1:
    tx = float(input("Enter translation in x direction: "))
    ty = float(input("Enter translation in y direction: "))

elif choice == 2:
    sx = float(input("Enter scaling factor in x direction: "))
    sy = float(input("Enter scaling factor in y direction: "))

elif choice == 3:
    angle = float(input("Enter rotation angle in degrees: "))

elif choice == 4:
    shx = float(input("Enter shearing factor in x direction: "))
    shy = float(input("Enter shearing factor in y direction: "))

else:
    print("Invalid Choice!")
    exit()

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
    label='Original Object'
)

# Display coordinates
for i in range(len(x) - 1):
    ax.text(
        x[i],
        y[i],
        f"({x[i]}, {y[i]})",
        fontsize=8
    )

# Axis limits
max_val = max(
    max(abs(v) for v in x),
    max(abs(v) for v in y)
)

if choice == 1:
    max_val += abs(tx) + abs(ty)

elif choice == 2:
    max_val *= max(abs(sx), abs(sy), 1)

elif choice == 3:
    max_val += 5

elif choice == 4:
    max_val *= (1 + abs(shx) + abs(shy))

max_val += 10

ax.set_xlim(-max_val, max_val)
ax.set_ylim(-max_val, max_val)

ax.set_aspect('equal')

ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")

# Animated Object
line, = ax.plot(
    [],
    [],
    'ro-',
    linewidth=3,
    markersize=8,
    label='Transformed Object'
)

# ==================================================
# ANIMATION
# ==================================================

frames = 120

def animate(frame):

    t = frame / (frames - 1)

    x_new = []
    y_new = []

    # ---------------- TRANSLATION ----------------
    if choice == 1:

        current_tx = tx * t
        current_ty = ty * t

        x_new = [xi + current_tx for xi in x]
        y_new = [yi + current_ty for yi in y]

        ax.set_title(
            f"Translation Animation\n"
            f"Tx={current_tx:.2f}, Ty={current_ty:.2f}"
        )

    # ---------------- SCALING ----------------
    elif choice == 2:

        current_sx = 1 + (sx - 1) * t
        current_sy = 1 + (sy - 1) * t

        x_new = [xi * current_sx for xi in x]
        y_new = [yi * current_sy for yi in y]

        ax.set_title(
            f"Scaling Animation\n"
            f"Sx={current_sx:.2f}, Sy={current_sy:.2f}"
        )

    # ---------------- ROTATION ----------------
    elif choice == 3:

        current_angle = angle * t

        rad = math.radians(current_angle)

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

        ax.set_title(
            f"Rotation Animation\n"
            f"Angle={current_angle:.2f}°"
        )

    # ---------------- SHEARING ----------------
    elif choice == 4:

        current_shx = shx * t
        current_shy = shy * t

        for i in range(len(x)):

            xs = x[i] + current_shx * y[i]
            ys = y[i] + current_shy * x[i]

            x_new.append(xs)
            y_new.append(ys)

        ax.set_title(
            f"Shearing Animation\n"
            f"Shx={current_shx:.2f}, Shy={current_shy:.2f}"
        )

    line.set_data(x_new, y_new)

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