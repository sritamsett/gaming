import matplotlib.pyplot as plt

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

        for i in range(dx + 1):

            x_points.append(x)
            y_points.append(y)

            print(f"{i}\t({x},{y})\tp={p}")

            x += sx

            if p < 0:
                p = p + 2 * dy
            else:
                y += sy
                p = p + 2 * dy - 2 * dx

    else:
        p = 2 * dx - dy

        for i in range(dy + 1):

            x_points.append(x)
            y_points.append(y)

            print(f"{i}\t({x},{y})\tp={p}")

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

# ---------- PLOTTING ----------
plt.figure(figsize=(10, 10))

# Axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# Line
plt.plot(x_points, y_points, marker='o', color='blue', label='Bresenham Line')

# Start & End points
plt.scatter(x1, y1, color='green', s=100, label='Start Point')
plt.scatter(x2, y2, color='red', s=100, label='End Point')

# ---------- PIXEL LABELS ----------
for i in range(len(x_points)):
    plt.text(
        x_points[i] + 0.15,
        y_points[i] + 0.15,
        f"{x_points[i]},{y_points[i]}",
        fontsize=9,
        color='darkblue'
    )

# Quadrant labels
plt.text(5, 5, "1st Quadrant", color='green')
plt.text(-15, 5, "2nd Quadrant", color='blue')
plt.text(-15, -5, "3rd Quadrant", color='red')
plt.text(5, -5, "4th Quadrant", color='purple')

# Grid
plt.grid(True, linestyle='--')

# Labels
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title(f"Bresenham Line Drawing Algorithm\n{quadrant}")

# Limits
max_range = max(abs(x1), abs(y1), abs(x2), abs(y2)) + 5
plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)

plt.axis('equal')
plt.legend()

plt.show()
