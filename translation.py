import matplotlib.pyplot as plt

n = int(input("Enter number of vertices: "))

x = []
y = []

print("Enter coordinates:")

for i in range(n):
    x.append(float(input(f"x{i+1}: ")))
    y.append(float(input(f"y{i+1}: ")))

x.append(x[0])
y.append(y[0])

tx = float(input("Enter Translation in X: "))
ty = float(input("Enter Translation in Y: "))

x_new = [i + tx for i in x]
y_new = [i + ty for i in y]

plt.figure(figsize=(8,8))
plt.axhline(0,color='black')
plt.axvline(0,color='black')

plt.plot(x,y,'bo-',label="Original")
plt.plot(x_new,y_new,'ro-',label="Translated")

plt.grid(True)
plt.axis('equal')
plt.legend()
plt.title("Translation")
plt.show()