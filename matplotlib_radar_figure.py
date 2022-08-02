# -*- coding: utf-8 -*-
# Author: lkm
# date: 2022/8/2 16:35

import numpy as np
import matplotlib.pyplot as plt


def plot_radar(labels, data, score, title):
    n = len(labels)
    # 转化为十分制
    if score in [5, 10, 100]:
        data = data * 10 /score
    elif score == 1:
        data = data * 10

