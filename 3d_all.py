
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import math

def plot_object(ax, xs, ys, zs, label):
    ax.plot(xs, ys, zs, marker="o", linewidth=2, label=label)

n = int(input("Enter number of vertices: "))

x=[]; y=[]; z=[]
for i in range(n):
    x.append(float(input(f"x{i+1}: ")))
    y.append(float(input(f"y{i+1}: ")))
    z.append(float(input(f"z{i+1}: ")))

x.append(x[0]); y.append(y[0]); z.append(z[0])

print("""
1. Translation
2. Scaling
3. Rotation
4. Shearing
5. Reflection
""")
choice=int(input("Choice: "))

fig=plt.figure(figsize=(9,9))
ax=fig.add_subplot(111,projection="3d")
plot_object(ax,x,y,z,"Original")

match choice:
    case 1:
        tx=float(input("tx: "))
        ty=float(input("ty: "))
        tz=float(input("tz: "))
        xn=[i+tx for i in x]
        yn=[i+ty for i in y]
        zn=[i+tz for i in z]
        plot_object(ax,xn,yn,zn,"Translation")

    case 2:
        sx=float(input("sx: "))
        sy=float(input("sy: "))
        sz=float(input("sz: "))
        xn=[i*sx for i in x]
        yn=[i*sy for i in y]
        zn=[i*sz for i in z]
        plot_object(ax,xn,yn,zn,"Scaling")

    case 3:
        print("1.X 2.Y 3.Z")
        c=int(input("Rotation: "))
        a=math.radians(float(input("Angle: ")))
        xn=[];yn=[];zn=[]
        for i in range(len(x)):
            if c==1:
                xn.append(x[i]); yn.append(y[i]*math.cos(a)-z[i]*math.sin(a)); zn.append(y[i]*math.sin(a)+z[i]*math.cos(a))
            elif c==2:
                xn.append(x[i]*math.cos(a)+z[i]*math.sin(a)); yn.append(y[i]); zn.append(-x[i]*math.sin(a)+z[i]*math.cos(a))
            else:
                xn.append(x[i]*math.cos(a)-y[i]*math.sin(a)); yn.append(x[i]*math.sin(a)+y[i]*math.cos(a)); zn.append(z[i])
        plot_object(ax,xn,yn,zn,"Rotation")

    case 4:
        print("1.X 2.Y 3.Z 4.XY 5.YZ 6.XZ 7.XYZ")
        c=int(input("Shearing type: "))
        shx=float(input("shx: "))
        shy=float(input("shy: "))
        shz=float(input("shz: "))
        xn=[];yn=[];zn=[]
        for i in range(len(x)):
            xx,yy,zz=x[i],y[i],z[i]
            if c==1:
                xx=xx+shx*yy
            elif c==2:
                yy=yy+shy*zz
            elif c==3:
                zz=zz+shz*xx
            elif c==4:
                xx=xx+shx*yy; yy=yy+shy*xx
            elif c==5:
                yy=yy+shy*zz; zz=zz+shz*yy
            elif c==6:
                xx=xx+shx*zz; zz=zz+shz*xx
            else:
                xx=xx+shx*yy
                yy=yy+shy*zz
                zz=zz+shz*xx
            xn.append(xx); yn.append(yy); zn.append(zz)
        plot_object(ax,xn,yn,zn,"Shearing")

    case 5:
        print("1.XY Plane 2.YZ Plane 3.ZX Plane 4.X-axis 5.Y-axis 6.Z-axis 7.Origin")
        c=int(input("Reflection type: "))
        xn=[];yn=[];zn=[]
        for i in range(len(x)):
            xx,yy,zz=x[i],y[i],z[i]
            if c==1: zz=-zz
            elif c==2: xx=-xx
            elif c==3: yy=-yy
            elif c==4: yy=-yy; zz=-zz
            elif c==5: xx=-xx; zz=-zz
            elif c==6: xx=-xx; yy=-yy
            else: xx=-xx; yy=-yy; zz=-zz
            xn.append(xx); yn.append(yy); zn.append(zz)
        plot_object(ax,xn,yn,zn,"Reflection")

for i in range(len(x)-1):
    ax.text(x[i],y[i],z[i],f"P{i}")

ax.set_xlabel("X")
ax.set_ylabel("Y")
ax.set_zlabel("Z")
ax.legend()
plt.show()
