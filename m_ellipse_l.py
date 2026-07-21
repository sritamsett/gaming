import matplotlib.pyplot as plt
import math

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


# ---------- STORE 4 SYMMETRIC POINTS ----------
def plot_ellipse_points(xc, yc, x, y, points):

    symmetric_points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y)
    ]

    for point in symmetric_points:
        if point not in points:
            points.append(point)


# ---------- MIDPOINT ELLIPSE DRAWING ALGORITHM ----------
def midpoint_ellipse(xc, yc, rx, ry):

    points = []

    x = 0
    y = ry

    # Squares
    rx2 = rx * rx
    ry2 = ry * ry

    # ---------- REGION 1 ----------
    p1 = ry2 - (rx2 * ry) + (0.25 * rx2)

    dx = 2 * ry2 * x
    dy = 2 * rx2 * y

    print("\n========== REGION 1 CALCULATIONS ==========")

    while dx < dy:

        plot_ellipse_points(xc, yc, x, y, points)

        print(f"x = {x}\ty = {y}\tp1 = {p1}")

        x += 1
        dx = 2 * ry2 * x

        if p1 < 0:
            p1 = p1 + dx + ry2
        else:
            y -= 1
            dy = 2 * rx2 * y
            p1 = p1 + dx - dy + ry2

    # ---------- REGION 2 ----------
    p2 = (
        (ry2) * ((x + 0.5) ** 2)
        + (rx2) * ((y - 1) ** 2)
        - (rx2 * ry2)
    )

    print("\n========== REGION 2 CALCULATIONS ==========")

    while y >= 0:

        plot_ellipse_points(xc, yc, x, y, points)

        print(f"x = {x}\ty = {y}\tp2 = {p2}")

        y -= 1
        dy = 2 * rx2 * y

        if p2 > 0:
            p2 = p2 + rx2 - dy
        else:
            x += 1
            dx = 2 * ry2 * x
            p2 = p2 + dx - dy + rx2

    return points


# ---------- MAIN PROGRAM ----------
print("=========== MIDPOINT ELLIPSE DRAWING ALGORITHM ===========")

xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))

rx = int(input("Enter x-radius (rx): "))
ry = int(input("Enter y-radius (ry): "))

position = find_ellipse_position(xc, yc)

print("\nEllipse Center is located in:", position)

points = midpoint_ellipse(xc, yc, rx, ry)

# ---------- SORT POINTS IN CIRCULAR ORDER ----------
points = sorted(
    points,
    key=lambda p: math.atan2(p[1] - yc, p[0] - xc)
)

# Close the ellipse
points.append(points[0])

# Separate x and y coordinates
x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

# ---------- PLOTTING ----------
plt.figure(figsize=(10, 10))

# Axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# ---------- CONNECTED ELLIPSE ----------
plt.plot(
    x_points,
    y_points,
    color='orange',
    marker='o',
    linestyle='-',
    linewidth=2,
    markersize=6,
    label='Midpoint Ellipse'
)

# Center Point
plt.scatter(
    xc,
    yc,
    color='red',
    s=120,
    label='Center'
)

# ---------- PIXEL LABELS ----------
for point in points[:-1]:

    plt.text(
        point[0] + 0.15,
        point[1] + 0.15,
        f"({point[0]},{point[1]})",
        fontsize=8,
        color='darkblue'
    )

# Quadrant Labels
plt.text(5, 5, "1st Quadrant", color='green')
plt.text(-15, 5, "2nd Quadrant", color='blue')
plt.text(-15, -5, "3rd Quadrant", color='red')
plt.text(5, -5, "4th Quadrant", color='purple')

# Grid
plt.grid(True, linestyle='--')

# Labels
plt.xlabel("X Axis")
plt.ylabel("Y Axis")

plt.title(f"Midpoint Ellipse Drawing Algorithm\n{position}")

# Limits
max_range = max(abs(xc), abs(yc), rx, ry) + 5

plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.axis('equal')
plt.legend()

plt.show()