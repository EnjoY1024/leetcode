#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 16:25
__author__ = "hanruobing"


class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n == 1:
        #     return 1
        # if n == 2:
        #     return 2
        # while n>2:
        #     return self.climbStairs(n-1)+self.climbStairs(n-2)

        # 上面超时
        
        a = 0
        b = 0
        c = 1
        for i in range(0, n):
            a = b
            b = c
            c = a + b
        return c


s = Solution()
print(s.climbStairs(3))