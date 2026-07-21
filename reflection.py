import matplotlib.pyplot as plt

n=int(input("Enter number of vertices: "))

x=[]
y=[]

for i in range(n):
    x.append(float(input(f"x{i+1}: ")))
    y.append(float(input(f"y{i+1}: ")))

x.append(x[0])
y.append(y[0])

print("1. X-axis")
print("2. Y-axis")
print("3. Origin")
print("4. Y=X")
print("5. Y=-X")

r=int(input("Choice: "))

x_new=[]
y_new=[]

if r==1:

    for i in range(len(x)):
        x_new.append(x[i])
        y_new.append(-y[i])

elif r==2:

    for i in range(len(x)):
        x_new.append(-x[i])
        y_new.append(y[i])

elif r==3:

    for i in range(len(x)):
        x_new.append(-x[i])
        y_new.append(-y[i])

elif r==4:

    for i in range(len(x)):
        x_new.append(y[i])
        y_new.append(x[i])

elif r==5:

    for i in range(len(x)):
        x_new.append(-y[i])
        y_new.append(-x[i])

plt.figure(figsize=(8,8))
plt.axhline(0,color='black')
plt.axvline(0,color='black')

plt.plot(x,y,'bo-',label="Original")
plt.plot(x_new,y_new,'ro-',label="Reflection")

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Reflection")
plt.show()