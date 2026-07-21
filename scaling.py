import matplotlib.pyplot as plt

n = int(input("Enter number of vertices: "))

x=[]
y=[]

for i in range(n):
    x.append(float(input(f"x{i+1}: ")))
    y.append(float(input(f"y{i+1}: ")))

x.append(x[0])
y.append(y[0])

sx=float(input("Scaling factor X: "))
sy=float(input("Scaling factor Y: "))

x_new=[i*sx for i in x]
y_new=[i*sy for i in y]

plt.figure(figsize=(8,8))
plt.axhline(0,color='black')
plt.axvline(0,color='black')

plt.plot(x,y,'bo-',label="Original")
plt.plot(x_new,y_new,'ro-',label="Scaled")

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Scaling")
plt.show()