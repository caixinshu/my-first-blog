#!/usr/bin/env python
# -*- coding=utf-8 -*-
from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

y_1 = [10,20,10,22,14,10,16,13,17,19]
y_2 = [10,10,9,3,1,4,16,21,31,27]

x_1 = range(1,11)
x_2 = range(11,22)

# plt.figure(figsize=(20,8),dpi=80)  # 设置图大小

plt.scatter(x_1,y_1)
plt.scatter(x_2,y_2)


plt.show()