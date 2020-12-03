#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2020/12/3 13:06
__author__ = "hanruobing"


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        hashmap = {}
        for i, num in enumerate(nums):
            if hashmap.get(target - num) is not None:
                return [i, hashmap.get(target - num)]
            hashmap[num] = i  # 这句不能放在if语句之前，解决list中有重复值或target-num=num的情况
            
        #之前遍历列表超时