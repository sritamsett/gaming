import matplotlib.pyplot as plt

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
def plot_circle_points(xc, yc, x, y, points):

    symmetric_points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]

    for point in symmetric_points:
        if point not in points:
            points.append(point)


# ---------- BRESENHAM CIRCLE ----------
def bresenham_circle(xc, yc, r):

    x = 0
    y = r

    p = 3 - 2 * r

    points = []

    print("\n========== BRESENHAM CIRCLE CALCULATIONS ==========")
    print(f"Initial Decision Parameter p = {p}\n")

    while x <= y:

        plot_circle_points(xc, yc, x, y, points)

        print(f"x = {x}\ty = {y}\tp = {p}")

        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1

        x += 1

    return points


# ---------- MAIN PROGRAM ----------
print("=========== BRESENHAM CIRCLE DRAWING ALGORITHM ===========")

xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
r = int(input("Enter radius: "))

position = find_circle_position(xc, yc)

print("\nCircle Center is located in:", position)

points = bresenham_circle(xc, yc, r)

# ---------- SORT POINTS FOR SMOOTH CONNECTION ----------
points = sorted(points, key=lambda p: (
    __import__('math').atan2(p[1] - yc, p[0] - xc)
))

x_points = [p[0] for p in points]
y_points = [p[1] for p in points]

# Close the circle
x_points.append(x_points[0])
y_points.append(y_points[0])

# ---------- PLOTTING ----------
plt.figure(figsize=(10, 10))

# Axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# ---------- CONNECTIVE LINES ----------
plt.plot(
    x_points,
    y_points,
    color='blue',
    linewidth=2,
    marker='o',
    markersize=6,
    label='Bresenham Circle'
)

# Center Point
plt.scatter(xc, yc, color='red', s=120, label='Center')

# ---------- PIXEL LABELS ----------
for i in range(len(points)):
    plt.text(
        points[i][0] + 0.15,
        points[i][1] + 0.15,
        f"({points[i][0]},{points[i][1]})",
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

plt.title(f"Bresenham Circle Drawing Algorithm\n{position}")

# Limits
max_range = max(abs(xc), abs(yc), r) + 5

plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.axis('equal')
plt.legend()

plt.show()