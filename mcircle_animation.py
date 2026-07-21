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


# ---------- RETURN 8 SYMMETRIC POINTS ----------
def get_circle_points(xc, yc, x, y):

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


# ---------- MIDPOINT CIRCLE DRAWING ----------
def midpoint_circle(xc, yc, r):

    x = 0
    y = r

    p = 1 - r

    frames = []
    plotted = []

    print("\n========== MIDPOINT CIRCLE CALCULATIONS ==========")
    print(f"Initial Decision Parameter p = {p}\n")

    while x <= y:

        current_points = get_circle_points(xc, yc, x, y)

        for pt in current_points:
            if pt not in plotted:
                plotted.append(pt)

        frames.append(plotted.copy())

        print(f"x = {x}\ty = {y}\tp = {p}")

        x += 1

        if p < 0:
            p = p + 2 * x + 1
        else:
            y -= 1
            p = p + 2 * x + 1 - 2 * y

    return frames


# ---------- MAIN PROGRAM ----------
print("=========== MIDPOINT CIRCLE DRAWING ALGORITHM ===========")

xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
r = int(input("Enter radius: "))

position = find_circle_position(xc, yc)

print("\nCircle Center is located in:", position)

frames = midpoint_circle(xc, yc, r)

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
ax.set_title(f"Midpoint Circle Drawing Algorithm\n{position}")

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
ax.scatter(xc, yc, color='red', s=120, label='Center')

# Animated Scatter
scatter = ax.scatter([], [], color='blue', s=40)

# Animated Line
circle_line, = ax.plot([], [], color='blue', linewidth=2)

labels = []

ax.legend()


# ---------- INITIALIZATION ----------
def init():
    scatter.set_offsets([[0, 0]])
    circle_line.set_data([], [])
    return scatter, circle_line


# ---------- ANIMATION FUNCTION ----------
def animate(frame):

    global labels

    # Remove previous labels
    for txt in labels:
        txt.remove()
    labels.clear()

    points = frames[frame]

    # Sort points by angle for smooth connection
    sorted_points = sorted(
        points,
        key=lambda p: math.atan2(p[1] - yc, p[0] - xc)
    )

    xs = [p[0] for p in sorted_points]
    ys = [p[1] for p in sorted_points]

    # Scatter points
    scatter.set_offsets(list(zip(xs, ys)))

    # Connect circle
    if len(xs) > 2:
        circle_line.set_data(xs + [xs[0]], ys + [ys[0]])

    # Coordinate Labels
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

    return [scatter, circle_line] + labels


# ---------- CREATE ANIMATION ----------
ani = FuncAnimation(
    fig,
    animate,
    init_func=init,
    frames=len(frames),
    interval=700,      # milliseconds between iterations
    repeat=False,
    blit=False
)

plt.show()