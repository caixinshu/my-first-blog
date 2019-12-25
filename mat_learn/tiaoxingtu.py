#!/usr/bin/env python
# -*- coding=utf-8 -*-

from matplotlib import pyplot as plt


'''
绘制条形图的实例

还有重叠的部分未找到原因
 '''

plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签

x = ['战狼','星级争霸','英雄联盟','cs:go','和平精英']
y = [56,10,30,5,8]

plt.barh(range(len(x)),y,height=0.3) #绘制横向条形图
# plt.bar(range(len(x)),y,height=0.3) #绘制条形图
plt.yticks(range(len(x)),x) #设置字符串在Y轴

plt.grid(alpha=0.3) # 绘制网格

# plt.legend() # 绘制图例

plt.show()