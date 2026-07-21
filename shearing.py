import matplotlib.pyplot as plt

n=int(input("Enter number of vertices: "))

x=[]
y=[]

for i in range(n):
    x.append(float(input(f"x{i+1}: ")))
    y.append(float(input(f"y{i+1}: ")))

x.append(x[0])
y.append(y[0])

print("1. X Shearing")
print("2. Y Shearing")
print("3. Both")

choice=int(input("Choice: "))

x_new=[]
y_new=[]

if choice==1:

    shx=float(input("Enter X Shearing Factor: "))

    for i in range(len(x)):
        x_new.append(x[i]+shx*y[i])
        y_new.append(y[i])

elif choice==2:

    shy=float(input("Enter Y Shearing Factor: "))

    for i in range(len(x)):
        x_new.append(x[i])
        y_new.append(y[i]+shy*x[i])

elif choice==3:

    shx=float(input("Enter X Shearing Factor: "))
    shy=float(input("Enter Y Shearing Factor: "))

    for i in range(len(x)):
        x_new.append(x[i]+shx*y[i])
        y_new.append(y[i]+shy*x[i])

plt.figure(figsize=(8,8))
plt.axhline(0,color='black')
plt.axvline(0,color='black')

plt.plot(x,y,'bo-',label="Original")
plt.plot(x_new,y_new,'ro-',label="Sheared")

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Shearing")
plt.show()