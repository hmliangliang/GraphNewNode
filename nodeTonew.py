#!/usr/bin/python3.8
# -*- coding: utf-8 -*-
# @Time    : 2021/10/25 16:44
# @Author  : Shuliang Xu
# @File    : LgameGNN.py
# @Software: PyCharm

import numpy as np

def reshapeGraph(data,signal):
    '''
    当图中节点编号不连续时，对图中的节点进行重新编号
    data:图的边矩阵，n行2列,每一行表示一条边
    signal: 0或1  0:表示该图为无向图   1:表示该图为有向图
    '''
    data = np.random.rand(2, 3)
    nodeset = np.unique(data) #节点的集合
    row_len = data.shape[0]
    col_len = data.shape[1]
    # 重新对节点进行编号
    for i in range(row_len):
        for j in range(col_len):
            data[i, j] = np.argwhere(nodeset == data[i, j])[0][0]
    return data, nodeset