import matplotlib.pyplot as plt
import math

n=int(input("Enter number of vertices: "))

x=[]
y=[]

for i in range(n):
    x.append(float(input(f"x{i+1}: ")))
    y.append(float(input(f"y{i+1}: ")))

x.append(x[0])
y.append(y[0])

angle=float(input("Enter Rotation Angle: "))
rad=math.radians(angle)

x_new=[]
y_new=[]

for i in range(len(x)):
    xr=x[i]*math.cos(rad)-y[i]*math.sin(rad)
    yr=x[i]*math.sin(rad)+y[i]*math.cos(rad)

    x_new.append(xr)
    y_new.append(yr)

plt.figure(figsize=(8,8))
plt.axhline(0,color='black')
plt.axvline(0,color='black')

plt.plot(x,y,'bo-',label="Original")
plt.plot(x_new,y_new,'ro-',label="Rotated")

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Rotation")
plt.show()