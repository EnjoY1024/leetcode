#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/1/29 14:26
__author__ = "hanruobing"


'''
希尔排序的整体思想是将固定间隔的几个元素之间排序，然后再缩小这个间隔。这样到最后数列就成为了基本有序数列。

具体步骤：

计算一个增量（间隔）值

对元素进行增量元素进行比较，比如增量值为7，那么就对0,7,14,21…个元素进行插入排序

然后对1,8,15…进行排序，依次递增进行排序

所有元素排序完后，缩小增量比如为3，然后又重复上述第2，3步

最后缩小增量至1时，数列已经基本有序，最后一遍普通插入即可

'''
def shell_sort(arr):
    #希尔排序
    # 取整计算增量（间隔）值
    gap = len(arr) // 2
    while gap > 0:
        # 从增量值开始遍历比较
        for i in range(gap, len(arr)):
            j = i
            current = arr[i]
            # 元素与他同列的前面的每个元素比较，如果比前面的小则互换
            while j - gap >= 0 and current < arr[j - gap]:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = current
        # 缩小增量（间隔）值
        gap //= 2
    return arr

print(shell_sort([2,7,5,1,3,6]))