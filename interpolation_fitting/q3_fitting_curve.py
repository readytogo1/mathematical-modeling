# import numpy as np
# from scipy.optimize import curve_fit
# y=lambda x, a, b, c: a*x**2+b*x+c #定义拟合函数
# x0=np.arange(0, 1.1, 0.1)
# y0=np.array([-0.447, 1.978, 3.28, 6.16, 7.08, 7.34, 7.66, 9.56, 9.48, 9.30, 11.2])
# popt, pcov=curve_fit(y, x0, y0) #用curve_fit函数拟合
# print("拟合的参数值为：", popt)
# print("预测值分别为：", y(np.array([0.25, 0.35]), *popt))
import matplotlib.pyplot as plt

from scipy.optimize import curve_fit

import numpy as np

#用指数形式来拟合

x=np.arange(10, 90, 10)
y=np.array([0.1, 0.3, 0.7, 0.94, 0.95, 0.68, 0.34, 0.13])

def func(x,b1,b2,b3):
      return b1/(b3+b2*(x-45)*(x-45))

popt,pcov=curve_fit(func,x,y)

print('b1,b2,b3的值分别为:',popt)
# popt里面是拟合系数
a,b,c=popt 
# 预测
yhat=func(100,a,b,c) 
print("100°时预测值转化率为：", yhat)
# 绘图
# x_new = np.arange(10, 90, 1)
# yvals=func(x_new,a,b,c)
# plot1=plt.plot(x,y,'*',label='original values')
# plot2=plt.plot(x_new,yvals,'r',label='curve_fit values')
# plt.xlabel('T')
# plt.ylabel('y')
# plt.legend(loc=1)  #指定图例位置为右上角
# plt.title('curve_fit')

# plt.show()

# 找出最大值
from scipy.optimize import fminbound
maximum = fminbound(lambda x: -func(x,a,b,c), 40, 60)
max=func(maximum,a,b,c)
print('curvefit最大值为:',max)
