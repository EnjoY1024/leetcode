#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time : 2021/2/19 22:29
__author__ = "hanruobing"


class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        strn =''
        for i in digits:
            strn += str(i)
        number = int(strn)
        plus = number+1

        plus_str = str(plus)

        rr = []

        for s in plus_str:
            rr.append(int(s))

        return rr


s = Solution()
print(s.plusOne(['1','2','3']))