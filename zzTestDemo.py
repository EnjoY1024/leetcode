#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/24 9:37
__author__ = "hanruobing"


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        dic = {}
        resp = []
        for num in array:
            if num in dic:
                dic[num] += 1
            else:
                dic[num] = 1
        for k, v in dic.items():
            if v == 1:
                resp.append(k)

        return resp

s = Solution()
print(s.FindNumsAppearOnce([1,2,3,3,2,4,4,5]))