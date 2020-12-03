#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 13:09
__author__ = "hanruobing"

class Solution(object):
    def runningSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        runningSum = []
        sum = 0
        for i in range(len(nums)):
            sum = sum + nums[i]
            runningSum.append(sum)
        return runningSum