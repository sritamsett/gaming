import numpy as np
import matplotlib.pyplot as plt

# Function to compute a point on the Bezier curve using De Casteljau algorithm
def bezier_point(control_points, t):
    points = np.array(control_points, dtype=float)

    while len(points) > 1:
        points = (1 - t) * points[:-1] + t * points[1:]

    return points[0]

# -------------------------
# User Input
# -------------------------
n = int(input("Enter the number of control points: "))

control_points = []

print("Enter the control points (x y):")
for i in range(n):
    x = float(input(f"Enter x{i+1}: "))
    y = float(input(f"Enter y{i+1}: "))
    control_points.append([x, y])

# Generate Bezier Curve
curve = []

for t in np.linspace(0, 1, 500):
    curve.append(bezier_point(control_points, t))

curve = np.array(curve)
control_points = np.array(control_points)

# -------------------------
# Plot
# -------------------------
plt.figure(figsize=(8,6))

# Control Polygon
plt.plot(control_points[:,0], control_points[:,1],
         'ro--', linewidth=1.5, label="Control Polygon")

# Bezier Curve
plt.plot(curve[:,0], curve[:,1],
         'b', linewidth=3, label="Bezier Curve")

# Label Control Points
for i, p in enumerate(control_points):
    plt.text(p[0], p[1], f"P{i}", fontsize=10)

plt.title("Bezier Curve")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()