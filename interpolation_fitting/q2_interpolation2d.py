import numpy as np
import pylab as pl
from scipy import interpolate 
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

##插值
# 根据题目写入x,y,z三个矩阵
x = np.linspace(5,85,9)
y = np.linspace(1,12,12)

# x = np.array([1200,1600,2000,2400,2800,3200,3600,4000])
# y = np.array([1200,1600,2000,2400,2800,3200,3600])
z = np.array([
    [2.4,   18.7,   20.8,  22.1,    37.3,   48.2,   25.6,   5.3,    0.3],
    [1.6,   21.4,   18.5,  20.1,    28.8,   36.6,   24.2,   5.3,    0],
    [2.4,   16.2,   18.2,  20.5,    27.8,   35.5,   25.5,   5.4,    0],
    [3.2,   9.2,    16.6,  25.1,    37.2,   40,     24.6,   4.9,    0.3],
    [1.0,   2.8,    12.9,  29.2,    40.3,   37.6,   21.1,   4.9,    0],
    [0.5,   1.7,    10.1,  32.6,    41.7,   35.4,   22.2,   7.1,    0],
    [0.4,   1.4,    8.3,   33.0,    46.2,   35,     20.2,   5.3,    0.1],
    [0.2,   2.4,    11.2,  31.0,    39.9,   34.7,   21.2,   7.3,    0.2],
    [0.5,   5.8,    12.5,  28.6,    25.9,   35.7,   22.6,   7,      0.3],
    [0.8,   9.2,    21.1,  32.0,    40.3,   39.5,   28.5,   8.6,    0],
    [2.4,   10.3,   23.9,  28.1,    38.2,   40,     25.3,   6.3,    0.1],
    [3.6,   16,     25.5,  25.6,    43.4,   41.9,   24.3,   6.6,    0.3]
    ])
    
# 生成网格点的坐标 xx,yy (二维数组)
xx, yy = np.meshgrid(x, y)  
# 二维插值
f_linear = interpolate.interp2d(xx, yy,z,kind='quintic')
# 插值点集
x_new = np.linspace(0,90,100)
y_new = np.linspace(1,12,100)
z_new = f_linear(x_new,y_new)

# 绘图
fig = plt.figure(figsize=(12,12))
ax1 = plt.subplot(1,2,1,projection='3d')
ax1.set_title("2-D original data")
surf = ax1.plot_surface(xx,yy,z,rstride=2,cstride=2,cmap=plt.cm.viridis)
ax1.set_zlabel('zData')
ax1.set_xlabel(u"纬度/°")
ax1.set_ylabel(u"月份")
ax1.set_xlim(0,90)
ax1.set_ylim(1,12)
ax1.set_xticks(np.linspace(0,90,10))
ax1.set_yticks(np.linspace(1,12,12))


xx_new,yy_new = np.meshgrid(x_new,y_new)
ax2 = plt.subplot(1,2,2,projection='3d')
ax2.set_title("2-D quintic interpolation data")
ax2.plot_wireframe(xx_new,yy_new,z_new,rstride=2,cstride=2,linewidth=1)
surf2 = ax2.plot_surface(xx_new,yy_new,z_new,rstride=2,cstride=2,cmap=plt.cm.viridis)
ax2.set_zlabel("cyclone")
ax2.set_xlabel(u"纬度/°")
ax2.set_ylabel(u"月份")
ax2.set_xlim(0,90)
ax2.set_ylim(1,12)
ax2.set_xticks(np.linspace(0,90,10))
ax2.set_yticks(np.linspace(1,12,12))

plt.show()
