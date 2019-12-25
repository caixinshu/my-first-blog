#!/usr/bin/env python
# -*- coding=utf-8 -*-

import pandas as pd
import numpy as np

t = pd.Series([1,2,3,4,5])

d = {'a':1,'b':3,'c':123,'d':244,'e':113}
d1 = pd.Series(d)
# print(d1[d1>3])
# print(d1.index) #直接使用索引

f = pd.read_csv('./pd_test.csv')  #pandas读取csv文件方法
# print(f)

t1 = pd.DataFrame(np.arange(12).reshape(3,4),index=list('abc'),columns=list('wxyz'))
print(t1)