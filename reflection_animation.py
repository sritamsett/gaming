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
    x.append(float(input(f"Enter x{i+1}: ")))
    y.append(float(input(f"Enter y{i+1}: ")))

# Close the polygon
x.append(x[0])
y.append(y[0])

# ==================================================
# REFLECTION MENU
# ==================================================

print("\n========== REFLECTION ==========")
print("1. Reflection about X-axis")
print("2. Reflection about Y-axis")
print("3. Reflection about Origin")
print("4. Reflection about line Y = X")
print("5. Reflection about line Y = -X")

choice = int(input("\nEnter your choice: "))

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

# Coordinate Labels
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
    label='Reflected Object'
)

# ==================================================
# ANIMATION
# ==================================================

frames = 120

def animate(frame):

    t = frame / (frames - 1)

    x_new = []
    y_new = []

    for i in range(len(x)):

        # Target reflected coordinates
        if choice == 1:          # X-axis
            tx = x[i]
            ty = -y[i]
            title = "Reflection about X-axis"

        elif choice == 2:        # Y-axis
            tx = -x[i]
            ty = y[i]
            title = "Reflection about Y-axis"

        elif choice == 3:        # Origin
            tx = -x[i]
            ty = -y[i]
            title = "Reflection about Origin"

        elif choice == 4:        # y = x
            tx = y[i]
            ty = x[i]
            title = "Reflection about Y = X"

        elif choice == 5:        # y = -x
            tx = -y[i]
            ty = -x[i]
            title = "Reflection about Y = -X"

        else:
            print("Invalid Choice!")
            exit()

        # Smooth interpolation
        xr = x[i] + (tx - x[i]) * t
        yr = y[i] + (ty - y[i]) * t

        x_new.append(xr)
        y_new.append(yr)

    line.set_data(x_new, y_new)
    ax.set_title(title)

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