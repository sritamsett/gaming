import matplotlib.pyplot as plt

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

# ---------- PLOTTING ----------
plt.figure(figsize=(10, 10))

# Axes
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# Line
plt.plot(x_points, y_points, marker='o', color='orange', label='DDA Line')

# Start & End
plt.scatter(x1, y1, color='green', s=100, label='Start')
plt.scatter(x2, y2, color='red', s=100, label='End')

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

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title(f"DDA Line Drawing Algorithm\n{quadrant}")

# Scale
max_range = max(abs(x1), abs(y1), abs(x2), abs(y2)) + 5
plt.xlim(-max_range, max_range)
plt.ylim(-max_range, max_range)
plt.axis('equal')

plt.legend()
plt.show()