#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/28 17:06
__author__ = "hanruobing"

def insertion_sort(arr):
    #插入排序
    #  第一层for表示循环插入的遍数
    for i in range(1, len(arr)):
    # 设置当前需要插入的元素，从第二个开始遍历到最后一个元素，做为当前元素
        current = arr[i]
    # 前面的元素与当前元素（从前一个元素开始比较）
        pre_index = i - 1
        while pre_index >= 0 and arr[pre_index] > current:
            # 当比较元素大于当前元素则把比较元素后移
            arr[pre_index + 1] = arr[pre_index]
            # 往前选择下一个比较元素
            pre_index -= 1
            # 当比较元素小于当前元素，则将当前元素插入在 其后面
            arr[pre_index + 1] = current
    return arr
    

print(insertion_sort([2,7,5,1,3,6]))