#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/26 22:29
__author__ = "hanruobing"


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minValue = float("inf")
        res = 0
        minValue = float("inf")
        for i in range(len(prices)):
            if prices[i] < minValue:  # 更新最小值
                minValue = prices[i]

            if prices[i] - minValue > res:  # 更新最大收益
                res = prices[i] - minValue
        print(minValue)
        return res


#两个for遍历相减取最大超时

s = Solution()
print(s.maxProfit([2,6,1,3]))
