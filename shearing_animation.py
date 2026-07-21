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
# SHEARING MENU
# ==================================================

print("\n========== SHEARING ==========")
print("1. X-Shearing")
print("2. Y-Shearing")
print("3. Both X and Y Shearing")

choice = int(input("\nEnter your choice: "))

shx = 0
shy = 0

if choice == 1:

    shx = float(input("Enter X-Shearing Factor: "))
    label = "X-Shearing Animation"

elif choice == 2:

    shy = float(input("Enter Y-Shearing Factor: "))
    label = "Y-Shearing Animation"

elif choice == 3:

    shx = float(input("Enter X-Shearing Factor: "))
    shy = float(input("Enter Y-Shearing Factor: "))
    label = "X & Y Shearing Animation"

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

max_val *= (1 + abs(shx) + abs(shy))
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
    label='Sheared Object'
)

# ==================================================
# ANIMATION
# ==================================================

frames = 120

def animate(frame):

    t = frame / (frames - 1)

    current_shx = shx * t
    current_shy = shy * t

    x_new = []
    y_new = []

    # ---------------- X-SHEARING ----------------

    if choice == 1:

        for i in range(len(x)):

            xs = x[i] + current_shx * y[i]
            ys = y[i]

            x_new.append(xs)
            y_new.append(ys)

        ax.set_title(
            f"{label}\n"
            f"Shx = {current_shx:.2f}"
        )

    # ---------------- Y-SHEARING ----------------

    elif choice == 2:

        for i in range(len(x)):

            xs = x[i]
            ys = y[i] + current_shy * x[i]

            x_new.append(xs)
            y_new.append(ys)

        ax.set_title(
            f"{label}\n"
            f"Shy = {current_shy:.2f}"
        )

    # ---------------- BOTH SHEARING ----------------

    elif choice == 3:

        for i in range(len(x)):

            xs = x[i] + current_shx * y[i]
            ys = y[i] + current_shy * x[i]

            x_new.append(xs)
            y_new.append(ys)

        ax.set_title(
            f"{label}\n"
            f"Shx = {current_shx:.2f}, "
            f"Shy = {current_shy:.2f}"
        )

    line.set_data(x_new, y_new)

    return line,

# ==================================================
# RUN ANIMATION
# ==================================================

ani = animation.FuncAnimation(
    fig,
    animate,
    frames=120,
    interval=30,
    blit=True,
    repeat=False
)

plt.legend()
plt.show()