#!/usr/bin/env python
# -*- coding=utf-8 -*-

from matplotlib import pyplot as plt

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

y_1 = [1,2,0,2,1,0,1,1,1,1]
y_2 = [0,0,0,0,1,0,0,1,1,1]
x = range(20,30)

# plt.figure(figsize=(20,8),dpi=80)  # 设置图大小

plt.plot(x,y_1,label="小王") # 画图
plt.plot(x,y_2,label="小李") # 画图

# 设置x轴刻度
_xtick_labels = ["{}岁".format(i) for i in x]
plt.xticks(x,_xtick_labels)

plt.grid(alpha=1) # 绘制网格


plt.show() # 展示

