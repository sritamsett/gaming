import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------- FUNCTION TO FIND QUADRANT ----------
def find_quadrant(x1, y1, x2, y2):

    mx = (x1 + x2) / 2
    my = (y1 + y2) / 2

    if mx > 0 and my > 0:
        return "1st Quadrant"
    elif mx < 0 and my > 0:
        return "2nd Quadrant"
    elif mx < 0 and my < 0:
        return "3rd Quadrant"
    elif mx > 0 and my < 0:
        return "4th Quadrant"
    elif mx == 0 and my == 0:
        return "Origin"
    elif mx == 0:
        return "On Y-Axis"
    elif my == 0:
        return "On X-Axis"


# ---------- DDA LINE FUNCTION ----------
def dda_line(x1, y1, x2, y2):

    dx = x2 - x1
    dy = y2 - y1

    steps = max(abs(dx), abs(dy))

    x_inc = dx / steps
    y_inc = dy / steps

    print("\n========== DDA CALCULATIONS ==========")
    print(f"dx = {dx}")
    print(f"dy = {dy}")
    print(f"Steps = {steps}")
    print(f"X Increment = {x_inc}")
    print(f"Y Increment = {y_inc}")

    x = x1
    y = y1

    x_points = []
    y_points = []

    print("\nStep\tX\tY\tPixel")

    for i in range(steps + 1):

        rx = round(x)
        ry = round(y)

        x_points.append(rx)
        y_points.append(ry)

        print(f"{i}\t{x:.2f}\t{y:.2f}\t({rx}, {ry})")

        x += x_inc
        y += y_inc

    return x_points, y_points


# ---------- MAIN PROGRAM ----------
print("=========== DDA LINE DRAWING ALGORITHM ===========")

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

quadrant = find_quadrant(x1, y1, x2, y2)
print("\nLine is located in:", quadrant)

x_points, y_points = dda_line(x1, y1, x2, y2)

# ---------- PLOT SETUP ----------
fig, ax = plt.subplots(figsize=(10, 10))

# Axes
ax.axhline(0, color='black', linewidth=2)
ax.axvline(0, color='black', linewidth=2)

# Grid
ax.grid(True, linestyle='--')

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_title(f"DDA Line Drawing Algorithm\n{quadrant}")

# Scale
max_range = max(abs(x1), abs(y1), abs(x2), abs(y2)) + 5
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_aspect('equal')

# Quadrant labels
ax.text(5, 5, "1st Quadrant", color='green')
ax.text(-15, 5, "2nd Quadrant", color='blue')
ax.text(-15, -5, "3rd Quadrant", color='red')
ax.text(5, -5, "4th Quadrant", color='purple')

# Start & End Points
ax.scatter(x1, y1, color='green', s=100, label='Start')
ax.scatter(x2, y2, color='red', s=100, label='End')

# Animated line
line, = ax.plot([], [], color='orange', marker='o',
                linewidth=2, markersize=7, label='DDA Line')

# Store text labels
pixel_labels = []

ax.legend()


# ---------- INITIALIZE ----------
def init():
    line.set_data([], [])
    return line,


# ---------- ANIMATION FUNCTION ----------
def animate(i):

    # Draw line till current point
    line.set_data(x_points[:i + 1], y_points[:i + 1])

    # Add pixel label
    txt = ax.text(
        x_points[i] + 0.15,
        y_points[i] + 0.15,
        f"({x_points[i]}, {y_points[i]})",
        fontsize=9,
        color="darkblue"
    )

    pixel_labels.append(txt)

    return [line] + pixel_labels


# ---------- CREATE ANIMATION ----------
ani = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=len(x_points),
    interval=500,      # milliseconds between points
    repeat=False,
    blit=False
)

plt.show()