#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/29 10:11
__author__ = "hanruobing"

def bubble_sort(arr):
    #冒泡排序
    # 第一层for表示循环的遍数
    for i in range(len(arr) - 1):
        # 第二层for表示具体比较哪两个元素
        for j in range(len(arr) - 1 - i):
            if arr[j] > arr[j + 1]:
            # 如果前面的大于后面的，则交换这两个元素的位置
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr
print(bubble_sort([2,7,5,1,3,6]))