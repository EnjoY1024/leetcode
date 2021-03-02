#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/3/2 23:13
__author__ = "hanruobing"


class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        numRows = rowIndex + 1
        if rowIndex == 0:
            return [1]
        if rowIndex == 1:
            return [1, 1]

        r = [[1] * i for i in range(1, numRows + 1)]

        for i in range(2, numRows):
            for j in range(0, i + 1):
                if j == 0 or j == i:
                    r[i][j] = 1
                else:
                    # print(r[i-1][j-1]+r[i-1][j])
                    r[i][j] = r[i - 1][j - 1] + r[i - 1][j]
        return r[rowIndex]

s = Solution()
print(s.getRow(4))