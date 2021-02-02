#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/2 22:20
__author__ = "hanruobing"


class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # i = 0
        # for j in range(0,len(nums)):
        #     if nums[j]!=val:
        #         nums[i]==nums[j]
        #         i= i+1
        # return i



###
        for i in nums:
            nums.remove(val)
        return nums

s = Solution()
print(s.removeElement([3,2,2,3],3))