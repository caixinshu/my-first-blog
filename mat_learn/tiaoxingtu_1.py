#!/usr/bin/env python
# -*- coding=utf-8 -*-

from matplotlib import pyplot as plt


'''
绘制多条形图的实例
 '''

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

x = ['战狼','星级争霸','英雄联盟','cs:go','和平精英']
y_1 = [56,10,30,5,8]
y_2 = [50,16,34,9,18]
y_3 = [45,19,23,12,4]

bar_w = 0.2 # 设置条形图间距

x_1 = list(range(len(x)))
x_2 = [i*bar_w for i in x_1]
x_3 = [i*bar_w*2 for i in x_1]

# 绘制条形图,无间距会导致条形图重叠
plt.bar(range(len(x)),y_1,width=bar_w,label='x月6时')
plt.bar(x_2,y_2,width=bar_w,label='x月12时')
plt.bar(x_3,y_3,width=bar_w,label='x月18时')

# 设置x轴的刻度
plt.xticks(x_1,x)


plt.legend()
plt.show()

