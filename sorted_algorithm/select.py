#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/29 10:01
__author__ = "hanruobing"

def selection_sort(arr):
    #选择排序
    # 第一层for表示循环选择的遍数
    for i in range(len(arr) - 1):
        # 将起始元素设为最小元素
        min_index = i
        # 第二层for表示最小元素和后面的元素逐个比较
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
            # 如果当前元素比最小元素小，则把当前元素角标记为最小元素角标
                min_index = j
        # 查找一遍后找到最小元素脚标，与遍历的目标元素互换
        arr[min_index], arr[i] = arr[i], arr[min_index]
    return arr


print(selection_sort([2,7,5,1,3,6]))
