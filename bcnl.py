import matplotlib.pyplot as plt

# ---------- QUADRANT / POSITION FUNCTION ----------
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


# ---------- PLOT 8 SYMMETRIC POINTS ----------
def plot_circle_points(xc, yc, x, y, x_points, y_points):

    points = [
        (xc + x, yc + y),
        (xc - x, yc + y),
        (xc + x, yc - y),
        (xc - x, yc - y),
        (xc + y, yc + x),
        (xc - y, yc + x),
        (xc + y, yc - x),
        (xc - y, yc - x)
    ]

    for px, py in points:
        x_points.append(px)
        y_points.append(py)


# ---------- BRESENHAM CIRCLE DRAWING ALGORITHM ----------
def bresenham_circle(xc, yc, r):

    x = 0
    y = r

    p = 3 - 2 * r

    x_points = []
    y_points = []

    print("\n========== BRESENHAM CIRCLE CALCULATIONS ==========")
    print(f"Initial Decision Parameter p = {p}\n")

    while x <= y:

        plot_circle_points(xc, yc, x, y, x_points, y_points)

        print(f"x = {x}\ty = {y}\tp = {p}")

        if p < 0:
            p = p + 4 * x + 6
        else:
            p = p + 4 * (x - y) + 10
            y -= 1

        x += 1

    return x_points, y_points


# ---------- MAIN PROGRAM ----------
print("=========== BRESENHAM CIRCLE DRAWING ALGORITHM ===========")

xc = int(input("Enter center x-coordinate: "))
yc = int(input("Enter center y-coordinate: "))
r = int(input("Enter radius: "))

position = find_circle_position(xc, yc)

print("\nCircle Center is located in:", position)

x_points, y_points = bresenham_circle(xc, yc, r)

# ---------- PLOTTING ----------
plt.figure(figsize=(10, 10))

# Axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# Circle Pixels
plt.scatter(x_points, y_points, color='blue', s=40, label='Circle Pixels')

# Center Point
plt.scatter(xc, yc, color='red', s=120, label='Center')

# ---------- PIXEL LABELS ----------
for i in range(len(x_points)):
    plt.text(
        x_points[i] + 0.15,
        y_points[i] + 0.15,
        f"({x_points[i]},{y_points[i]})",
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