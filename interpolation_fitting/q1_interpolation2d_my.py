import numpy as np
import pylab as pl
from scipy import interpolate 
import matplotlib.pyplot as plt
plt.rcParams['font.sans-serif'] = ['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus'] = False #用来正常显示负号

##插值
# 根据题目写入x,y,z三个矩阵
x = np.array([1200,1600,2000,2400,2800,3200,3600,4000])
y = np.array([1200,1600,2000,2400,2800,3200,3600])
z = np.array([
    [1130,1250,1280,1230,1040,900,500,700],
    [1320,1450,1420,1400,1300,700,900,850],
    [1390,1500,1500,1400,900,1100,1060,950],
    [1500,1200,1100,1350,1450,1200,1150,1010],
    [1500,1200,1100,1550,1600,1550,1380,1070],
    [1500,1550,1600,1550,1600,1600,1600,1550],
    [1480,1500,1550,1510,1430,1300,1200,980]
    ])
    
# 生成网格点的坐标 xx,yy (二维数组)
xx, yy = np.meshgrid(x, y)  
# 二维插值
f_linear = interpolate.interp2d(xx, yy,z,kind='linear')
# 插值点集
x_new = np.linspace(1200,4000,100)
y_new = np.linspace(1200,3600,100)
z_new = f_linear(x_new,y_new)

# 绘图
fig = plt.figure(figsize=(16,16))
ax1 = plt.subplot(2,2,1,projection='3d')
ax1.set_title("2-D original data")
surf = ax1.plot_surface(xx,yy,z,rstride=2,cstride=2,cmap=plt.cm.coolwarm)
ax1.set_zlabel('zData')
xx_new,yy_new = np.meshgrid(x_new,y_new)
ax2 = plt.subplot(2,2,2,projection='3d')
ax2.set_title("2-D interpolation data")
ax2.plot_wireframe(xx_new,yy_new,z_new,rstride=2,cstride=2,linewidth=1)
surf2 = ax2.plot_surface(xx_new,yy_new,z_new,rstride=2,cstride=2,cmap=plt.cm.coolwarm)
ax2.set_zlabel("zInter")

ax3 = plt.subplot(2,2,3,projection='3d')
ax3.set_title("2-D contour")
# 画网格线
# ax3.plot_wireframe(xx_new,yy_new,z_new,rstride=2,cstride=2,linewidth=1)
# surf3 = ax2.plot_surface(xx_new,yy_new,z_new,rstride=2,cstride=2,cmap=plt.cm.coolwarm)
ax3.set_zlabel("zInter")
#画出8条线，并将颜色设置为黑色
cset = plt.contourf(xx_new,yy_new,z_new,20,cmap=plt.cm.hot) 
contour = plt.contour(xx_new,yy_new,z_new,10,colors='k')
#等高线上标明z（即高度）的值，字体大小是10，颜色分别是黑色和红色
plt.clabel(contour,fontsize=10,colors='k')

z_height = z_new
z_height[z_height<1400]=0
# np.where(z_height > 1400, z_height, 0)
print(z_height)
ax4 = plt.subplot(2,2,4,projection='3d')
ax4.set_title("2-D interpolation data")
ax4.plot_wireframe(xx_new,yy_new,z_height,rstride=2,cstride=2,linewidth=1)
surf4 = ax4.plot_surface(xx_new,yy_new,z_height,rstride=2,cstride=2,cmap=plt.cm.coolwarm)
ax4.set_zlabel("zInter")
# ax4.set_zlim3d(1400,2000)
# plt.zlim(zmin=1400)
plt.show()
