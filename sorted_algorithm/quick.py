#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/29 10:19
__author__ = "hanruobing"

def quick_sort(arr):
    if len(arr) < 2:
        # 基线条件：为空或只包含一个元素的数组是“有序”的
        return arr
    else:
        # 递归条件
        pivot = arr[0]
        # 由所有小于基准值的元素组成的子数组
        less = [i for i in arr[1:] if i <= pivot]
        # 由所有大于基准值的元素组成的子数组
        greater = [i for i in arr[1:] if i > pivot]
        #递归调用
    return quick_sort(less) + [pivot] + quick_sort(greater)
    

print(quick_sort([2,7,5,1,3,6]))