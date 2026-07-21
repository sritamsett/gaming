import matplotlib.pyplot as plt
import math

# ---------- USER INPUT FOR OBJECT ----------
n = int(input("Enter number of vertices: "))

x = []
y = []

print("\nEnter coordinates of the object:")

for i in range(n):
    x_point = float(input(f"Enter x{i+1}: "))
    y_point = float(input(f"Enter y{i+1}: "))

    x.append(x_point)
    y.append(y_point)

# Close the shape
x.append(x[0])
y.append(y[0])

# ---------- MENU ----------
print("\n========== 2D TRANSFORMATIONS ==========")
print("1. Translation")
print("2. Scaling")
print("3. Rotation")
print("4. Shearing")
print("5. Reflection")

choice = int(input("\nEnter your choice: "))

# ---------- PLOT ----------
plt.figure(figsize=(10, 10))

# Draw X and Y axes
plt.axhline(0, color='black')
plt.axvline(0, color='black')

# ---------- ORIGINAL OBJECT ----------
plt.plot(
    x,
    y,
    marker='o',
    linewidth=2,
    label='Original Object'
)

# ---------- TRANSFORMATIONS ----------
match choice:

    # ==================================================
    # TRANSLATION
    # ==================================================
    case 1:

        tx = float(input("Enter translation in x direction: "))
        ty = float(input("Enter translation in y direction: "))

        x_new = [i + tx for i in x]
        y_new = [i + ty for i in y]

        plt.plot(
            x_new,
            y_new,
            marker='o',
            linewidth=2,
            label='Translation'
        )

    # ==================================================
    # SCALING
    # ==================================================
    case 2:

        sx = float(input("Enter scaling factor in x direction: "))
        sy = float(input("Enter scaling factor in y direction: "))

        x_new = [i * sx for i in x]
        y_new = [i * sy for i in y]

        plt.plot(
            x_new,
            y_new,
            marker='o',
            linewidth=2,
            label='Scaling'
        )

    # ==================================================
    # ROTATION
    # ==================================================
    case 3:

        angle = float(input("Enter rotation angle (degrees): "))

        rad = math.radians(angle)

        x_new = []
        y_new = []

        for i in range(len(x)):

            xr = x[i] * math.cos(rad) - y[i] * math.sin(rad)
            yr = x[i] * math.sin(rad) + y[i] * math.cos(rad)

            x_new.append(xr)
            y_new.append(yr)

        plt.plot(
            x_new,
            y_new,
            marker='o',
            linewidth=2,
            label='Rotation'
        )

    # ==================================================
    # SHEARING
    # ==================================================
    case 4:

        print("\nTypes of Shearing")
        print("1. X-Shearing")
        print("2. Y-Shearing")
        print("3. Both X and Y Shearing")

        sh_choice = int(input("Enter your choice: "))

        x_new = []
        y_new = []

        match sh_choice:

            # X-Shearing
            case 1:

                shx = float(input("Enter X-Shearing factor: "))

                for i in range(len(x)):
                    x_new.append(x[i] + shx * y[i])
                    y_new.append(y[i])

                label = "X-Shearing"

            # Y-Shearing
            case 2:

                shy = float(input("Enter Y-Shearing factor: "))

                for i in range(len(x)):
                    x_new.append(x[i])
                    y_new.append(y[i] + shy * x[i])

                label = "Y-Shearing"

            # Both X and Y Shearing
            case 3:

                shx = float(input("Enter X-Shearing factor: "))
                shy = float(input("Enter Y-Shearing factor: "))

                for i in range(len(x)):
                    xs = x[i] + shx * y[i]
                    ys = y[i] + shy * x[i]

                    x_new.append(xs)
                    y_new.append(ys)

                label = "Both X and Y Shearing"

            case _:
                print("Invalid Choice!")
                exit()

        plt.plot(
            x_new,
            y_new,
            marker='o',
            linewidth=2,
            label=label
        )

    # ==================================================
    # REFLECTION
    # ==================================================
    case 5:

        print("\nReflection Types")
        print("1. Reflection about X-axis")
        print("2. Reflection about Y-axis")
        print("3. Reflection about Origin")
        print("4. Reflection about line Y = X")
        print("5. Reflection about line Y = -X")

        r = int(input("Enter your choice: "))

        x_new = []
        y_new = []

        match r:

            # Reflection about X-axis
            case 1:

                for i in range(len(x)):
                    x_new.append(x[i])
                    y_new.append(-y[i])

                label = "Reflection about X-axis"

            # Reflection about Y-axis
            case 2:

                for i in range(len(x)):
                    x_new.append(-x[i])
                    y_new.append(y[i])

                label = "Reflection about Y-axis"

            # Reflection about Origin
            case 3:

                for i in range(len(x)):
                    x_new.append(-x[i])
                    y_new.append(-y[i])

                label = "Reflection about Origin"

            # Reflection about Y = X
            case 4:

                for i in range(len(x)):
                    x_new.append(y[i])
                    y_new.append(x[i])

                label = "Reflection about Y = X"

            # Reflection about Y = -X
            case 5:

                for i in range(len(x)):
                    x_new.append(-y[i])
                    y_new.append(-x[i])

                label = "Reflection about Y = -X"

            case _:
                print("Invalid Choice!")
                exit()

        plt.plot(
            x_new,
            y_new,
            marker='o',
            linewidth=2,
            label=label
        )

    # ==================================================
    # INVALID CHOICE
    # ==================================================
    case _:
        print("Invalid Choice!")
        exit()

# ---------- LABEL ORIGINAL POINTS ----------
for i in range(len(x) - 1):
    plt.text(
        x[i],
        y[i],
        f"({x[i]}, {y[i]})",
        fontsize=9
    )

# ---------- GRAPH SETTINGS ----------
plt.grid(True, linestyle='--')
plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("2D Transformations")
plt.axis('equal')
plt.legend()

plt.show()