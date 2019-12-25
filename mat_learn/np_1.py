#!/usr/bin/env python
# -*- coding=utf-8 -*-

import numpy

t1 = numpy.arange(12)
t2 = numpy.arange(48)
t3 = numpy.array([[11,2,3],[11,2,3],[11,2,3],[11,2,3],[11,2,3],[11,2,3],])

print('*'*30)

# print(t1.reshape((3,4)))
# print(t2.reshape(2,3,4))

# print(t3[:,1:3])
'''
t3[:,1:3]
逗号前是行，后面是列
'''
print(numpy.random.randint(0,20,(3,4)))