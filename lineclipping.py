import matplotlib.pyplot as plt

# Region Codes
INSIDE = 0
LEFT = 1
RIGHT = 2
BOTTOM = 4
TOP = 8

# Compute Region Code
def computeCode(x, y, xmin, ymin, xmax, ymax):
    code = INSIDE

    if x < xmin:
        code |= LEFT
    elif x > xmax:
        code |= RIGHT

    if y < ymin:
        code |= BOTTOM
    elif y > ymax:
        code |= TOP

    return code

# Cohen-Sutherland Line Clipping Algorithm
def cohenSutherlandClip(x1, y1, x2, y2, xmin, ymin, xmax, ymax):

    code1 = computeCode(x1, y1, xmin, ymin, xmax, ymax)
    code2 = computeCode(x2, y2, xmin, ymin, xmax, ymax)

    accept = False

    while True:

        # Both endpoints inside
        if code1 == 0 and code2 == 0:
            accept = True
            break

        # Both endpoints outside in same region
        elif (code1 & code2) != 0:
            break

        else:
            if code1 != 0:
                code_out = code1
            else:
                code_out = code2

            # Find intersection point
            if code_out & TOP:
                x = x1 + (x2 - x1) * (ymax - y1) / (y2 - y1)
                y = ymax

            elif code_out & BOTTOM:
                x = x1 + (x2 - x1) * (ymin - y1) / (y2 - y1)
                y = ymin

            elif code_out & RIGHT:
                y = y1 + (y2 - y1) * (xmax - x1) / (x2 - x1)
                x = xmax

            elif code_out & LEFT:
                y = y1 + (y2 - y1) * (xmin - x1) / (x2 - x1)
                x = xmin

            if code_out == code1:
                x1 = x
                y1 = y
                code1 = computeCode(x1, y1, xmin, ymin, xmax, ymax)

            else:
                x2 = x
                y2 = y
                code2 = computeCode(x2, y2, xmin, ymin, xmax, ymax)

    return accept, x1, y1, x2, y2

# ---------------- User Input ----------------

xmin = float(input("Enter xmin: "))
ymin = float(input("Enter ymin: "))
xmax = float(input("Enter xmax: "))
ymax = float(input("Enter ymax: "))

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

# Save original line
ox1, oy1, ox2, oy2 = x1, y1, x2, y2

accept, x1, y1, x2, y2 = cohenSutherlandClip(
    x1, y1, x2, y2,
    xmin, ymin, xmax, ymax
)

# ---------------- Output ----------------

if accept:
    print("\nLine Accepted")
    print(f"Clipped Line Endpoints:")
    print(f"P1' = ({x1:.2f}, {y1:.2f})")
    print(f"P2' = ({x2:.2f}, {y2:.2f})")
else:
    print("\nLine Rejected")

# ---------------- Plot ----------------

plt.figure(figsize=(8, 8))

# Clipping Window
plt.plot([xmin, xmax], [ymin, ymin], 'k')
plt.plot([xmax, xmax], [ymin, ymax], 'k')
plt.plot([xmax, xmin], [ymax, ymax], 'k')
plt.plot([xmin, xmin], [ymax, ymin], 'k')

# Original Line
plt.plot([ox1, ox2], [oy1, oy2],
         'r--', linewidth=2, label="Original Line")

# Clipped Line
if accept:
    plt.plot([x1, x2], [y1, y2],
             'b', linewidth=3, label="Clipped Line")

plt.scatter([ox1, ox2], [oy1, oy2], color='red')
if accept:
    plt.scatter([x1, x2], [y1, y2], color='blue')

plt.title("Cohen-Sutherland Line Clipping")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()