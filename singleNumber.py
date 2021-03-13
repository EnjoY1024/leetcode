#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/13 21:43
__author__ = "hanruobing"

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(set(nums))*2-sum(nums)

s = Solution()
print(s.singleNumber([2,2,1]))