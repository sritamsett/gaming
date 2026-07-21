import matplotlib.pyplot as plt

# Check if point is inside clipping edge
def inside(p, edge):
    x, y = p
    xmin, ymin, xmax, ymax = clip_window

    if edge == "LEFT":
        return x >= xmin
    elif edge == "RIGHT":
        return x <= xmax
    elif edge == "BOTTOM":
        return y >= ymin
    elif edge == "TOP":
        return y <= ymax


# Find intersection point
def intersection(p1, p2, edge):
    x1, y1 = p1
    x2, y2 = p2
    xmin, ymin, xmax, ymax = clip_window

    if edge == "LEFT":
        x = xmin
        y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)

    elif edge == "RIGHT":
        x = xmax
        y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)

    elif edge == "BOTTOM":
        y = ymin
        x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)

    elif edge == "TOP":
        y = ymax
        x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)

    return (x, y)


# Sutherland-Hodgman Clipping
def clip_polygon(polygon):

    edges = ["LEFT", "RIGHT", "BOTTOM", "TOP"]

    output = polygon

    for edge in edges:
        input_list = output
        output = []

        if not input_list:
            break

        s = input_list[-1]

        for e in input_list:

            if inside(e, edge):

                if inside(s, edge):
                    output.append(e)

                else:
                    output.append(intersection(s, e, edge))
                    output.append(e)

            elif inside(s, edge):
                output.append(intersection(s, e, edge))

            s = e

    return output


# ---------------- User Input ----------------

xmin = float(input("Enter xmin: "))
ymin = float(input("Enter ymin: "))
xmax = float(input("Enter xmax: "))
ymax = float(input("Enter ymax: "))

clip_window = (xmin, ymin, xmax, ymax)

n = int(input("Enter number of polygon vertices: "))

polygon = []

print("Enter polygon vertices (x y):")
for i in range(n):
    x = float(input(f"x{i+1}: "))
    y = float(input(f"y{i+1}: "))
    polygon.append((x, y))

# Clip Polygon
clipped = clip_polygon(polygon)

# ---------------- Output ----------------

print("\nOriginal Polygon:")
for p in polygon:
    print(p)

print("\nClipped Polygon:")
for p in clipped:
    print((round(p[0], 2), round(p[1], 2)))

# ---------------- Plot ----------------

plt.figure(figsize=(8,8))

# Clipping Window
window_x = [xmin, xmax, xmax, xmin, xmin]
window_y = [ymin, ymin, ymax, ymax, ymin]
plt.plot(window_x, window_y, 'k', linewidth=2, label="Clipping Window")

# Original Polygon
ox = [p[0] for p in polygon] + [polygon[0][0]]
oy = [p[1] for p in polygon] + [polygon[0][1]]
plt.plot(ox, oy, 'r--', linewidth=2, label="Original Polygon")

# Clipped Polygon
if clipped:
    cx = [p[0] for p in clipped] + [clipped[0][0]]
    cy = [p[1] for p in clipped] + [clipped[0][1]]
    plt.plot(cx, cy, 'b', linewidth=3, label="Clipped Polygon")

plt.grid(True)
plt.axis("equal")
plt.legend()
plt.title("Sutherland-Hodgman Polygon Clipping")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.show()