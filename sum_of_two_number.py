#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/9/6 10:19
__author__ = "hanruobing"

#返回列表中两数之和为target的两个数的索引
class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        len_nums = len(nums)
        print (len_nums)
        for i in [0, len_nums]:
            r = nums[i]
            print (r)
            n = nums[:]
            print(n,type(n),type(n[0]))

            others = n.remove(r)
            print(others)
            # for j in [0, len_nums - 1]:
            #     if nums[i] + others[j] == target:
            #         k = nums.index(others[j])
            #         return [i, k]
            #     else:
            #         return 0

test = Solution()
a = test.twoSum([1,3,2,6],5)
print(a)
#     a = [1, 2, 3, 4, 5, 2, 6]
#     a.remove(2)
#     print(a)