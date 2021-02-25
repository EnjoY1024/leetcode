#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/25 17:19
__author__ = "hanruobing"


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]

        r = [[1] * i for i in range(1, numRows + 1)]

        for i in range(3,numRows+1):
            for j in range(numRows):
                if j == 0 or j==numRows-1:
                    r[i][j] = 1
                else:
                    r[i][j] = r[i-1][j]+r[i-1][j+1]
        return r
#数组越界，不知道哪，需调试
    
s = Solution()
print(s.generate(3))