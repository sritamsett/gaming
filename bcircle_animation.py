import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import math

# ---------- POSITION FUNCTION ----------
def find_circle_position(xc, yc):

    if xc > 0 and yc > 0:
        return "1st Quadrant"
    elif xc < 0 and yc > 0:
        return "2nd Quadrant"
    elif xc < 0 and yc < 0:
        return "3rd Quadrant"
    elif xc > 0 and yc < 0:
        return "4th Quadrant"
    elif xc == 0 and yc == 0:
        return "Origin"
    elif xc == 0:
        return "On Y-Axis"
    elif yc == 0:
        return "On X-Axis"


# ---------- STORE 8 SYMMETRIC POINTS ----------
def plot_circle_points(xc, yc, x, y):

    return [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]


# ---------- BRESENHAM CIRCLE ----------
def bresenham_circle(xc, yc, r):

    x = 0
    y = r

    p = 3 - 2 * r

    frames = []
    plotted = []

    print("\n========== BRESENHAM CIRCLE CALCULATIONS ==========")
    print(f"Initial Decision Parameter p = {p}\n")

    while x <= y:

        current_points = plot_circle_points(xc, yc, x, y)

        for pt in current_points:
            if pt not in plotted:
                plotted.append(pt)

        frames.append(plotted.copy())

        print(f"x = {x}\ty = {y}\tp = {p}")

        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1

        x += 1

    return frames


# ---------- MAIN PROGRAM ----------
print("=========== BRESENHAM CIRCLE DRAWING ALGORITHM ===========")

xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
r = int(input("Enter radius: "))

position = find_circle_position(xc, yc)

print("\nCircle Center is located in:", position)

frames = bresenham_circle(xc, yc, r)

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
ax.set_title(f"Bresenham Circle Drawing Algorithm\n{position}")

# Limits
max_range = max(abs(xc), abs(yc), r) + 5
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_aspect('equal')

# Quadrant Labels
ax.text(5, 5, "1st Quadrant", color='green')
ax.text(-15, 5, "2nd Quadrant", color='blue')
ax.text(-15, -5, "3rd Quadrant", color='red')
ax.text(5, -5, "4th Quadrant", color='purple')

# Center Point
ax.scatter(xc, yc, color='red', s=120, label="Center")

# Animated Scatter
scatter = ax.scatter([], [], color='blue', s=40)

labels = []

ax.legend()


# ---------- INITIALIZATION ----------
def init():
    scatter.set_offsets([])
    return scatter,


# ---------- ANIMATION ----------
def animate(i):

    global labels

    # Remove previous labels
    for txt in labels:
        txt.remove()
    labels.clear()

    points = frames[i]

    # Sort points to connect smoothly
    sorted_points = sorted(
        points,
        key=lambda p: math.atan2(p[1] - yc, p[0] - xc)
    )

    xs = [p[0] for p in sorted_points]
    ys = [p[1] for p in sorted_points]

    scatter.set_offsets(list(zip(xs, ys)))

    # Connect points
    if len(xs) > 2:
        xs2 = xs + [xs[0]]
        ys2 = ys + [ys[0]]

        ax.lines = ax.lines[:2]  # Keep only axes

        ax.plot(xs2, ys2,
                color='blue',
                linewidth=2,
                marker='o',
                markersize=5)

    # Coordinate labels
    for x, y in sorted_points:
        labels.append(
            ax.text(
                x + 0.15,
                y + 0.15,
                f"({x},{y})",
                fontsize=8,
                color="darkblue"
            )
        )

    return [scatter] + labels


# ---------- CREATE ANIMATION ----------
ani = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=len(frames),
    interval=700,      # milliseconds
    repeat=False,
    blit=False
)

plt.show()