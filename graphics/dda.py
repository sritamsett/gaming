import matplotlib.pyplot as plt

def draw_dda_line(x1, y1, x2, y2):
    # 1. Calculate differences
    dx = x2 - x1
    dy = y2 - y1

    # 2. Determine number of steps (greater of dx or dy)
    steps = int(max(abs(dx), abs(dy)))

    # 3. Calculate increments for each step
    x_inc = dx / steps
    y_inc = dy / steps

    # 4. Initialize current coordinates
    x, y = x1, y1
    x_points = []
    y_points = []

    # 5. Iterate and plot points
    for _ in range(steps + 1):
        x_points.append(round(x))
        y_points.append(round(y))
        x += x_inc
        y += y_inc

    return x_points, y_points

# Example usage
x1, y1 = 2, 2
x2, y2 = 10, 6
x_pts, y_pts = draw_dda_line(x1, y1, x2, y2)

# Visualization
plt.scatter(x_pts, y_pts, color='red')
plt.plot(x_pts, y_pts)
plt.title("DDA Line Drawing Algorithm")
plt.grid(True)
plt.show()
