import matplotlib.pyplot as plt

# ---------------- Point Clipping Function ----------------

def pointClip(x, y, xmin, ymin, xmax, ymax):

    if xmin <= x <= xmax and ymin <= y <= ymax:
        return True
    else:
        return False

# ---------------- User Input ----------------

xmin = float(input("Enter xmin: "))
ymin = float(input("Enter ymin: "))
xmax = float(input("Enter xmax: "))
ymax = float(input("Enter ymax: "))

x = float(input("Enter x-coordinate of the point: "))
y = float(input("Enter y-coordinate of the point: "))

# Check Point
accept = pointClip(x, y, xmin, ymin, xmax, ymax)

# ---------------- Output ----------------

if accept:
    print("\nPoint Accepted (Inside Clipping Window)")
    print(f"P = ({x:.2f}, {y:.2f})")
else:
    print("\nPoint Rejected (Outside Clipping Window)")
    print(f"P = ({x:.2f}, {y:.2f})")

# ---------------- Plot ----------------

plt.figure(figsize=(8, 8))

# Clipping Window
plt.plot([xmin, xmax], [ymin, ymin], 'k')
plt.plot([xmax, xmax], [ymin, ymax], 'k')
plt.plot([xmax, xmin], [ymax, ymax], 'k')
plt.plot([xmin, xmin], [ymax, ymin], 'k')

# Plot Point
if accept:
    plt.scatter(x, y, color='blue', s=100, label="Accepted Point")
else:
    plt.scatter(x, y, color='red', s=100, label="Rejected Point")

# Label Point
plt.text(x + 0.5, y + 0.5, f"P({x:.1f}, {y:.1f})")

plt.title("Point Clipping Algorithm")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()