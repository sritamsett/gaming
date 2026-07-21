import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------- QUADRANT FUNCTION ----------
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


# ---------- BRESENHAM ALGORITHM ----------
def bresenham_line(x1, y1, x2, y2):

    dx = abs(x2 - x1)
    dy = abs(y2 - y1)

    x, y = x1, y1

    sx = 1 if x2 > x1 else -1
    sy = 1 if y2 > y1 else -1

    x_points = []
    y_points = []

    print("\n========== BRESENHAM CALCULATIONS ==========")
    print(f"dx = {dx}")
    print(f"dy = {dy}")

    if dx > dy:
        p = 2 * dy - dx

        print("\nStep\tPixel\tDecision Parameter")

        for i in range(dx + 1):

            x_points.append(x)
            y_points.append(y)

            print(f"{i}\t({x},{y})\t{p}")

            x += sx

            if p < 0:
                p = p + 2 * dy
            else:
                y += sy
                p = p + 2 * dy - 2 * dx

    else:
        p = 2 * dx - dy

        print("\nStep\tPixel\tDecision Parameter")

        for i in range(dy + 1):

            x_points.append(x)
            y_points.append(y)

            print(f"{i}\t({x},{y})\t{p}")

            y += sy

            if p < 0:
                p = p + 2 * dx
            else:
                x += sx
                p = p + 2 * dx - 2 * dy

    return x_points, y_points


# ---------- MAIN PROGRAM ----------
print("=========== BRESENHAM LINE DRAWING ALGORITHM ===========")

x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

quadrant = find_quadrant(x1, y1, x2, y2)
print("\nLine is located in:", quadrant)

x_points, y_points = bresenham_line(x1, y1, x2, y2)

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
ax.set_title(f"Bresenham Line Drawing Algorithm\n{quadrant}")

# Scale
max_range = max(abs(x1), abs(y1), abs(x2), abs(y2)) + 5
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_aspect('equal')

# Quadrant Labels
ax.text(5, 5, "1st Quadrant", color='green')
ax.text(-15, 5, "2nd Quadrant", color='blue')
ax.text(-15, -5, "3rd Quadrant", color='red')
ax.text(5, -5, "4th Quadrant", color='purple')

# Start & End Points
ax.scatter(x1, y1, color='green', s=100, label='Start Point')
ax.scatter(x2, y2, color='red', s=100, label='End Point')

# Animated Line
line, = ax.plot([], [], color='blue', marker='o',
                linewidth=2, markersize=7,
                label='Bresenham Line')

pixel_labels = []

ax.legend()


# ---------- INITIALIZATION ----------
def init():
    line.set_data([], [])
    return line,


# ---------- ANIMATION ----------
def animate(i):

    # Draw line up to current pixel
    line.set_data(x_points[:i + 1], y_points[:i + 1])

    # Add coordinate label
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
    interval=500,      # 500 ms between pixels
    repeat=False,
    blit=False
)

plt.show()