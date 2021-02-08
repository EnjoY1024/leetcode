#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/8 21:49
__author__ = "hanruobing"


class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        for i in range(0,len(nums)):
            if nums[i] == target:
                return i
        if nums[-1]<target:
            return len(nums)

        for i in range(0,len(nums)):
            if nums[i] > target:
                if i == 0:
                    return 0
                elif i<len(nums):
                    return i

