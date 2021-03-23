#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/23 22:05
__author__ = "hanruobing"

class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        #常规想法超时，数组有序，则按二分查找

        for i in range (len(numbers)):
            low = i+1
            high = len(numbers)-1
            while low <= high:
                mid = (low + high) //2
                if numbers[mid] == target-numbers[i]:
                    return [i+1,mid+1]
                elif numbers[mid] < target - numbers[i]:
                    low = mid+1
                else:
                    high = mid-1
        return [-1,-1]

s = Solution()
print(s.twoSum( [5,25,75],100))