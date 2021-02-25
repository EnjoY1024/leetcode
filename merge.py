#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 16:35
__author__ = "hanruobing"

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """
        nums1[m:m + n] = nums2[:n]
        nums1.sort()
        return nums1

s = Solution()
print(s.merge([1,2,3,0,0,0], 3, [2,5,6],3))