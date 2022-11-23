import numpy as np
import matplotlib.pyplot as plt
T=np.arange(10, 90, 10)
y0=np.array([0.1, 0.3, 0.7, 0.94, 0.95, 0.68, 0.34, 0.13])
p=np.polyfit(T, y0, 2) #拟合多项式 (2次)
print("拟合二次多项式的从高次幂到低次幂系数分别为:",p)
yhat=np.polyval(p,100) #预测
print("100°时预测值转化率为：", yhat)
plt.rc('font',size=16)
# 自己写函数方式
# T_draw = np.arange(10, 90, 1)
# y_draw = T_draw*T_draw*p[0]+T_draw*p[1]+p[2]
# plt.plot(T, y0, '*', T_draw, y_draw, '-')

T_draw = np.arange(10, 90, 1)
plt.plot(T, y0, '*', T_draw, np.polyval(p,T_draw), '-')
plt.show()

from scipy.optimize import fminbound
maximum = fminbound(lambda x: -np.polyval(p,x), 40, 60)
max=np.polyval(p,maximum)
print('Polynomial最大值为:',max)