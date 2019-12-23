#!/usr/bin/env python
# -*- coding=utf-8 -*-

from matplotlib import pyplot as plt
from matplotlib import font_manager
import random

# my_font = font_manager.FontProperties(fname="C:/Windows/Fonts/Cambria.ttf")
plt.rcParams['font.sans-serif']=['SimHei'] #用来正常显示中文标签
plt.rcParams['axes.unicode_minus']=False #用来正常显示负号

x = range(0,120)
y = [random.randint(20,35) for i in range(120)]

fig = plt.figure(figsize=(20,8))
plt.plot(x,y)


# 调整x轴
_xtick_labels = [u"10点{}分".format(i) for i in range(60)]
_xtick_labels += [u"11点{}分".format(i) for i in range(60)]
# 取步长，数字字符，数据长度
plt.xticks(list(x)[::3],_xtick_labels[::3],rotation=45)
plt.savefig("./fig.png")
plt.show()
