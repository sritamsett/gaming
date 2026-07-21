import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

# ---------- USER INPUT FOR 3D OBJECT ----------
n = int(input("Enter number of vertices: "))

x = []
y = []
z = []

print("\nEnter coordinates of the 3D object:")

for i in range(n):

    x_point = float(input(f"Enter x{i+1}: "))
    y_point = float(input(f"Enter y{i+1}: "))
    z_point = float(input(f"Enter z{i+1}: "))

    x.append(x_point)
    y.append(y_point)
    z.append(z_point)

# Close the shape
x.append(x[0])
y.append(y[0])
z.append(z[0])

# ---------- MENU ----------
print("\n========== 3D TRANSFORMATIONS ==========")
print("1. Translation")
print("2. Scaling")
print("3. Rotation about X-axis")
print("4. Rotation about Y-axis")
print("5. Rotation about Z-axis")
print("6. Shearing")

choice = int(input("\nEnter your choice: "))

# ---------- CREATE 3D FIGURE ----------
fig = plt.figure(figsize=(10, 10))
ax = fig.add_subplot(111, projection='3d')

# ---------- ORIGINAL OBJECT ----------
ax.plot(
    x,
    y,
    z,
    marker='o',
    linewidth=2,
    label='Original Object'
)

# ---------- SWITCH CASE ----------
match choice:

    # ---------- TRANSLATION ----------
    case 1:

        tx = float(input("Enter translation in x direction: "))
        ty = float(input("Enter translation in y direction: "))
        tz = float(input("Enter translation in z direction: "))

        x_new = [i + tx for i in x]
        y_new = [i + ty for i in y]
        z_new = [i + tz for i in z]

        ax.plot(
            x_new,
            y_new,
            z_new,
            marker='o',
            linewidth=2,
            label='Translation'
        )

    # ---------- SCALING ----------
    case 2:

        sx = float(input("Enter scaling factor in x direction: "))
        sy = float(input("Enter scaling factor in y direction: "))
        sz = float(input("Enter scaling factor in z direction: "))

        x_new = [i * sx for i in x]
        y_new = [i * sy for i in y]
        z_new = [i * sz for i in z]

        ax.plot(
            x_new,
            y_new,
            z_new,
            marker='o',
            linewidth=2,
            label='Scaling'
        )

    # ---------- ROTATION ABOUT X-AXIS ----------
    case 3:

        angle = float(input("Enter rotation angle in degrees: "))
        rad = math.radians(angle)

        x_new = []
        y_new = []
        z_new = []

        for i in range(len(x)):

            xr = x[i]
            yr = y[i] * math.cos(rad) - z[i] * math.sin(rad)
            zr = y[i] * math.sin(rad) + z[i] * math.cos(rad)

            x_new.append(xr)
            y_new.append(yr)
            z_new.append(zr)

        ax.plot(
            x_new,
            y_new,
            z_new,
            marker='o',
            linewidth=2,
            label='Rotation X-axis'
        )

    # ---------- ROTATION ABOUT Y-AXIS ----------
    case 4:

        angle = float(input("Enter rotation angle in degrees: "))
        rad = math.radians(angle)

        x_new = []
        y_new = []
        z_new = []

        for i in range(len(x)):

            xr = x[i] * math.cos(rad) + z[i] * math.sin(rad)
            yr = y[i]
            zr = -x[i] * math.sin(rad) + z[i] * math.cos(rad)

            x_new.append(xr)
            y_new.append(yr)
            z_new.append(zr)

        ax.plot(
            x_new,
            y_new,
            z_new,
            marker='o',
            linewidth=2,
            label='Rotation Y-axis'
        )

    # ---------- ROTATION ABOUT Z-AXIS ----------
    case 5:

        angle = float(input("Enter rotation angle in degrees: "))
        rad = math.radians(angle)

        x_new = []
        y_new = []
        z_new = []

        for i in range(len(x)):

            xr = x[i] * math.cos(rad) - y[i] * math.sin(rad)
            yr = x[i] * math.sin(rad) + y[i] * math.cos(rad)
            zr = z[i]

            x_new.append(xr)
            y_new.append(yr)
            z_new.append(zr)

        ax.plot(
            x_new,
            y_new,
            z_new,
            marker='o',
            linewidth=2,
            label='Rotation Z-axis'
        )

    # ---------- SHEARING ----------
    case 6:

        shx = float(input("Enter shearing factor in x direction: "))
        shy = float(input("Enter shearing factor in y direction: "))
        shz = float(input("Enter shearing factor in z direction: "))

        x_new = []
        y_new = []
        z_new = []

        for i in range(len(x)):

            xs = x[i] + shx * y[i]
            ys = y[i] + shy * z[i]
            zs = z[i] + shz * x[i]

            x_new.append(xs)
            y_new.append(ys)
            z_new.append(zs)

        ax.plot(
            x_new,
            y_new,
            z_new,
            marker='o',
            linewidth=2,
            label='Shearing'
        )

    # ---------- INVALID CHOICE ----------
    case _:
        print("Invalid Choice!")

# ---------- LABEL ORIGINAL POINTS ----------
for i in range(len(x)-1):

    ax.text(
        x[i],
        y[i],
        z[i],
        f"({x[i]}, {y[i]}, {z[i]})",
        fontsize=8
    )

# Labels
ax.set_xlabel("X Axis")
ax.set_ylabel("Y Axis")
ax.set_zlabel("Z Axis")

# Title
ax.set_title("3D Transformations")

# Legend
ax.legend()

# Show Plot
plt.show()