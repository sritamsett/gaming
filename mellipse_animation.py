import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# ---------- POSITION FUNCTION ----------
def find_ellipse_position(xc, yc):

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


# ---------- RETURN 4 SYMMETRIC POINTS ----------
def get_ellipse_points(xc, yc, x, y):

    return [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ]


# ---------- MIDPOINT ELLIPSE DRAWING ----------
def midpoint_ellipse(xc, yc, rx, ry):

    frames = []
    plotted = []

    x = 0
    y = ry

    rx2 = rx * rx
    ry2 = ry * ry

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    print("\n========== REGION 1 ==========")

    # -------- REGION 1 --------
    while dx < dy:

        current = get_ellipse_points(xc, yc, x, y)

        for pt in current:
            if pt not in plotted:
                plotted.append(pt)

        frames.append(plotted.copy())

        print(f"x={x}\ty={y}\tp1={p1}")

        x += 1
        dx = 2 * ry2 * x

        if p1 < 0:
            p1 = p1 + dx + ry2
        else:
            y -= 1
            dy = 2 * rx2 * y
            p1 = p1 + dx - dy + ry2

    p2 = (
        ry2 * (x + 0.5) ** 2 +
        rx2 * (y - 1) ** 2 -
        rx2 * ry2
    )

    print("\n========== REGION 2 ==========")

    # -------- REGION 2 --------
    while y >= 0:

        current = get_ellipse_points(xc, yc, x, y)

        for pt in current:
            if pt not in plotted:
                plotted.append(pt)

        frames.append(plotted.copy())

        print(f"x={x}\ty={y}\tp2={p2}")

        y -= 1
        dy = 2 * rx2 * y

        if p2 > 0:
            p2 = p2 + rx2 - dy
        else:
            x += 1
            dx = 2 * ry2 * x
            p2 = p2 + dx - dy + rx2

    return frames


# ---------- MAIN PROGRAM ----------
print("=========== MIDPOINT ELLIPSE DRAWING ALGORITHM ===========")

xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
rx = int(input("Enter x-radius (rx): "))
ry = int(input("Enter y-radius (ry): "))

position = find_ellipse_position(xc, yc)

print("\nEllipse Center is located in:", position)

frames = midpoint_ellipse(xc, yc, rx, ry)

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
ax.set_title(f"Midpoint Ellipse Drawing Algorithm\n{position}")

# Limits
max_range = max(abs(xc), abs(yc), rx, ry) + 5
ax.set_xlim(-max_range, max_range)
ax.set_ylim(-max_range, max_range)
ax.set_aspect('equal')

# Quadrant Labels
ax.text(5, 5, "1st Quadrant", color='green')
ax.text(-15, 5, "2nd Quadrant", color='blue')
ax.text(-15, -5, "3rd Quadrant", color='red')
ax.text(5, -5, "4th Quadrant", color='purple')

# Center
ax.scatter(xc, yc, color='red', s=120, label="Center")

# Animated scatter
scatter = ax.scatter([], [], color="orange", s=50)

labels = []

ax.legend()


# ---------- INITIALIZATION ----------
def init():
    scatter.set_offsets([[0, 0]])
    return scatter,


# ---------- ANIMATION ----------
def animate(frame):

    global labels

    # Remove previous labels
    for txt in labels:
        txt.remove()
    labels.clear()

    points = frames[frame]

    xs = [p[0] for p in points]
    ys = [p[1] for p in points]

    scatter.set_offsets(list(zip(xs, ys)))

    # Coordinate labels
    for x, y in points:
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
    interval=600,      # milliseconds
    repeat=False,
    blit=False
)

plt.show()