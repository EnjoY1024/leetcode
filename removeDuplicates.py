#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/1 21:48
__author__ = "hanruobing"


class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums)==0:
            return 0


        i = 0
        for j in range(1,len(nums)):
            if nums[i]!=nums[j]:
                i =i+1
                nums[i] = nums[j]


        return  i+1


s = Solution()
print(s.removeDuplicates([1,1,2,3]))